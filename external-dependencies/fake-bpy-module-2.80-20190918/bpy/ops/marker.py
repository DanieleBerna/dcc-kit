import sys
import typing


def add():
    '''Add a new time marker 

    '''

    pass


def camera_bind():
    '''Bind the selected camera to a marker on the current frame 

    '''

    pass


def delete():
    '''Delete selected time marker(s) 

    '''

    pass


def duplicate(frames: int = 0):
    '''Duplicate selected time marker(s) 

    :param frames: Frames 
    :type frames: int
    '''

    pass


def make_links_scene(scene: int = ''):
    '''Copy selected markers to another scene 

    :param scene: Scene 
    :type scene: int
    '''

    pass


def move(frames: int = 0, tweak: bool = False):
    '''Move selected time marker(s) 

    :param frames: Frames 
    :type frames: int
    :param tweak: Tweak, Operator has been activated using a tweak event 
    :type tweak: bool
    '''

    pass


def rename(name: str = "RenamedMarker"):
    '''Rename first selected time marker 

    :param name: Name, New name for marker 
    :type name: str
    '''

    pass


def select(extend: bool = False, camera: bool = False):
    '''Select time marker(s) 

    :param extend: Extend, Extend the selection 
    :type extend: bool
    :param camera: Camera, Select the camera 
    :type camera: bool
    '''

    pass


def select_all(action: int = 'TOGGLE'):
    '''Change selection of all time markers 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: int
    '''

    pass


def select_box(xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: int = 'SET',
               tweak: bool = False):
    '''Select all time markers using box selection 

    :param xmin: X Min 
    :type xmin: int
    :param xmax: X Max 
    :type xmax: int
    :param ymin: Y Min 
    :type ymin: int
    :param ymax: Y Max 
    :type ymax: int
    :param wait_for_input: Wait for Input 
    :type wait_for_input: bool
    :param mode: ModeSET Set, Set a new selection.ADD Extend, Extend existing selection.SUB Subtract, Subtract existing selection. 
    :type mode: int
    :param tweak: Tweak, Operator has been activated using a tweak event 
    :type tweak: bool
    '''

    pass
