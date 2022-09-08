import logging

from zuper_commons.logs import ZLogger, ZLoggerInterface

logger: ZLoggerInterface = ZLogger(__name__)

logger.setLevel(logging.DEBUG)

logger_interaction = logger.get_child("interaction")
logger_interaction.setLevel(logging.CRITICAL)

from .interface import *
