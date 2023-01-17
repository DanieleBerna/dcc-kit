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
import datetime
import platform
from enum import Enum

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

"""
These constants define the special characters and words used in scene hierarchy.
Their main purpose is to define a role for an element of the hierarchy
"""
COMMENT_PREFIX = '#'  # Used just for organization purposes in the scene and it never affects assets naming
TAG_PREFIX = '@'  # Used for adding tags/words to the asset name. It never affects folder structure at export time
GROUP_PREFIX = '>'  # A Group is similar to a tag but Group name can be included in export folder structure
IGNORE = 'ignore'  # This is a special name used to exclude all its content from assets exporting
ROOT = "tree_root"  # Name given to the root node of built scene tree


class Primitive3dRoles(Enum):
    """Class - Enum for different usages of 3D Primitives"""
    MESH = 1
    COLLIDER = 2
    SOCKET = 3
    SKELETON = 4
    EMPTY = 5


class Primitive3d:
    """
    Base class for a generic Primitive in a 3D scene
    A Primitive3d could be any type of basic 3D primitive (a mesh, an empty object, a bone...)
    """

    def __init__(self, data, name="", role=Primitive3dRoles.EMPTY, vertex_count=0):
        """
        :param data: actual object data inside the DCC
        :keyword param name: (str) primitive name
        :keyword param role: (Primitive3dTypes) primitive role
        """
        self.data = data
        self.name = name
        self.role = role
        self.vertex_count = vertex_count

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

    def __init__(self, name="", display_name="", primitives=[], group="", tags=[], metadata={}):
        """
        :keyword param name: (str) assets name
        :keyword param primitives: (list) Primitives3d objects composing the asset
        :keyword param type: (Asset3dTypes) asset type
        :keyword group: (str) group to which the object belongs
        :keyword tags: (list) tags of the Asset
        :keyword metadata: (dict) asset metadata (NOT USED YET!!)
        """
        self.name = name  # Unique name
        self.display_name = display_name  # User friendly name
        self.primitives = primitives  # Primitives composing the asset
        self.group = group  # Optional asset group
        self.tags = tags  # Optional asset tags
        self.metadata = metadata  # Asset metadata
        self.vertex_count = self.query_vertex_count()

    def __repr__(self):
        output = f"\n\tAsset: {self.name}\n\tGroup: {self.group}\n"
        for prim in self.primitives:
            output = output + repr(prim)
        return output

    def query_primitives(self, types_list=None):
        """
        Return a list of asset's primitives, given their types or all if types list is not provided
        :param types_list: a list of Primitive3dRoles values
        :return:
        """
        if types_list is None:
            return self.primitives
        else:
            return [primitive for primitive in self.primitives if primitive.role in types_list]

    def query_vertex_count(self):
        count = 0
        for p in self.primitives:
            count = count + p.vertex_count
        return count

    def DELETEMEFROMHERE_compose_tagged_name(self):  # DEPRECATED
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

    def DELETEMEFROMHERE_compose_full_name(self, scene_name="", use_tags=True):
        """
        Build the full name for the asset, including any Tags and Group, to be used for export too
        :param scene_name:
        :param use_tags:
        :return:
        """
        # asset_name = self.name.split('.')[0]
        asset_name = self.display_name

        if use_tags:
            # tags = []
            tags = self.tags[:]
            try:
                group_index = self.tags.index(".")
                if self.group and self.group != "":
                    tags[group_index] = self.group
                else:
                    tags.pop(group_index)
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

    def __init__(self, name="", unique_name="", primitives=[], group="", tags=[], metadata={}):
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
        Asset3d.__init__(self, name, unique_name, primitives, group, tags, metadata)
        self.type = Asset3dTypes.STATIC_MESH
        self.meshes = self.query_primitives([Primitive3dRoles.MESH])
        self.colliders = self.query_primitives([Primitive3dRoles.COLLIDER])
        self.sockets = self.query_primitives([Primitive3dRoles.SOCKET])

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


