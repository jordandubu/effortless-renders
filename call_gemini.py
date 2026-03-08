import os
import sys
from google import genai

try:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    
    version = "5.0.1"
    error_log = """=== LINT OUTPUT ===
All checks passed!

=== TEST OUTPUT ===
============================================================
Effortless Renders — Addon Compatibility Test
============================================================
── Testing bl_info ──
  bl_info = {'name': '3D Market Exporter', 'description': 'Create renders, generate description', 'author': 'Jordan Dubu - Doyorn', 'version': (1, 1), 'blender': (4, 0, 0), 'location': 'View3D > Tool Shelf > Turbosquid Tab', 'warning': '', 'wiki_url': '', 'tracker_url': '', 'category': 'Development'}
  ✅ bl_info validation passed

── Testing syntax ──
  ✅ properties.py
  ✅ main.py
  ✅ preferences.py
  ✅ operators.py
  ✅ utils.py
  ✅ __init__.py
  ✅ panels.py

── Testing register/unregister ──
  Calling register()...
  ✅ register() succeeded
  Verifying operators...
    ✅ object.rendering_operator is registered
    ✅ object.test_connection is registered
    ✅ scene.import_scene is registered
    ✅ object.import_helper_box is registered
    ✅ object.open_library_path is registered
  Calling unregister()...
  ✅ unregister() succeeded

============================================================
✅ ALL TESTS PASSED
============================================================

=== VERSION ERROR ===
Addon is compatible, but bl_info needs update to: 5.0.1"""
    migration = """<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
</body></html>"""
    
    with open("all_source.txt", "r") as f:
        source = f.read()

    prompt = f"""You are a Blender addon maintenance bot. A Blender addon has broken on a new Blender version or needs a metadata update. Your job is to fix the Python code so it works with the new version and update the blender version in bl_info.

    IMPORTANT RULES:
    - Only fix what is broken. Do not refactor or change working code.
    - Maintain backward compatibility where possible.
    - Update the 'blender' key in bl_info in __init__.py to match the new version if it is higher than the current one.
    - Increment the 'version' tuple in bl_info (e.g., (1, 1) -> (1, 1, 1)) to reflect this update.
    - Output ONLY the fixed file contents in this exact format for EACH file that needs changes:

    --- FILE: filename.py ---
    <full file content>
    --- END FILE ---

    If no fix is needed for a file, do not include it.
    Do NOT include any explanation, markdown, or commentary — ONLY the file blocks above.

    ## Blender version
    {version}

    ## Error log
    {error_log[:4000]}

    ## Current source code
    {source[:20000]}

    ## Blender migration notes (if available)
    {migration[:4000]}"""

    # Using gemini-3.1-pro-preview as identified from diagnostics
    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents=prompt
    )
    
    with open("gemini_output.txt", "w") as f:
        f.write(response.text)
    print("✅ Gemini response received")
except Exception as e:
    print(f"❌ Error calling Gemini: {e}", file=sys.stderr)
    sys.exit(1)
