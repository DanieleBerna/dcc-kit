import sys
import typing
import bpy


def add_simple_uvs():
    '''Add cube map uvs on mesh 

    '''

    pass


def add_texture_paint_slot(type: int = 'BASE_COLOR',
                           name: str = "Untitled",
                           width: int = 1024,
                           height: int = 1024,
                           color: float = (0.0, 0.0, 0.0, 1.0),
                           alpha: bool = True,
                           generated_type: int = 'BLANK',
                           float: bool = False):
    '''Add a texture paint slot 

    :param type: Type, Merge method to use 
    :type type: int
    :param name: Name, Image data-block name 
    :type name: str
    :param width: Width, Image width 
    :type width: int
    :param height: Height, Image height 
    :type height: int
    :param color: Color, Default fill color 
    :type color: float
    :param alpha: Alpha, Create an image with an alpha channel 
    :type alpha: bool
    :param generated_type: Generated Type, Fill the image with a grid for UV map testingBLANK Blank, Generate a blank image.UV_GRID UV Grid, Generated grid to test UV mappings.COLOR_GRID Color Grid, Generated improved UV grid to test UV mappings. 
    :type generated_type: int
    :param float: 32 bit Float, Create image with 32 bit floating point bit depth 
    :type float: bool
    '''

    pass


def brush_colors_flip():
    '''Toggle foreground and background brush colors 

    '''

    pass


def brush_select(sculpt_tool: int = 'DRAW',
                 vertex_tool: int = 'DRAW',
                 weight_tool: int = 'DRAW',
                 image_tool: int = 'DRAW',
                 gpencil_tool: int = 'DRAW',
                 toggle: bool = False,
                 create_missing: bool = False):
    '''Select a paint mode’s brush by tool type 

    :param sculpt_tool: sculpt_tool 
    :type sculpt_tool: int
    :param vertex_tool: vertex_tool 
    :type vertex_tool: int
    :param weight_tool: weight_tool 
    :type weight_tool: int
    :param image_tool: image_tool 
    :type image_tool: int
    :param gpencil_tool: gpencil_toolDRAW Draw, The brush is of type used for drawing strokes.FILL Fill, The brush is of type used for filling areas.ERASE Erase, The brush is used for erasing strokes. 
    :type gpencil_tool: int
    :param toggle: Toggle, Toggle between two brushes rather than cycling 
    :type toggle: bool
    :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush 
    :type create_missing: bool
    '''

    pass


def face_select_all(action: int = 'TOGGLE'):
    '''Change selection for all faces 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: int
    '''

    pass


def face_select_hide(unselected: bool = False):
    '''Hide selected faces 

    :param unselected: Unselected, Hide unselected rather than selected objects 
    :type unselected: bool
    '''

    pass


def face_select_linked():
    '''Select linked faces 

    '''

    pass


def face_select_linked_pick(deselect: bool = False):
    '''Select linked faces under the cursor 

    :param deselect: Deselect, Deselect rather than select items 
    :type deselect: bool
    '''

    pass


def face_select_reveal(select: bool = True):
    '''Reveal hidden faces 

    :param select: Select 
    :type select: bool
    '''

    pass


def grab_clone(delta: float = (0.0, 0.0)):
    '''Move the clone source image 

    :param delta: Delta, Delta offset of clone image in 0.0..1.0 coordinates 
    :type delta: float
    '''

    pass


def hide_show(action: int = 'HIDE',
              area: int = 'INSIDE',
              xmin: int = 0,
              xmax: int = 0,
              ymin: int = 0,
              ymax: int = 0,
              wait_for_input: bool = True):
    '''Hide/show some vertices 

    :param action: Action, Whether to hide or show verticesHIDE Hide, Hide vertices.SHOW Show, Show vertices. 
    :type action: int
    :param area: Area, Which vertices to hide or showOUTSIDE Outside, Hide or show vertices outside the selection.INSIDE Inside, Hide or show vertices inside the selection.ALL All, Hide or show all vertices.MASKED Masked, Hide or show vertices that are masked (minimum mask value of 0.5). 
    :type area: int
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
    '''

    pass


def image_from_view(filepath: str = ""):
    '''Make an image from biggest 3D view for re-projection 

    :param filepath: File Path, Name of the file 
    :type filepath: str
    '''

    pass


def image_paint(stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
                mode: int = 'NORMAL'):
    '''Paint a stroke into the image 

    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Regular, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: int
    '''

    pass


def mask_flood_fill(mode: int = 'VALUE', value: float = 0.0):
    '''Fill the whole mask with a given value, or invert its values 

    :param mode: ModeVALUE Value, Set mask to the level specified by the ‘value’ property.VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted ‘value’ property.INVERT Invert, Invert the mask. 
    :type mode: int
    :param value: Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked 
    :type value: float
    '''

    pass


def mask_lasso_gesture(path: typing.List['bpy.types.OperatorMousePath'] = None,
                       mode: int = 'VALUE',
                       value: float = 1.0):
    '''Add mask within the lasso as you move the brush 

    :param path: Path 
    :type path: typing.List['bpy.types.OperatorMousePath']
    :param mode: ModeVALUE Value, Set mask to the level specified by the ‘value’ property.VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted ‘value’ property.INVERT Invert, Invert the mask. 
    :type mode: int
    :param value: Value, Mask level to use when mode is ‘Value’; zero means no masking and one is fully masked 
    :type value: float
    '''

    pass


