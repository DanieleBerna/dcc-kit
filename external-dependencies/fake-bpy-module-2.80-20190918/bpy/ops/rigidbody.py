import sys
import typing


def bake_to_keyframes(frame_start: int = 1,
                      frame_end: int = 250,
                      step: int = 1):
    '''Bake rigid body transformations of selected objects to keyframes 

    :param frame_start: Start Frame, Start frame for baking 
    :type frame_start: int
    :param frame_end: End Frame, End frame for baking 
    :type frame_end: int
    :param step: Frame Step, Frame Step 
    :type step: int
    '''

    pass


def connect(con_type: int = 'FIXED',
            pivot_type: int = 'CENTER',
            connection_pattern: int = 'SELECTED_TO_ACTIVE'):
    '''Create rigid body constraints between selected rigid bodies 

    :param con_type: Type, Type of generated constraintFIXED Fixed, Glue rigid bodies together.POINT Point, Constrain rigid bodies to move around common pivot point.HINGE Hinge, Restrict rigid body rotation to one axis.SLIDER Slider, Restrict rigid body translation to one axis.PISTON Piston, Restrict rigid body translation and rotation to one axis.GENERIC Generic, Restrict translation and rotation to specified axes.GENERIC_SPRING Generic Spring, Restrict translation and rotation to specified axes with springs.MOTOR Motor, Drive rigid body around or along an axis. 
    :type con_type: int
    :param pivot_type: Location, Constraint pivot locationCENTER Center, Pivot location is between the constrained rigid bodies.ACTIVE Active, Pivot location is at the active object position.SELECTED Selected, Pivot location is at the selected object position. 
    :type pivot_type: int
    :param connection_pattern: Connection Pattern, Pattern used to connect objectsSELECTED_TO_ACTIVE Selected to Active, Connect selected objects to the active object.CHAIN_DISTANCE Chain by Distance, Connect objects as a chain based on distance, starting at the active object. 
    :type connection_pattern: int
    '''

    pass


def constraint_add(type: int = 'FIXED'):
    '''Add Rigid Body Constraint to active object 

    :param type: Rigid Body Constraint TypeFIXED Fixed, Glue rigid bodies together.POINT Point, Constrain rigid bodies to move around common pivot point.HINGE Hinge, Restrict rigid body rotation to one axis.SLIDER Slider, Restrict rigid body translation to one axis.PISTON Piston, Restrict rigid body translation and rotation to one axis.GENERIC Generic, Restrict translation and rotation to specified axes.GENERIC_SPRING Generic Spring, Restrict translation and rotation to specified axes with springs.MOTOR Motor, Drive rigid body around or along an axis. 
    :type type: int
    '''

    pass


def constraint_remove():
    '''Remove Rigid Body Constraint from Object 

    '''

    pass


def mass_calculate(material: int = 'DEFAULT', density: float = 1.0):
    '''Automatically calculate mass values for Rigid Body Objects based on volume 

    :param material: Material Preset, Type of material that objects are made of (determines material density) 
    :type material: int
    :param density: Density, Custom density value (kg/m^3) to use instead of material preset 
    :type density: float
    '''

    pass


def object_add(type: int = 'ACTIVE'):
    '''Add active object as Rigid Body 

    :param type: Rigid Body TypeACTIVE Active, Object is directly controlled by simulation results.PASSIVE Passive, Object is directly controlled by animation system. 
    :type type: int
    '''

    pass


def object_remove():
    '''Remove Rigid Body settings from Object 

    '''

    pass


def object_settings_copy():
    '''Copy Rigid Body settings from active object to selected 

    '''

    pass


def objects_add(type: int = 'ACTIVE'):
    '''Add selected objects as Rigid Bodies 

    :param type: Rigid Body TypeACTIVE Active, Object is directly controlled by simulation results.PASSIVE Passive, Object is directly controlled by animation system. 
    :type type: int
    '''

    pass


def objects_remove():
    '''Remove selected objects from Rigid Body simulation 

    '''

    pass


def shape_change(type: int = 'MESH'):
    '''Change collision shapes for selected Rigid Body Objects 

    :param type: Rigid Body ShapeBOX Box, Box-like shapes (i.e. cubes), including planes (i.e. ground planes).SPHERE Sphere.CAPSULE Capsule.CYLINDER Cylinder.CONE Cone.CONVEX_HULL Convex Hull, A mesh-like surface encompassing (i.e. shrinkwrap over) all vertices (best results with fewer vertices).MESH Mesh, Mesh consisting of triangles only, allowing for more detailed interactions than convex hulls. 
    :type type: int
    '''

    pass


def world_add():
    '''Add Rigid Body simulation world to the current scene 

    '''

    pass


def world_remove():
    '''Remove Rigid Body simulation world from the current scene 

    '''

    pass
