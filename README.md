# dcc-kit

dcckit is a module used to perform simple operations on objects in a 3D scene.

It is aimed to make the writings of python scripts and addons that edits/exports game assets a little easier.

The idea is that:

1- A specific object (subclassed from Dcc) performs operations for a software (like Blender, 3dsmax,whatever...)

2- A Dcc object has a Scene3d member and performs operations based on the data provided by the scene.

3- A Scene3d is an object that contains one or more Asset3d. Assets are organized in a tree-like structure.
This tree hierarchy is derived from the currently opened file in the dcc software.

4- An Asset3d is an object representing a game asset. It can be subclassed to different specific types.
For now only StaticMeshAsset3d exists. An Asset3d is composed by one or more Primitive3d

5- A Primitive3d is a basic 3D object (like a mesh, a bone...)

#An example of a scene hierarchy
```bash
.
└── Root
    ├── Asset1
    │   ├── Primitive1_1
    │   ├── Primitive1_2
    │   └── Primitive1_3
    └── #Comment1
        ├── _Group1
        │   ├── Asset2
        │   ├── Primitive2_1
        │   ├── Primitive2_2
        │   ├── @Tag1
        │   │   └── Asset3
        │   │       ├── Primitive3_1
        │   │       ├── Primitive3_2
        │   │       └── Primitive3_3
        │   └── Asset4
        │       └── Primitive4_1
        └── @Tag2
            └── _Group2
                ├── Asset5
                │   ├── Primitive5_1
                │   └── Primitive5_2
                └── Asset6
                    └── Primitive6_1
```

- An element with no specific prefix is an indipendent asset (like a table).
At export time, a subfolder with the same name can be created.
- hashtag character denotes a comment. Is a hierarchy element that doesn't affect export process in any way.
It is there just for artist's organization purposes.

- Underscore ( _ ) prefix indicates that the hierarchy element is a group of assets. At export time this means that
a folder with the group name can be created and it will contain the single exported asset files.
- @ prefix indicates that the element is a Tag. It's similar in some way to groups but it can't affect folder structure
at export time. Tag are just added to the names of all Groups and Assets under itself.

#How to implement a structure like this in a DCC: Blender
We use Blender's Collections.
Each collection is an element of the hierarchy and it's named accordingly (so with prefixes where needed).
Objects like meshes (the Primitives) are then placed under the collection that represent the Asset that contains them.

#Export
When exporting, some options can be used to control:
- scene_name_prefix: add the scene name as prefix to the exported file (ie scenename_assetname.fbx) and folder too
- use_tags : tags and group names are added to the exported file (ie tag_group_tag_assetname.fbx)
- create_subfolders: export each asset in a specific subfolder of the main provided export folder. The subfolder will have
the same name of the asset.
- subfolder_groups_only: in combination with create_subfolders, this will cause assets from the same group to be exported
inside a subfolder with the group name, instead of asset name.