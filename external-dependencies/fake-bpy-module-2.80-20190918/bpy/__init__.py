import sys
import typing
from . import types
from . import ops
from . import app
from . import context
from . import utils
from . import props
from . import path

context: 'types.Context' = None

data: 'types.BlendData' = None
'''Access to Blenders internal data '''
