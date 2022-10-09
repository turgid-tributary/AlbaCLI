import logging
import time

from alba_cli.cli import parse_args

log = logging.getLogger(__name__)


def main() -> int:
    """
    The main entry point for AlbaCLI

    :returns: eventually should return 0 for success; 1 otherwise
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )
    logging.Formatter.converter = time.gmtime
    args = parse_args()
    return args.func(args)
