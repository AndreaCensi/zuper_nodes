from zuper_commons.logs import ZLogger, ZLoggerInterface

logger: ZLoggerInterface = ZLogger(__name__)

from . import test_language, test_protocol
