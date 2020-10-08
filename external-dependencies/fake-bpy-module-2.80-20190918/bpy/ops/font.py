import sys
import typing


def case_set(case: int = 'LOWER'):
    '''Set font case 

    :param case: Case, Lower or upper case 
    :type case: int
    '''

    pass


def case_toggle():
    '''Toggle font case 

    '''

    pass


def change_character(delta: int = 1):
    '''Change font character code 

    :param delta: Delta, Number to increase or decrease character code with 
    :type delta: int
    '''

    pass


def change_spacing(delta: int = 1):
    '''Change font spacing 

    :param delta: Delta, Amount to decrease or increase character spacing with 
    :type delta: int
    '''

    pass


def delete(type: int = 'PREVIOUS_CHARACTER'):
    '''Delete text by cursor position 

    :param type: Type, Which part of the text to delete 
    :type type: int
    '''

    pass


def line_break():
    '''Insert line break at cursor position 

    '''

    pass


def move(type: int = 'LINE_BEGIN'):
    '''Move cursor to position type 

    :param type: Type, Where to move cursor to 
    :type type: int
    '''

    pass


def move_select(type: int = 'LINE_BEGIN'):
    '''Move the cursor while selecting 

    :param type: Type, Where to move cursor to, to make a selection 
    :type type: int
    '''

    pass


def open(filepath: str = "",
         filter_blender: bool = False,
         filter_backup: bool = False,
         filter_image: bool = False,
         filter_movie: bool = False,
         filter_python: bool = False,
         filter_font: bool = True,
         filter_sound: bool = False,
         filter_text: bool = False,
         filter_btx: bool = False,
         filter_collada: bool = False,
         filter_alembic: bool = False,
         filter_folder: bool = True,
         filter_blenlib: bool = False,
         filemode: int = 9,
         relative_path: bool = True,
         display_type: int = 'DEFAULT',
         sort_method: int = 'FILE_SORT_ALPHA'):
    '''Load a new font from a file 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: bool
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def select_all():
    '''Select all text 

    '''

    pass


def style_set(style: int = 'BOLD', clear: bool = False):
    '''Set font style 

    :param style: Style, Style to set selection to 
    :type style: int
    :param clear: Clear, Clear style rather than setting it 
    :type clear: bool
    '''

    pass


def style_toggle(style: int = 'BOLD'):
    '''Toggle font style 

    :param style: Style, Style to set selection to 
    :type style: int
    '''

    pass


def text_copy():
    '''Copy selected text to clipboard 

    '''

    pass


def text_cut():
    '''Cut selected text to clipboard 

    '''

    pass


def text_insert(text: str = "", accent: bool = False):
    '''Insert text at cursor position 

    :param text: Text, Text to insert at the cursor position 
    :type text: str
    :param accent: Accent mode, Next typed character will strike through previous, for special character input 
    :type accent: bool
    '''

    pass


def text_paste():
    '''Paste text from clipboard 

    '''

    pass


def text_paste_from_file(filepath: str = "",
                         filter_blender: bool = False,
                         filter_backup: bool = False,
                         filter_image: bool = False,
                         filter_movie: bool = False,
                         filter_python: bool = False,
                         filter_font: bool = False,
                         filter_sound: bool = False,
                         filter_text: bool = True,
                         filter_btx: bool = False,
                         filter_collada: bool = False,
                         filter_alembic: bool = False,
                         filter_folder: bool = True,
                         filter_blenlib: bool = False,
                         filemode: int = 9,
                         display_type: int = 'DEFAULT',
                         sort_method: int = 'FILE_SORT_ALPHA'):
    '''Paste contents from file 

    :param filepath: File Path, Path to file 
    :type filepath: str
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
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: int
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: int
    '''

    pass


def textbox_add():
    '''Add a new text box 

    '''

    pass


def textbox_remove(index: int = 0):
    '''Remove the textbox 

    :param index: Index, The current text box 
    :type index: int
    '''

    pass


def unlink():
    '''Unlink active font data-block 

    '''

    pass
