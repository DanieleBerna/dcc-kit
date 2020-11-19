# -*- coding: utf-8 -*-

"""
dcore module contains all classes needed to represent a simple scene in a generic DCC software.
Here there are no references to any specific software.
Primitives, Assets and Scenes aren't related to any specific software.
Dcc class has basic methods and attributes: for specific software the class needs to be extended (see dblender module)
"""

import os
import getpass
import logging
from datetime import datetime
from enum import Enum

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

"""
These constants define the special characters and words used in scene hierarchy.
Their main purpose is to define a role for an element of the hierarchy
"""
COMMENT_PREFIX = '#'  # Used just for organization purposes in the scene and it never affects assets naming
TAG_PREFIX = '@'  # Used for adding tags/words to the asset name. It never affects folder structure at export time
GROUP_PREFIX = '_'  # A Group is similar to a tag but Group name can be included in export folder structure
IGNORE = 'ignore'  # This is a special name used to exclude all its content from assets exporting
ROOT = "root"  # Name given to the root node of built scene tree
DCC_ROOTS_LIST = ('Master Collection',)  # list of names used by DCCs to call the root element in a scene hierarchy
DCC_RESERVED_LIST = ('cutters',)  # list of reserved names used by DCCs for hierarchy elements that shouldn't be considered


class Primitive3dRoles(Enum):
    """Class - Enum for different usages of 3D Primitives"""
    MESH = 1
    COLLIDER = 2
    SOCKET = 3
    BONE = 4
    EMPTY = 5


class Primitive3d:
    """
    Base class for a generic Primitive in a 3D scene
    A Primitive3d could be any type of basic 3D primitive (a mesh, an empty object, a bone...)
    """

    def __init__(self, data, name="", role=Primitive3dRoles.EMPTY):
        """
        :param data: actual object data inside the DCC
        :keyword param name: (str) primitive name
        :keyword param role: (Primitive3dTypes) primitive role
        """
        self.data = data
        self.name = name
        self.role = role

    def __repr__(self):
        return f"\n\t\tPrimitive: {self.name} ({self.role})\n"


class Asset3dTypes(Enum):
    """Class - Enum for different types of 3D Asset"""
    STATIC_MESH = 1
    SKELETAL_MESH = 2
    ANIMATION = 3


class Asset3d:
    """
    Base class for a generic 3D Asset.
    An Asset3D is composed by one or more Primitive3d
    """

    def __init__(self, name="", primitives=[], type=Asset3dTypes.STATIC_MESH, group="", tags=[], metadata={}):
        """
        :keyword param name: (str) assets name
        :keyword param primitives: (list) Primitives3d objects composing the asset
        :keyword param type: (Asset3dTypes) asset type
        :keyword group: (str) group to which the object belongs
        :keyword tags: (list) tags of the Asset
        :keyword metadata: (dict) asset metadata (NOT USED YET!!)
        """
        self.name = name
        self.primitives = primitives
        self.type = type
        self.group = group
        self.tags = tags
        self.metadata = metadata

    def __repr__(self):
        output = f"\n\tAsset: {self.name}\n\tType: {self.type}\n\tGroup: {self.group}\n"
        for prim in self.primitives:
            output = output + repr(prim)
        return output

    def compose_tagged_name(self):  # DEPRECATED
        """ Build the name of the assets with tags and groups """
        tags = []
        asset_name = self.name.split('.')[0]
        try:
            tags = self.tags[:]
            group_index = self.tags.index(".")
            tags[group_index] = self.group
        except ValueError:
            pass
        if tags:
            tags.append("")
        tagged_name = "_".join(tags) + asset_name
        return tagged_name

    def compose_full_name(self, scene_name="", use_tags=True):
        """
        Build full name for the file that must be exported
        :param scene_name:
        :param use_tags:
        :return:
        """
        asset_name = self.name.split('.')[0]

        if use_tags:
            tags = []
            try:
                tags = self.tags[:]
                group_index = self.tags.index(".")
                tags[group_index] = self.group
            except ValueError:
                pass
            if tags:
                tags.append("")
            asset_name = "_".join(tags) + asset_name

        else:
            if self.group:
                asset_name = f"{self.group}_{asset_name}"  # add Set group

        if scene_name:
            asset_name = f"{scene_name}_{asset_name}"

        return asset_name


