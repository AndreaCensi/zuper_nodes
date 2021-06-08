import argparse
import os
import sys
import traceback

from zuper_commons.types import import_name

from . import logger
from .interface import wrap_direct

__all__ = ['launcher_main']


# noinspection PyBroadException
def launcher_main():
    sys.path.append(os.getcwd())
    prog = 'node-launch'
    parser = argparse.ArgumentParser(prog=prog)
    # define arguments
    parser.add_argument(
        "--protocol", required=True,
        help="Protocol (python symbol)",
    )
    parser.add_argument(
        "--node", required=True,
        help="node class (python symbol)",
    )
    # parse arguments
    parsed = parser.parse_args()

    node_symbol = parsed.node
    try:
        node_type = import_name(node_symbol)
    except Exception:
        msg = 'Cannot import the node class'
        logger.error(msg, node_symbol=node_symbol, tb=traceback.format_exc())
        sys.exit(3)

    # noinspection PyCallingNonCallable
    try:
        node = node_type()
    except Exception:
        msg = 'Cannot instantiate the node class'
        logger.error(msg, node_symbol=node_symbol, tb=traceback.format_exc())
        sys.exit(3)

    protocol_symbol = parsed.protocol
    try:
        protocol = import_name(protocol_symbol)
    except Exception:
        msg = 'Cannot import the protocol class'
        logger.error(msg, protocol_symbol=protocol_symbol, tb=traceback.format_exc())
        sys.exit(3)

    return wrap_direct(node=node, protocol=protocol, args=[])


if __name__ == '__main__':
    launcher_main()