class SkeletalMesh3d(Asset3d):
    """
    Extends Asset3d in order to better represent a StaticMesh.
    It is composed by one or more Primitive3d of mesh type
    and it could have some colliders and sockets
    """

    engine_prefix = "SKM_"

    def __init__(self, name="", unique_name="", primitives=[], group="", tags=[], metadata={}):
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
        Asset3d.__init__(self, name, unique_name, primitives, group, tags, metadata)
        self.type = Asset3dTypes.SKELETAL_MESH
        self.meshes = [primitive for primitive in self.primitives if primitive.role == Primitive3dRoles.MESH]
        self.bones = [primitive for primitive in self.primitives if primitive.role == Primitive3dRoles.SKELETON]
        self.sockets = [primitive for primitive in self.primitives if primitive.role == Primitive3dRoles.SOCKET]

    def __repr__(self):
        output = f"\n\tAsset: {self.name}\n\tType: {self.type}\n\tGroup: {self.group}\n"
        output = output + f"\n\tMeshes:\n"
        for mesh in self.meshes:
            output = output + repr(mesh)
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
        return f"SK_{super().compose_tagged_name()}"


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
    def __init__(self, name="", display_name="", type=SceneNodeTypes.COMMENT, children=[], data=[], parent=None):
        self.name = name
        self.display_name = display_name
        self.type = type
        self.children = children
        self.data = data
        self.parent = parent
        self.tags = []
        self.group = ""

    def __repr__(self):
        return self.name

    def print_node(self, indent=0):
        tabs = ""
        for i in range(indent):
            tabs = tabs + "\t"
        print(tabs+self.name)
        if self.children:
            for c in self.children:
                c.print_node(indent+1)

    def find_by_name(self, node_name):
        if self.name == node_name:
            return self
        else:
            if self.children:
                for c in self.children:
                    node = c.find(node_name)
                    if node:
                        return node
            else:
                return None

    def get_path(self, path=[]):
        if self.parent:
            path.append(self.parent)
            self.parent.get_path(path)
            return path
        else:
            return None

    def find_assets_with_labels(self, finds=[], use_ignore=True, use_tags=True):
        
        if (use_ignore and self.type == SceneNodeTypes.IGNORE) or self.type == SceneNodeTypes.RESERVED:  # return immediately if the 'ignore' element is found
            return assets, labels

        if self.type == SceneNodeTypes.ASSET and self.data.primitives:
            assets.append((self, labels))
            return assets, labels
        else:
            if self.type == SceneNodeTypes.GROUP:
                labels.append(self.display_name)
            elif self.type == SceneNodeTypes.TAG and use_tags:
                labels.append(self.display_name)
            for child in self.children:
                assets = child.find_assets_with_labels(assets=assets[:], labels=labels[:], use_ignore=use_ignore, use_tags=use_tags)
            return assets, labels


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

    def search_all_assets(self, node=None, assets=[], use_ignore=True, non_empty_only=True): # SOON DEPRECATED?
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

        if node.type == SceneNodeTypes.ASSET and node.data.primitives:
            assets.append(node.data)
            return assets
        else:
            for child in node.children:
                assets = self.search_all_assets(node=child, assets=assets[:])
            return assets

    def get_all_assets(self, use_ignore=True, use_tags=True):
        """
        Return a list of all valid Assets in the scene tree
        :keyword param node: (SceneNode) the tree node from where the recursive search must start
        :keyword param assets: (list) the assets list that needs to be filled during search
        :keyword param use_ignore: (bool) do not include 'ignore' branch in search
        """
        assets,self.tree.find_assets_with_labels(use_ignore=use_ignore, use_tags=use_tags)

    def search_asset_by_name(self, asset_name, node=None, use_ignore=True, visited_nodes=[], non_empty_only=True):
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

        if node.name == asset_name and node.type == SceneNodeTypes.ASSET and node.data.primitives:
            return node.data
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
            return [c.data for c in node.children if c.type == SceneNodeTypes.ASSET and node.data.primitives]
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

    @staticmethod
    def write_metadata_on_object(object, metadata_dict):
        return True