class StaticMesh3d(Asset3d):
    """
    Extends Asset3d in order to better represent a StaticMesh.
    It is composed by one or more Primitive3d of mesh type
    and it could have some colliders and sockets
    """

    engine_prefix = "SM_"

    def __init__(self, name="", primitives=[], type=Asset3dTypes.STATIC_MESH, group="", tags=[], metadata={}):
        """
        Overrides super method.
        There are 3 different primitive lists for meshes, colliders and socket
        :keyword param name: (str) assets name
        :keyword param primitives: (list) Primitives3d objects composing the asset
        :keyword param type: (Asset3dTypes) asset type
        :keyword group: (str) group to which the object belongs
        :keyword tags: (list) tags of the Asset
        :keyword metadata: (dict) asset metadata  (NOT USED YET!!)
        """
        Asset3d.__init__(self, name, primitives, type, group, tags, metadata)
        self.meshes = [primitive for primitive in self.primitives if primitive.role == Primitive3dRoles.MESH]
        self.colliders = [primitive for primitive in self.primitives if primitive.role == Primitive3dRoles.COLLIDER]
        self.sockets = [primitive for primitive in self.primitives if primitive.role == Primitive3dRoles.SOCKET]

    def __repr__(self):
        output = f"\n\tAsset: {self.name}\n\tType: {self.type}\n\tGroup: {self.group}\n"
        output = output + f"\n\tMeshes:\n"
        for mesh in self.meshes:
            output = output + repr(mesh)
        output = output + f"\n\tColliders:\n"
        for collider in self.colliders:
            output = output + repr(collider)
        output = output + f"\n\tSockets:\n"
        for socket in self.sockets:
            output = output + repr(socket)
        return output

    def compose_tagged_name(self):  # DEPRECATED
        """
        Overrides super method.
        Build full name for the file that must be exported, adding StaticMesh prefix (Unreal Engine style)
        to the full name.
        """
        return f"SM_{super().compose_tagged_name()}"


class SceneNodeTypes(Enum):
    """Class - Enum for different types of Scene Nodes"""
    ROOT = 0  # hierarchy root
    IGNORE = 1  # ignore branch
    COMMENT = 2  # node used just for comment and organization purposes
    GROUP = 3  # node representing an assets group
    ASSET = 4  # node containing an asset
    TAG = 5  # Tag node
    RESERVED = 6  # Reserved by DCC


class SceneNode:
    """
        A SceneNode is the basic element of a Scene hierarchy
    """
    def __init__(self, name="", type=SceneNodeTypes.COMMENT, children=[], content=[], parent=None):
        self.name = name
        self.type = type
        self.children = children
        self.content = content
        self.parent = parent
        self.tags = []
        self.group = ""


