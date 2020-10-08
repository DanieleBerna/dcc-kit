# dcc-kit

**dcckit is a module used to help writing pipeline scripts for 3D DCC softwares.**

Its aim is to make the writings of python scripts and addons that edits/exports game assets a little easier...

## Introduction
### My problem (and motivation)

I wrote some rough Blender addons for speed up game asset creation and streamline a little our internal process at our (small) company.
When working on a custom exporter I found myself constantly redesigning things and adding features and so on, most of the times after some talks with 3D artists.
So I told myself that I could try to write some *basic framework* that I could reuse for multiple addons.
For example, _exporter_ script requires a organization of the 3D scene, so precise naming... What if I'll decide to also write some *wizard* for setup the scene in the proper way? the 2 addons would share part of the code, probably.
So I reworked my exporter again, stripping and refactoring the pure *code part*, leaving any UI out of play.

While doing this, I also thought that it could be nice to make it working (for the most part) regardless of the specific DCC used: what if I would like to wrote the same addon in 3dsmax too? (since we still use it).

### My solution
So I wrote a bunch of classes (**Primitive3d**, **Asset3d**, **Scene3d** and **Dcc**) and put most of the logic there, inside the dcore.py file.
While Primitive3d, Asset3d and Scene3d classes are completely *software agnostic*, the idea is that one can subclass the Dcc class and override its methods (or add new ones) to perform operations in a specific DCC.
(*for example, the core part of the export asset function is in the parent class Dcc, the BlenderDcc subclass just add the part that really export the files using Blender Python API*)

### Why all these classes?
*I'm not a programmer*.
I used to be a little, like 12 years ago, but I fully switched to an art path.
However past is still there and I turned to tech-art. And good tech-art requires some good scripting/coding skill.
So I decided to use this small package both for production purposes and learning ones: I tried to think about the best solutions and revamped my coding knowledge.
I know that **object-oriented programming** is not always needed, and maybe I overcomplicated stuff, but I like it and tried to write this in the cleanest way I could.
Plus, I tried to learn more about coding style, good habits and so on.

## What's inside
- **dcore.py**: contains all the base classes representing 3D primitives, assets, scene and a generic DCC.
- **blender.py** : contains a child class of Dcc, implementing Blender specific methods

## Key concepts

- A specific object (subclassed from **Dcc**) performs operations for a software (like Blender, 3dsmax,whatever...)

- A Dcc object has a **Scene3d member** and performs operations based on the data provided by the scene.

- A Scene3d is an object that **contains one or more Asset3d**. Assets are organized in a **tree-like structure**.
This tree hierarchy is derived from the currently opened file in the dcc software.

- An Asset3d represents a game asset. It can or not be a single, complete object (like a chair), a part of a composed object (like the hood of a specific car) or a graphic variation of an object.
It can be subclassed to different specific types.
For now only **StaticMeshAsset3d** exists. An Asset3d is composed by one or more **Primitive3d**

- A Primitive3d is a basic 3D object (like a mesh, a bone...)

### Example of a scene
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
