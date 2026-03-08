#!/usr/bin/python3
# copyright (c) 2023 - DUBU JORDAN

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


import os
import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty

bl_info = {
    "name": "Effortless Renders",
    "description": "Create renders, generate description",
    "author": "Jordan Dubu - Doyorn",
    "version": (1, 1, 1),
    "blender": (5, 0, 1),
    "location": "View3D > Tool Shelf > Turbosquid Tab",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

class EffortlessRendersPreferences(AddonPreferences):
    bl_idname = __name__

    library_path: StringProperty(
        name="Library Path",
        subtype='DIR_PATH',
        default=os.path.join(os.path.dirname(__file__), "render_scenes")
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "library_path")

from . import properties

def register():
    bpy.utils.register_class(EffortlessRendersPreferences)
    properties.register()

def unregister():
    properties.unregister()
    bpy.utils.unregister_class(EffortlessRendersPreferences)

if __name__ == "__main__":
    register()