class Scene3d:
    """
    Class for a generic Scene of a DCC software
    It contains one or more Asset3d
    """

    def __init__(self, name="", root_node=None, filepath="./"):
        self.name = name
        if root_node:
            self.tree = root_node
        else:
            self.tree = SceneNode()
        self.filepath = filepath

    def __repr__(self):
        output = f"Scene: {self.name}\nType: {self.type}\n"
        for asset in self.assets:
            output = output + repr(asset)
        return output

    def search_all_assets(self, node=None, assets=[], use_ignore=True, non_empty_only=True):
        """
        Return a list of all valid Assets in the scene tree
        :keyword param node: (SceneNode) the tree node from where the recursive search must start
        :keyword param assets: (list) the assets list that needs to be filled during search
        :keyword param use_ignore: (bool) do not include 'ignore' branch in search
        """
        if node is None:
            node = self.tree

        if (use_ignore and node.type == SceneNodeTypes.IGNORE) or node.type == SceneNodeTypes.RESERVED:  # return immediately if the 'ignore' element is found
            return assets

        if node.type == SceneNodeTypes.ASSET and node.content.primitives:
            assets.append(node.content)
            return assets
        else:
            for child in node.children:
                assets = self.search_all_assets(node=child, assets=assets[:])
            return assets

    def search_asset_by_name(self, asset_name, node=None, use_ignore=True, non_empty_only=True):
        """
        Search and return an Assets given its name from the scene tree
        :param asset_name: (str) the name of the asset that must be searched
        :param node: (SceneNode) the tree node from where the recursive search must start
        :param use_ignore: (bool) do not include 'ignore' branch in search
        """
        if node is None:
            node = self.tree

        if (use_ignore and node.type == SceneNodeTypes.IGNORE) or node.type == SceneNodeTypes.RESERVED:  # return immediately if the 'ignore' element is found
            return

        if node.name == asset_name and node.type == SceneNodeTypes.ASSET and node.content.primitives:
            return node.content
        else:
            asset = None
            for child in node.children:
                asset = self.search_asset_by_name(asset_name, node=child)
                if asset is not None:
                    return asset

    def search_assets_by_group(self, group_name, node=None, non_empty_only=True):
        """
        Search and return Assets given that belongs to a given group
        :param group_name: (str) the name of the group that must be used for assets search
        :param node: (SceneNode) the tree node from where the recursive search must start
        """
        if node is None:
            node = self.tree
        if node.name == group_name and node.type == SceneNodeTypes.GROUP:
            return [c.content for c in node.children if c.type == SceneNodeTypes.ASSET and node.content.primitives]
        else:
            assets = None
            for child in node.children:
                assets = self.search_assets_by_group(group_name, node=child)
                if assets:
                    return assets

    def search_all_groups(self, node=None, groups=[], use_ignore=True):
        """
        Return a list of all Group names from the scene tree
        :keyword param node: (SceneNode) the tree node from where the recursive search must start
        :keyword param groups: (list) the groups list that needs to be filled during search
        :keyword param use_ignore: (bool) do not include 'ignore' branch in search
        """
        if node is None:
            node = self.tree

        if (use_ignore and node.type == SceneNodeTypes.IGNORE) or node.type == SceneNodeTypes.RESERVED:  # return immediately if the 'ignore' element is found
            return groups

        if node.type == SceneNodeTypes.GROUP:
            groups.append(node.name)
            return groups
        else:
            for child in node.children:
                groups = self.search_all_groups(node=child, groups=groups[:])
            return groups

    def search_group_tags_by_name(self, group_name, node=None, use_ignore=True):
        """
        Search and return a Group given its name from the scene tree
        :param group_name: (str) the name of the group that must be searched
        :keyword param node: (SceneNode) the tree node from where the recursive search must start
        :keyword param use_ignore: (bool) do not include 'ignore' branch in search
        """
        if node is None:
            node = self.tree

        if (use_ignore and node.type == SceneNodeTypes.IGNORE) or node.type == SceneNodeTypes.RESERVED:  # return immediately if the 'ignore' element is found
            return

        if node.name == group_name and node.type == SceneNodeTypes.GROUP:
            return node.tags
        else:
            tags = None
            for child in node.children:
                tags = self.search_group_tags_by_name(group_name, node=child)
                if tags is not None:
                    return tags

    def freeze_metadata(self):
        return {"work_file": os.path.join(self.folder, self.name) + ".blend", "artist": getpass.getuser(),
                "last_modified_date": datetime.now().strftime("%H:%M")}

    def write_metadata_on_object(self, object, metadata_dict):
        return True


