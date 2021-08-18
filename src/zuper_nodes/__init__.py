__version__ = "7.1.2108182113"
__date__ = "2021-08-18T21:13:58.271182+00:00"

from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)


logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .language import *

from .language_parse import *
from .language_recognize import *


from .structures import *
from .compatibility import *
