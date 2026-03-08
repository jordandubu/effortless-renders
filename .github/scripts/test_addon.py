#!/usr/bin/env python3
"""
Headless Blender addon validation script.
Runs via `bpy` (Blender as Python module) to test register/unregister.
Used by the blender-compat GitHub Actions workflow.
"""

import sys
import os
import traceback

# ── Mock modules not available in bpy's Python ──────────────────────
# `requests` is not bundled with bpy, so we mock it before importing the addon.
import types

mock_requests = types.ModuleType("requests")
mock_requests.get = lambda *a, **kw: None
mock_requests.RequestException = Exception
sys.modules["requests"] = mock_requests

# ── Setup addon path ────────────────────────────────────────────────
# The addon source should be in the repo root. We add it so the addon
# can be imported as a package.
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ADDON_DIR = REPO_ROOT  # The addon IS the repo root

# We need to add the parent so `import effortless-renders` would work,
# but since the package name has a hyphen, we'll copy/symlink or just
# import directly. For bpy addons, we install via bpy.utils.

errors = []


def test_bl_info():
    """Validate bl_info has all required keys."""
    print("── Testing bl_info ──")
    sys.path.insert(0, REPO_ROOT)

    # Import __init__.py directly
    init_path = os.path.join(ADDON_DIR, "__init__.py")
    if not os.path.exists(init_path):
        errors.append("__init__.py not found at repo root")
        return

    import importlib.util
    spec = importlib.util.spec_from_file_location("addon_init", init_path)
    mod = importlib.util.module_from_spec(spec)

    # We can't fully exec it without bpy context, but we can parse bl_info
    import ast
    with open(init_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    bl_info = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "bl_info":
                    bl_info = ast.literal_eval(node.value)

    if bl_info is None:
        errors.append("bl_info not found in __init__.py")
        return

    required_keys = ["name", "version", "blender", "category"]
    for key in required_keys:
        if key not in bl_info:
            errors.append(f"bl_info missing required key: '{key}'")

    print(f"  bl_info = {bl_info}")
    print(f"  ✅ bl_info validation passed")


def test_register_unregister():
    """Test that the addon can register and unregister in Blender."""
    print("\n── Testing register/unregister ──")
    
    # CRITICAL FIX: Use the standardized name that Blender will actually use.
    # If the repository name or folder name has hyphens, this test should 
    # help us identify that it's an invalid Python module name.
    addon_name = "effortless_renders" 
    
    import re
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', addon_name):
        errors.append(f"Invalid addon name '{addon_name}': Module names cannot contain hyphens or dots.")
        print(f"  ❌ Invalid module name: {addon_name}")
        return

    try:
        import bpy
    except ImportError:
        errors.append("bpy not available — cannot test register/unregister")
        return

    # Create a temporary addon directory that bpy can load
    tmp_dir = tempfile.mkdtemp()
    addon_dst = os.path.join(tmp_dir, addon_name)
    
    # Copy addon files
    py_files = [f for f in os.listdir(ADDON_DIR) if f.endswith(".py")]
    os.makedirs(addon_dst, exist_ok=True)
    for py_file in py_files:
        shutil.copy2(os.path.join(ADDON_DIR, py_file), os.path.join(addon_dst, py_file))

    # Add to Blender's addon search path
    bpy.utils.script_paths_pref().append(tmp_dir) if hasattr(bpy.utils, 'script_paths_pref') else None
    sys.path.insert(0, tmp_dir)

    try:
        # Try importing the addon package
        addon_mod = __import__(addon_name)
        
        # Test register
        print("  Calling register()...")
        addon_mod.register()
        print("  ✅ register() succeeded")

        # Verify specific operators exist
        print("  Verifying operators...")
        expected_ops = [
            "object.rendering_operator",
            "object.test_connection",
            "scene.import_scene",
            "object.import_helper_box",
            "object.open_library_path"
        ]
        
        for op_id in expected_ops:
            module, name = op_id.split(".")
            if hasattr(bpy.ops, module) and hasattr(getattr(bpy.ops, module), name):
                print(f"    ✅ {op_id} is registered")
            else:
                errors.append(f"Operator {op_id} failed to register (not found in bpy.ops)")
                print(f"    ❌ {op_id} NOT found")

        # Test unregister
        print("  Calling unregister()...")
        addon_mod.unregister()
        print("  ✅ unregister() succeeded")

    except Exception as e:
        tb = traceback.format_exc()
        errors.append(f"register/unregister failed:\n{tb}")
        print(f"  ❌ FAILED: {e}")
    finally:
        # Cleanup
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_syntax():
    """Check all .py files for syntax errors."""
    print("\n── Testing syntax ──")
    py_files = [f for f in os.listdir(ADDON_DIR) if f.endswith(".py")]

    for py_file in py_files:
        filepath = os.path.join(ADDON_DIR, py_file)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                compile(f.read(), filepath, "exec")
            print(f"  ✅ {py_file}")
        except SyntaxError as e:
            errors.append(f"Syntax error in {py_file}: {e}")
            print(f"  ❌ {py_file}: {e}")


if __name__ == "__main__":
    print("=" * 60)
    print("Effortless Renders — Addon Compatibility Test")
    print("=" * 60)

    test_bl_info()
    test_syntax()
    test_register_unregister()

    print("\n" + "=" * 60)
    if errors:
        print(f"❌ {len(errors)} ERROR(S) FOUND:")
        for i, err in enumerate(errors, 1):
            print(f"\n  [{i}] {err}")
        print("\n" + "=" * 60)
        sys.exit(1)
    else:
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        sys.exit(0)
