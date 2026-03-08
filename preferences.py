#!/usr/bin/python3
# copyright (c) 2023 - DUBU JORDAN

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
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
from bpy.types import AddonPreferences
from bpy.props import StringProperty
from .__init__ import ADDON_NAME

class AddonPreferences(AddonPreferences):
    bl_idname = ADDON_NAME

    library_path: StringProperty(
        name="Library Path",
        subtype='DIR_PATH',
        default=os.path.join(os.path.dirname(__file__), "render_scenes")
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "library_path")
