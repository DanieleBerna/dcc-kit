# dcc-kit
## (updated)
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
- **dblender.py** : contains a child class of Dcc, implementing Blender specific methods

## Key concepts

- A specific object (subclassed from **Dcc**) performs operations for a software (like Blender, 3dsmax,whatever...)

- Some methods (example: open_scene_file() )share a common base of code (example: check for file existence): in these cases the common code is part of a "private" Dcc class
method (marked with "\_"), and the public method is defined abstract in base class, forcing a proper implementation in child class. 

- A Dcc object has a **Scene3d member** and performs operations based on the data provided by the scene.

- A Scene3d is an object that **contains one or more Asset3d**. Assets are organized in a **tree-like structure**.
This tree hierarchy is derived from the currently opened file in the dcc software.

- An Asset3d represents a game asset. It can or not be a single, complete object (like a chair), a part of a composed object (like the hood of a specific car) or a graphic variation of an object.
It can be subclassed to different specific types.
For now only **StaticMeshAsset3d** exists. An Asset3d is composed by one or more **Primitive3d**

- A Primitive3d is a basic 3D object (like a mesh, a bone...)

## Scene hierarchy and naming conventions

The software scene needs to have a specific hierarchy.
Each DCC has its own way to achieve this: since I only wrote the working class for Blender, I decided to use Blender's **collections** to organize the scene.
3dsmax for example could do the same using **layers**.
From now on, let's call these hierarchy objects as **nodes** (like tree nodes...)

- Node names without any reserved character as prefix in name represent Assets
- Node names starting with *_* represent **Groups** (see before assets parts of a composed object: these nodes actually are the object)
- Node names starting with *#* represent **Comments**: they're used just for organization purposes in the scene and they never affect assets naming or folders
- Node names starting with *@* represent **Tags**: they're used for adding tags/words to the asset name. They never affects folder structure at export time
- *ignore* named node identifies a hierarchy branch that won't be considered during assets listing or export.

### Scene example

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

## Export requirements and options

When exporting, some options can be used to control:
- *'scene_name_prefix'* add the scene name as prefix to the exported file (ie scenename_assetname.fbx) and folder too.
- *'use_tags'* tags and group names are added to the exported file (ie tag_group_tag_assetname.fbx).
- *'create_subfolders'* makes each asset to be exported into a specific subfolder of the given export folder. Subfolder name have to refer to the object (so it's equal to the asset name, minus any engine specific prefix like SM_ for unreal static meshes)
- *'subfolder_groups_only'*, in combination with 'create_subfolder', makes all assets from the same group exported inside a common subfolder, named as the Group (and not as the asset)