class Dcc:
    """Class for a generic DCC software"""

    def __init__(self):
        _scene_name = self.query_current_file_name()  # Get the currently opened scene name from scene file
        _scene_filepath = self.query_current_file_path()  # Get the currently opened scene filepath
        _scene_tree_root = self.query_current_scene_tree()   # Build the assets hierarchy from the scene
        print("SCENE TREE:")
        _scene_tree_root.print_node()
        self.scene = Scene3d(_scene_name, _scene_tree_root, _scene_filepath)  # Create and store a Scene3d object
        self.scene_file_type = ""  # Scene file extension

    @staticmethod
    def clean_name(name):
        """
        Clean name, removing any specific substring added by the DCC to avoid duplicates or reserved characters
        :param name:
        :return: (string) Unique name
        """

        raise NotImplementedError("'make_unique_collection_name()' method must be implemented in a child class"
                                  "\n\n*** Example: ***"
                                  "\ndef make_unique_name(name):"
                                  "\n\treturn name.split('.')[0]")

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

    def query_current_file_name(self):
        """ Override this in child class for specific DCCs"""
        return ""

    def query_current_file_path(self):
        """ Override this in child class for specific DCCs"""
        return ""

    def query_current_scene_tree(self):
        """ Override this in child class for specific DCCs"""
        raise NotImplementedError("'query_current_scene_tree()' method must be implemented in a Dcc child class"
                                  "\nand return the SceneNode object representing the scene hierarchy root")

    def _update_metadata(self):
        """
        Update metadata.
        :return: (dict)
        """
        artist_name = getpass.getuser()
        artist_machine = platform.node()
        timestamp = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        sourcefile = os.path.join(self.scene_filepath, self.scene_name)
        metadata = {"Artist": artist_name, "Machine": artist_machine, "Timestamp": timestamp, "RawFile": sourcefile}

        return metadata

    def _setup_export_asset_task(self, asset_name, file_name="", destination_folder="./", file_format="fbx", options={}):
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
                    print(f"esporto un asset: {asset_name} nel fine chiamato {file_name} con la cartella di gruppo")
                    print(f"Il suo group sarebbe: {asset_to_export.group}")
                    group_tags = self.scene.search_group_tags_by_name(asset_to_export.group)
                    print(f"I tag del gruppo sarebbero: {group_tags}")
                    tagged_group_name = "_".join(group_tags+[asset_to_export.group])
                    print(f"Il gruppo coi tag davanti sarebbe: {tagged_group_name}")
                    destination_folder = os.path.join(destination_folder, scene_prefix + tagged_group_name)
                    print(f"La cartella di export sarebbe: {destination_folder}")
                else:
                    destination_folder = os.path.join(destination_folder, scene_prefix + file_name)
            else:
                destination_folder = os.path.join(destination_folder, scene_prefix + file_name)

        if asset_to_export.type == Asset3dTypes.STATIC_MESH:
            engine_prefix = StaticMesh3d.engine_prefix
        elif asset_to_export.type == Asset3dTypes.SKELETAL_MESH:
            engine_prefix = SkeletalMesh3d.engine_prefix
        else:
            engine_prefix = ""

        full_path = os.path.join(destination_folder, engine_prefix+file_name + "." + file_format)
        if not os.path.exists(destination_folder):
            try:
                os.makedirs(destination_folder)
            except IOError:
                return False

        primitive_types = [Primitive3dRoles.MESH, Primitive3dRoles.SKELETON]
        if options['export_colliders']:
            primitive_types.append(Primitive3dRoles.COLLIDER)
        if options['export_sockets']:
            primitive_types.append(Primitive3dRoles.SOCKET)

        metadata = self._update_metadata()
        objects_to_export = [primitive.data for primitive in asset_to_export.query_primitives(primitive_types)]

        logging.info(f"Exporting {asset_to_export.name} with name {asset_name} in {destination_folder}")
        return objects_to_export, full_path, metadata

    def export_asset(self, asset_name, file_name="", destination_folder="./", file_format="fbx", options={}):
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

