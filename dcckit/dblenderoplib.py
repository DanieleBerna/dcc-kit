import bpy


def duplicate_object(obj):
    """
    :param obj: the object to be duplicated
    :return: the new object or None
    """
    try:
        new_obj = obj.copy()
        new_obj.data = obj.data.copy()
        new_obj.animation_data_clear()
        bpy.context.collection.objects.link(new_obj)
        return new_obj
    except Exception as e:
        print(e)
        return None


def duplicate_object_by_name(obj_name, new_obj_name=""):
    """

    :param obj_name: the nae of the object to be duplicated
    :param new_obj_name: optional - the name of the new object
    :return:
    """
    obj = bpy.data.objects[obj_name]
    new_obj = duplicate_object(obj)
    if new_obj is not None:
        if new_obj_name:
            new_obj.name = new_obj_name
    return new_obj


def set_scene_units_for_rigging(scale=0.01):
    """
    Set scene units and grid for compatibility wit Unreal Engine 4 for skeletal meshes
    :param scale:
    :return:
    """
    bpy.data.scenes['Scene'].unit_settings.system = 'METRIC'
    bpy.data.scenes['Scene'].unit_settings.scale_length = scale
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.overlay.grid_scale = scale
                    break


def import_ue4_mannequin(filepath="C:\Works\City20\Raw\Developers\danielebernardini\CharacterPrototype\Mannequin.fbx"):
    bpy.ops.object.mode_set(mode='OBJECT')
    mannequin_collection = bpy.data.collections.new(EXPORT_COLLECTION)
    bpy.context.scene.collection.children.link(mannequin_collection)
    layer_collection = bpy.context.view_layer.layer_collection.children[mannequin_collection.name]
    bpy.context.view_layer.active_layer_collection = layer_collection

    try:
        bpy.ops.import_scene.fbx(filepath=filepath, use_anim=False)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Mannequin'].select_set(True)
        bpy.data.objects['Mannequin.001'].select_set(True)
        bpy.ops.object.delete()
        return True
    except Exception as e:
        print(e)
        return False


def parent_to_armature(obj, armature_name):
    try:
        bpy.ops.object.mode_set(mode='OBJECT')
    except:
        pass
    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)
    bpy.ops.object.parent_clear(type='CLEAR')

    armature = bpy.data.objects[armature_name]
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.parent_set(type='ARMATURE_NAME')


def remove_all_modifiers_by_type(obj, mod_type="ARMATURE"):
    mods = [mod for mod in obj.modifiers if mod.type == mod_type]
    if mods:
        for i in range(len(mods)):
            obj.modifiers.remove(mods[i])


def dump_armature_transforms(armature, filename="D:\\matrix_file.json"):
    transforms = {}
    for source_bone in armature.pose.bones:
        rows = []
        for i in range(4):
            rows.append((source_bone.matrix.row[i][0], source_bone.matrix.row[i][1], source_bone.matrix.row[i][2],
                         source_bone.matrix.row[i][3]))
        transforms[source_bone.name] = rows
    try:
        matrix_file = open(filename, 'w')
        json.dump(transforms, matrix_file)
        matrix_file.close()
        return True
    except IOError:
        return False


def pose_armature_from_file(armature, filename="D:\\matrix_file.json"):
    try:
        matrix_file = open(filename)
        transforms = json.load(matrix_file)
        matrix_file.close()
    except IOError:
        return False
    for bone in armature.pose.bones:
        bone.matrix = Matrix(transforms[bone.name])
        bpy.context.view_layer.update()
    return True


def snap_armature_bones(source_armature_name, target_armature_name):
    """
    Snap all bones of source armature co the position of corresponding bones of
    target armature
    """
    try:
        bpy.ops.object.mode_set(mode='OBJECT')
    except:
        pass
    bpy.ops.object.select_all(action='DESELECT')

    source_armature = bpy.data.objects[source_armature_name]
    target_armature = bpy.data.objects[target_armature_name]
    source_armature.select_set(True)
    target_armature.select_set(True)
    mannequin_inverted_matrix = source_armature.matrix_world.inverted()

    bpy.ops.object.mode_set(mode='EDIT')
    for source_bone in source_armature.data.edit_bones:
        for target_bone in target_armature.data.edit_bones:
            if source_bone.name == target_bone.name:
                original_head_position = source_bone.head.copy()
                source_bone.head = mannequin_inverted_matrix @ target_bone.head
                offset = source_bone.head - original_head_position
                source_bone.tail = source_bone.tail + offset
                print(f"Souce {source_bone.name} moved to target position")

    bpy.ops.object.mode_set(mode='OBJECT')


def skin_mesh_to_mannequin(mesh_name):
    set_scene_units_for_rigging()
    import_ue4_mannequin()
    snap_armature_bones('root', 'Character_Armature')
    mesh = bpy.data.objects[mesh_name]
    remove_all_modifiers_by_type(mesh)
    parent_to_armature(mesh, 'root')

# Step 1: import a Mannequin

# Step 2: duplicate the mannequin and flatten its hierarchy

# Step 3: make flattened metarig child of character rig
mesh_name = 'body'
skin_mesh_to_mannequin(mesh_name)