def project_image(image: int = ''):
    '''Project an edited render from the active camera back onto the object 

    :param image: Image 
    :type image: int
    '''

    pass


def sample_color(location: int = (0, 0),
                 merged: bool = False,
                 palette: bool = False):
    '''Use the mouse to sample a color in the image 

    :param location: Location 
    :type location: int
    :param merged: Sample Merged, Sample the output display color 
    :type merged: bool
    :param palette: Add to Palette 
    :type palette: bool
    '''

    pass


def texture_paint_toggle():
    '''Toggle texture paint mode in 3D view 

    '''

    pass


def vert_select_all(action: int = 'TOGGLE'):
    '''Change selection for all vertices 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: int
    '''

    pass


def vert_select_ungrouped(extend: bool = False):
    '''Select vertices without a group 

    :param extend: Extend, Extend the selection 
    :type extend: bool
    '''

    pass


def vertex_color_brightness_contrast(brightness: float = 0.0,
                                     contrast: float = 0.0):
    '''Adjust vertex color brightness/contrast 

    :param brightness: Brightness 
    :type brightness: float
    :param contrast: Contrast 
    :type contrast: float
    '''

    pass


def vertex_color_dirt(blur_strength: float = 1.0,
                      blur_iterations: int = 1,
                      clean_angle: float = 3.14159,
                      dirt_angle: float = 0.0,
                      dirt_only: bool = False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param blur_strength: Blur Strength, Blur strength per iteration 
    :type blur_strength: float
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more) 
    :type blur_iterations: int
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range 
    :type clean_angle: float
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range 
    :type dirt_angle: float
    :param dirt_only: Dirt Only, Don’t calculate cleans for convex areas 
    :type dirt_only: bool
    '''

    pass


def vertex_color_from_weight():
    '''Convert active weight into gray scale vertex colors 

    '''

    pass


def vertex_color_hsv(h: float = 0.5, s: float = 1.0, v: float = 1.0):
    '''Adjust vertex color HSV values 

    :param h: Hue 
    :type h: float
    :param s: Saturation 
    :type s: float
    :param v: Value 
    :type v: float
    '''

    pass


def vertex_color_invert():
    '''Invert RGB values 

    '''

    pass


def vertex_color_levels(offset: float = 0.0, gain: float = 1.0):
    '''Adjust levels of vertex colors 

    :param offset: Offset, Value to add to colors 
    :type offset: float
    :param gain: Gain, Value to multiply colors by 
    :type gain: float
    '''

    pass


def vertex_color_set():
    '''Fill the active vertex color layer with the current paint color 

    '''

    pass


def vertex_color_smooth():
    '''Smooth colors across vertices 

    '''

    pass


def vertex_paint(stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
                 mode: int = 'NORMAL'):
    '''Paint a stroke in the active vertex color layer 

    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Regular, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: int
    '''

    pass


def vertex_paint_toggle():
    '''Toggle the vertex paint mode in 3D view 

    '''

    pass


def weight_from_bones(type: int = 'AUTOMATIC'):
    '''Set the weights of the groups matching the attached armature’s selected bones, using the distance between the vertices and the bones 

    :param type: Type, Method to use for assigning weightsAUTOMATIC Automatic, Automatic weights from bones.ENVELOPES From Envelopes, Weights from envelopes with user defined radius. 
    :type type: int
    '''

    pass


def weight_gradient(type: int = 'LINEAR',
                    xstart: int = 0,
                    xend: int = 0,
                    ystart: int = 0,
                    yend: int = 0,
                    cursor: int = 1002):
    '''Draw a line to apply a weight gradient to selected vertices 

    :param type: Type 
    :type type: int
    :param xstart: X Start 
    :type xstart: int
    :param xend: X End 
    :type xend: int
    :param ystart: Y Start 
    :type ystart: int
    :param yend: Y End 
    :type yend: int
    :param cursor: Cursor, Mouse cursor style to use during the modal operator 
    :type cursor: int
    '''

    pass


def weight_paint(stroke: typing.List['bpy.types.OperatorStrokeElement'] = None,
                 mode: int = 'NORMAL'):
    '''Paint a stroke in the current vertex group’s weights 

    :param stroke: Stroke 
    :type stroke: typing.List['bpy.types.OperatorStrokeElement']
    :param mode: Stroke Mode, Action taken when a paint stroke is madeNORMAL Regular, Apply brush normally.INVERT Invert, Invert action of brush for duration of stroke.SMOOTH Smooth, Switch brush to smooth mode for duration of stroke. 
    :type mode: int
    '''

    pass


def weight_paint_toggle():
    '''Toggle weight paint mode in 3D view 

    '''

    pass


def weight_sample():
    '''Use the mouse to sample a weight in the 3D view 

    '''

    pass


def weight_sample_group(group: int = 'DEFAULT'):
    '''Select one of the vertex groups available under current mouse position 

    :param group: Keying Set, The Keying Set to use 
    :type group: int
    '''

    pass


def weight_set():
    '''Fill the active vertex group with the current paint weight 

    '''

    pass
