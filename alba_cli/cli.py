import sys
from argparse import ArgumentParser, Namespace


def build_parser() -> ArgumentParser:
    """
    Builds a parser to parse command line arguments for the tool.

    :returns: an fully configured ArgumentParser
    """
    parser = ArgumentParser(
        description=(
            "Command line tool containing various subcommands "
            "to assist the Albion College English department"
        )
    )
    return parser


def parse_args() -> Namespace:
    """
    Parse CLI arguments.

    :returns: an argparse Namespace object containing the CLI arguments
    """
    return build_parser().parse_args(sys.argv[1:])
