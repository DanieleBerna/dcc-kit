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

```bash
.
└── Root
    ├── Asset1
    │   ├── Primitive1_1
    │   ├── Primitive1_2
    │   └── Primitive1_3
    └── #Comment1
        ├── _Set1
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
            └── _Set2
                ├── Asset5
                │   ├── Primitive5_1
                │   └── Primitive5_2
                └── Asset6
                    └── Primitive6_1
```