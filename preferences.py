#!/usr/bin/python3
# copyright (c) 2023 - DUBU JORDAN

import os
import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty

# Get the top-level package name for bl_idname
_addon_package = __name__.rsplit('.', 1)[0] if '.' in __name__ else __name__

class EffortlessRendersPreferences(AddonPreferences):
    bl_idname = _addon_package

    library_path: StringProperty(
        name="Library Path",
        subtype='DIR_PATH',
        default=os.path.join(os.path.dirname(__file__), "render_scenes")
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "library_path")
