import logging

logger = logging.getLogger("nodes-wrapper")
logger.setLevel(logging.DEBUG)

logger_interaction = logger.getChild("interaction")
logger_interaction.setLevel(logging.CRITICAL)

from .interface import *
