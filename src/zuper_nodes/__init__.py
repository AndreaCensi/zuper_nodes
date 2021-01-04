__version__ = "6.1.2101041536"
__date__ = "2021-01-04T15:36:44.646271"

from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)


logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .language import *

from .language_parse import *
from .language_recognize import *

from .structures import *
from .compatibility import *
