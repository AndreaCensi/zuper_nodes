import traceback

from . import logger
from .interface import wrap_direct


def launcher_main():
    node = DummyImageFilter()
    protocol = protocol_image_filter
    wrap_direct(node=node, protocol=protocol)

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
    parsed = parser.parse_args(args)

    node_symbol = parsed.node
    try:
        node = import_name(node_symbol)
    except BaseException:
        msg = 'Cannot import the node class'
        logger.error(msg, node_symbol=node_symbol, tb=traceback.format_exc())
        sys.exit(3)

    protocol_symbol = parsed.protocol
    try:
        protocol = import_name(protocol_symbol)
    except BaseException:
        msg = 'Cannot import the protocol class'
        logger.error(msg, protocol_symbol=protocol_symbol, tb=traceback.format_exc())
        sys.exit(3)

    return wrap_direct()


if __name__ == '__main__':
    wrap_script_entry_point(launcher_main)
