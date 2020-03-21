import logging

logger = logging.getLogger("znw")
logger.setLevel(logging.DEBUG)

logger_interaction = logger.getChild("interaction")
logger_interaction.setLevel(logging.DEBUG)

from .interface import *
