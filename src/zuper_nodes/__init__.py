__version__ = '1.0.0'

from .col_logging import logger

logger.info(f'aido_nodes {__version__}')

from .language import *

from .language_parse import *
from .language_recognize import *