class Dcc:
    """Class for a generic DCC software"""

    def __init__(self):
        self.scene_name = self.query_current_scene_name()  # Get the currently opened scene name from scene file
        self.scene_filepath = self.query_current_scene_filepath()  # Get the currently opened scene filepath
        self.scene_tree_root = self.query_current_scene_tree()   # Build the assets hierarchy from the scene
        self.scene = Scene3d(self.scene_name, self.scene_tree_root, self.scene_filepath)  # Create and store a Scene3d object
        self.scene_file_type = ""  # Scene file extension

    def _scene_file_exists(self, filepath):
        """
        Check for given scene file existence
        :param filepath:
        :return: (bool)
        """

        if os.path.splitext(filepath)[1] != self.scene_file_type:
            logging.warning(f"Wrong file extension\n"
                            f"got: {os.path.splitext(filepath)[1]}\n"
                            f"expected: {self.scene_file_type}")
            return False
        elif not os.path.exists(filepath):
            logging.warning(f"Scene file {filepath} doesn't exists")
            return False
        else:
            return True

    def open_scene_file(self, filepath):
        """
        Try to open a new scene from file.
        :param filepath:
        :return: (bool)
        """

        raise NotImplementedError("'open_scene_file()' method must be implemented in a child class"
                                  "\nand use self._scene_file_exists(filepath)"
                                  "\n\n*** Example: ***"
                                  "\ndef open_scene_file(self, filepath):\n"
                                  "\tif self._scene_file_exists(filepath):\n"
                                  "\t\t  # Use specific dcc's api to open the file")

    def query_current_scene_name(self):
        """ Override this in child class for specific DCCs"""
        return ""

    def query_current_scene_filepath(self):
        """ Override this in child class for specific DCCs"""
        return ""

    def query_current_scene_tree(self):
        """ Override this in child class for specific DCCs"""
        return SceneNode()

    def _setup_export_asset_task(self, asset_name, file_name="", destination_folder="./", file_format="FBX", options={}):
        """
        Override this in child class for specific DCCs
        It export a given asset from the scene to a file
        :param asset_name: (str)
        :param destination_folder: (str)
        :param file_format: (str)
        :param options: (dict) export options: 'scene_name_prefix', 'use_tags', 'create_subfolders', 'subfolder_groups_only'
        :return: (bool)
        """
        asset_to_export = self.scene.search_asset_by_name(asset_name)  # Get the desired asset from the Scene
        if asset_to_export is None:
            logging.warning(f"Asset is invalid or doesn't exist: {asset_name}")
            return False

        """ Compose full name for the file that must be exported, depending on options """
        if not file_name:  # if a file name is provided, skip name creation based on options
            if options['use_tags']:
                asset_name = asset_to_export.compose_tagged_name()
            else:
                asset_name = f"{asset_to_export.group}_{asset_to_export.name}"
            if options['scene_name_prefix']:
                asset_name = f"{self.scene.name}_{asset_name}"

        """ Compose export path """
        if options['scene_name_prefix']:
            scene_prefix = f"{self.scene.name}_"
        else:
            scene_prefix = ""
        if options['create_subfolders']:
            if options['subfolder_groups_only']:
                if asset_to_export.group:
                    group_tags = self.scene.search_group_tags_by_name(asset_to_export.group)
                    tagged_group_name = "_".join(group_tags+[asset_to_export.group])
                    destination_folder = os.path.join(destination_folder, scene_prefix + tagged_group_name)
                else:
                    destination_folder = os.path.join(destination_folder, scene_prefix + file_name)
            else:
                destination_folder = os.path.join(destination_folder, scene_prefix + file_name)

        if asset_to_export.type == Asset3dTypes.STATIC_MESH:
            engine_prefix = StaticMesh3d.engine_prefix
        else:
            engine_prefix = ""

        full_path = os.path.join(destination_folder, engine_prefix+file_name + "." + file_format)
        if not os.path.exists(destination_folder):
            try:
                os.makedirs(destination_folder)
            except IOError:
                return False

        if asset_to_export.type == Asset3dTypes.STATIC_MESH:
            meshes_to_export = [mesh.data for mesh in asset_to_export.meshes]
            if options['export_colliders']:
                colliders_to_export = [collider.data for collider in asset_to_export.colliders]
            if options['export_sockets']:
                sockets_to_export = [socket.data for socket in asset_to_export.sockets]
            objects_to_export = meshes_to_export + colliders_to_export + sockets_to_export

        logging.info(f"Exporting {asset_to_export.name} with name {asset_name} in {destination_folder}")
        return objects_to_export, full_path

    def export_asset(self, asset_name, file_name="", destination_folder="./", file_format="FBX", options={}):
        raise NotImplementedError("'export_asset()' method must be implemented in a Dcc child class"
                                  "\nand s call to '_setup_export_asset_task()' must be included."
                                  "\n\n*** Example: ***"
                                  "\ndef export_asset(self, asset_name, destination_folder='./', file_format='ext', options={}):"
                                  "\n\tobjects_to_export, full_path = self._setup_export_asset_task(asset_name, destination_folder, file_format, options)"
                                  "\n\t  # for object in objects_to_export -> export object to full_path")


if __name__ == "__main__":
    logging.debug("\n*********** DCC Test ***********")
    logging.debug("\nTest 0 - Create a DCC and build a scene tree: ")
    try:
        dcc = Dcc()
        logging.debug(f"Dcc object created: {dcc}")
    except Exception as e:
        logging.warning(f"An error has occurred!\n\n{e}")
    logging.debug("\nTest 1 - Try to export asset without implementing the abstract method export_asset(): ")
    dcc.export_asset("raise_a_NotImplementedError!")

