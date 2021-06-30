__version__ = "7.1.2106301840"
__date__ = "2021-06-30T18:40:11.306725+00:00"

from zuper_commons.logs import ZLogger

logger = ZLogger(__name__)


logger.hello_module(name=__name__, filename=__file__, version=__version__, date=__date__)

from .language import *

from .language_parse import *
from .language_recognize import *

from .structures import *
from .compatibility import *
