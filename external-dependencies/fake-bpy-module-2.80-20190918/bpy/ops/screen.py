import sys
import typing


def actionzone(modifier: int = 0):
    '''Handle area action zones for mouse actions/gestures 

    :param modifier: Modifier, Modifier state 
    :type modifier: int
    '''

    pass


def animation_cancel(restore_frame: bool = True):
    '''Cancel animation, returning to the original frame 

    :param restore_frame: Restore Frame, Restore the frame when animation was initialized 
    :type restore_frame: bool
    '''

    pass


def animation_play(reverse: bool = False, sync: bool = False):
    '''Play animation 

    :param reverse: Play in Reverse, Animation is played backwards 
    :type reverse: bool
    :param sync: Sync, Drop frames to maintain framerate 
    :type sync: bool
    '''

    pass


def animation_step():
    '''Step through animation by position 

    '''

    pass


def area_dupli():
    '''Duplicate selected area into new window 

    '''

    pass


def area_join(min_x: int = -100,
              min_y: int = -100,
              max_x: int = -100,
              max_y: int = -100):
    '''Join selected areas into new window 

    :param min_x: X 1 
    :type min_x: int
    :param min_y: Y 1 
    :type min_y: int
    :param max_x: X 2 
    :type max_x: int
    :param max_y: Y 2 
    :type max_y: int
    '''

    pass


def area_move(x: int = 0, y: int = 0, delta: int = 0):
    '''Move selected area edges 

    :param x: X 
    :type x: int
    :param y: Y 
    :type y: int
    :param delta: Delta 
    :type delta: int
    '''

    pass


def area_options():
    '''Operations for splitting and merging 

    '''

    pass


def area_split(direction: int = 'HORIZONTAL',
               factor: float = 0.5,
               cursor: int = (0, 0)):
    '''Split selected area into new windows 

    :param direction: Direction 
    :type direction: int
    :param factor: Factor 
    :type factor: float
    :param cursor: Cursor 
    :type cursor: int
    '''

    pass


def area_swap():
    '''Swap selected areas screen positions 

    '''

    pass


def back_to_previous():
    '''Revert back to the original screen layout, before fullscreen area overlay 

    '''

    pass


def delete():
    '''Delete active screen 

    '''

    pass


def drivers_editor_show():
    '''Show drivers editor in a separate window 

    '''

    pass


def frame_jump(end: bool = False):
    '''Jump to first/last frame in frame range 

    :param end: Last Frame, Jump to the last frame of the frame range 
    :type end: bool
    '''

    pass


def frame_offset(delta: int = 0):
    '''Move current frame forward/backward by a given number 

    :param delta: Delta 
    :type delta: int
    '''

    pass


def header_toggle_menus():
    '''Expand or collapse the header pulldown menus 

    '''

    pass


def keyframe_jump(next: bool = True):
    '''Jump to previous/next keyframe 

    :param next: Next Keyframe 
    :type next: bool
    '''

    pass


def marker_jump(next: bool = True):
    '''Jump to previous/next marker 

    :param next: Next Marker 
    :type next: bool
    '''

    pass


def new():
    '''Add a new screen 

    '''

    pass


def redo_last():
    '''Display menu for last action performed 

    '''

    pass


def region_blend():
    '''Blend in and out overlapping region 

    '''

    pass


def region_context_menu():
    '''Display region context menu 

    '''

    pass


def region_flip():
    '''Toggle the region’s alignment (left/right or top/bottom) 

    '''

    pass


def region_quadview():
    '''Split selected area into camera, front, right & top views 

    '''

    pass


def region_scale():
    '''Scale selected area 

    '''

    pass


def repeat_history(index: int = 0):
    '''Display menu for previous actions performed 

    :param index: Index 
    :type index: int
    '''

    pass


def repeat_last():
    '''Repeat last action 

    '''

    pass


def screen_full_area(use_hide_panels: bool = False):
    '''Toggle display selected area as fullscreen/maximized 

    :param use_hide_panels: Hide Panels, Hide all the panels 
    :type use_hide_panels: bool
    '''

    pass


def screen_set(delta: int = 0):
    '''Cycle through available screens 

    :param delta: Delta 
    :type delta: int
    '''

    pass


def screenshot(filepath: str = "",
               check_existing: bool = True,
               filter_blender: bool = False,
               filter_backup: bool = False,
               filter_image: bool = True,
               filter_movie: bool = False,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = False,
               filter_text: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 9,
               show_multiview: bool = False,
               use_multiview: bool = False,
               display_type: int = 'DEFAULT',
               sort_method: int = 'FILE_SORT_ALPHA',
               full: bool = True):
    '''Capture a picture of the active area or whole Blender window 

    :param filepath: File Path, Path to file 
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: bool
    :param filter_blender: Filter .blend files 
    :type filter_blender: bool
    :param filter_backup: Filter .blend files 
    :type filter_backup: bool
    :param filter_image: Filter image files 
    :type filter_image: bool
    :param filter_movie: Filter movie files 
    :type filter_movie: bool
    :param filter_python: Filter python files 
    :type filter_python: bool
    :param filter_font: Filter font files 
    :type filter_font: bool
    :param filter_sound: Filter sound files 
    :type filter_sound: bool
    :param filter_text: Filter text files 
    :type filter_text: bool
    :param filter_btx: Filter btx files 
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: bool
    :param filter_folder: Filter folders 
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int
    :param show_multiview: Enable Multi-View 
    :type show_multiview: bool
    :param use_multiview: Use Multi-View 
    :type use_multiview: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    :param full: Full Screen, Capture the whole window (otherwise only capture the active area) 
    :type full: bool
    '''

    pass


def space_context_cycle(direction: int = 'NEXT'):
    '''Cycle through the editor context by activating the next/previous one 

    :param direction: Direction, Direction to cycle through 
    :type direction: int
    '''

    pass


def space_type_set_or_cycle(space_type: int = 'EMPTY'):
    '''Set the space type or cycle sub-type 

    :param space_type: TypeEMPTY Empty.VIEW_3D 3D Viewport, Manipulate objects in a 3D environment.IMAGE_EDITOR UV/Image Editor, View and edit images and UV Maps.NODE_EDITOR Node Editor, Editor for node-based shading and compositing tools.SEQUENCE_EDITOR Video Sequencer, Video editing tools.CLIP_EDITOR Movie Clip Editor, Motion tracking tools.DOPESHEET_EDITOR Dope Sheet, Adjust timing of keyframes.GRAPH_EDITOR Graph Editor, Edit drivers and keyframe interpolation.NLA_EDITOR Nonlinear Animation, Combine and layer Actions.TEXT_EDITOR Text Editor, Edit scripts and in-file documentation.CONSOLE Python Console, Interactive programmatic console for advanced editing and script development.INFO Info, Log of operations, warnings and error messages.TOPBAR Top Bar, Global bar at the top of the screen for global per-window settings.STATUSBAR Status Bar, Global bar at the bottom of the screen for general status information.OUTLINER Outliner, Overview of scene graph and all available data-blocks.PROPERTIES Properties, Edit properties of active object and related data-blocks.FILE_BROWSER File Browser, Browse for files and assets.PREFERENCES Preferences, Edit persistent configuration settings. 
    :type space_type: int
    '''

    pass


def spacedata_cleanup():
    '''Remove unused settings for invisible editors 

    '''

    pass


def userpref_show():
    '''Edit user preferences and system settings 

    '''

    pass


def workspace_cycle(direction: int = 'NEXT'):
    '''Cycle through workspaces 

    :param direction: Direction, Direction to cycle through 
    :type direction: int
    '''

    pass
