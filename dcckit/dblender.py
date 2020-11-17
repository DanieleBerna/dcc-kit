# -*- coding: utf-8 -*-

"""
dblender module contains the classes needed to represent a simple scene in Blender.
"""

import os
import re

import bpy

from . import dcore
from .dcore import DCC_ROOTS_LIST, DCC_RESERVED_LIST, ROOT, IGNORE, TAG_PREFIX, COMMENT_PREFIX, GROUP_PREFIX


class BlenderDcc(dcore.Dcc):
    """Extends Dcc class to handle a Blender scene """
    def __init__(self, context=None):
        if context is not None:
            self.context = context
        else:
            self.context = self.build_context()
        self.scene_file_type = "blend"
        super().__init__()

    @staticmethod
    def build_context():
        """
        Build a valid context for use of the class inside some external gui like PySide2.
        To be HEAVILY tested.
        For now, it just store the bpy context
        """
        return bpy.context

    def open_scene_file(self, filepath):
        if self._scene_file_exists(filepath):
            bpy.ops.wm.open_mainfile(filepath=filepath)
            return True
        else:
            return False

    def query_current_scene_name(self):
        return (bpy.path.basename(bpy.context.blend_data.filepath)).split('.')[0]

    def query_current_scene_filepath(self):
        return os.path.dirname(bpy.context.blend_data.filepath)

    def query_current_scene_tree(self):
        master_collection = self.context.scene.collection

        def recurse_scene_hierarchy(root, parent, group="", tags=[]):
            """
            root: current hierarchy level
            parent: parent of current collection
            group: group detected from previous iteration
            group: tags list detected from previous iterations
            """
            scene_node = dcore.SceneNode()
            scene_node.children = []
            scene_node.parent = parent
            if tags:
                scene_node.tags = tags[:]

            if root.name.rstrip() in DCC_ROOTS_LIST:
                scene_node.type = dcore.SceneNodeTypes.ROOT
                scene_node.name = ROOT
            elif root.name.lower() in DCC_RESERVED_LIST:
                scene_node.type = dcore.SceneNodeTypes.RESERVED
                scene_node.name = "-reserved-"
            elif root.name.lower() == IGNORE:
                scene_node.type = dcore.SceneNodeTypes.IGNORE
                scene_node.name = IGNORE
            elif root.name[0] == TAG_PREFIX:
                scene_node.type = dcore.SceneNodeTypes.TAG
                scene_node.name = root.name[1:]
                tags.append(scene_node.name)
            elif root.name[0] == COMMENT_PREFIX:
                scene_node.type = dcore.SceneNodeTypes.COMMENT
                scene_node.name = root.name[1:]
            elif root.name[0] == GROUP_PREFIX:
                scene_node.type = dcore.SceneNodeTypes.GROUP
                scene_node.name = root.name[1:]
                group = scene_node.name
                tags.append(".")
            else:
                scene_node.type = dcore.SceneNodeTypes.ASSET
                scene_node.name = root.name

                temp_primitives = []
                for obj in root.all_objects.items():
                    if not isinstance(obj, bpy.types.Collection) and obj[1].type in ("EMPTY", "MESH"):
                        is_valid = False
                        prim_data = obj[1]
                        prim_name = prim_data.name
                        socket_naming_pattern = re.compile("^SOCKET_.*")
                        collider_naming_pattern = re.compile("^UCX_.*_\d\d$")
                        if prim_data.type == "EMPTY" and bool(socket_naming_pattern.match(prim_name)):
                            primitive_type = dcore.Primitive3dRoles.SOCKET
                            is_valid = True
                        elif prim_data.type == "MESH" and bool(collider_naming_pattern.match(prim_name)):
                            primitive_type = dcore.Primitive3dRoles.COLLIDER
                            is_valid = True
                        elif prim_data.type == "MESH":
                            primitive_type = dcore.Primitive3dRoles.MESH
                            is_valid = True

                        if is_valid:
                            temp_primitives.append(dcore.Primitive3d(obj[1], prim_name, primitive_type))
                scene_node.content = dcore.StaticMesh3d(name=scene_node.name, type=dcore.Asset3dTypes.STATIC_MESH,
                                                        group=group, tags=tags, primitives=temp_primitives)

            if root.children:
                for child in root.children:
                    scene_node.children.append(recurse_scene_hierarchy(child, scene_node, group, tags[:]))

            print(f"Scene node: {scene_node.name}, tags: {scene_node.tags}")
            return scene_node

        tree_root = recurse_scene_hierarchy(master_collection, None)
        print(f"Scene tree built: root is {tree_root}")
        return tree_root

    def export_asset(self, asset_name, destination_folder="./", file_format="FBX", options={}):
        objects_to_export, full_path = self._setup_export_asset_task(asset_name, destination_folder=destination_folder,
                                                            file_format=file_format, options=options)

        # This line is needed to remove any unwanted '.[0-9][0-9][0-9]' string present in asset name due to Blender handling of duplicated collections name
        full_path = os.path.join((os.path.dirname(full_path)), os.path.splitext(os.path.basename(full_path))[0].split('.')[0]+os.path.splitext(os.path.basename(full_path))[1])
        if objects_to_export:
            override_context = self.context.copy()
            """for obj in objects_to_export:
                if metadata:
                    for key in metadata.keys():
                        obj[key] = metadata[key]"""

            override_context['selected_objects'] = objects_to_export

            bpy.ops.export_scene.fbx(override_context, filepath=full_path,
                                     path_mode='RELATIVE',
                                     use_selection=True,
                                     axis_forward='Y',
                                     axis_up='Z',
                                     filter_glob='*.fbx',
                                     bake_space_transform=True,
                                     use_mesh_modifiers=True,
                                     mesh_smooth_type='OFF',
                                     use_mesh_edges=False,
                                     use_tspace=False,
                                     use_custom_props=True,
                                     bake_anim=False,
                                     use_metadata=True)


if __name__ == "__main__":
    print("\n\n*********** BlenderDCC Test ***********")
    print("\nTest 0 - Create a BlenderDCC and build scene tree: ")
    bl = BlenderDcc()

    print("\nTest 1 - Show all assets names: ")
    scene_assets = bl.scene.search_all_assets()
    for asset in scene_assets:
        print(asset.name)

    print("\nTest 2 - Compose and show full names for all assets: ")
    for asset in scene_assets:
        print(asset.compose_tagged_name())

    print("\nTest 3 - Search an asset given its name ('01'): ")
    target_asset = bl.scene.search_asset_by_name("01")
    if target_asset is not None:
        print(target_asset.name)

    print("\nTest 4 - Show all groups names: ")
    scene_groups = bl.scene.search_all_groups()
    print(scene_groups)

    print("\nTest 5 - Search all asset that belongs to a given group ('Set1'): ")
    target_assets = bl.scene.search_assets_by_group("Set1")
    for asset in target_assets:
        print(asset.name)

    print("\nTest 6 - Export a given asset ('Asset1'): ")
    options = {'scene_name_prefix': False, "use_tags": False, 'create_subfolders': True, 'subfolder_groups_only': True,
               'export_colliders': True, 'export_sockets': True}
    for asset in scene_assets:
        bl.export_asset(asset.name, destination_folder="C:\\TestExport", options=options)
