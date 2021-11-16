__version__ = "7.3"
__date__ = ""

from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)


logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .language import *

from .language_parse import *
from .language_recognize import *


from .structures import *
from .compatibility import *

logger.hello_module_finished(__name__)
