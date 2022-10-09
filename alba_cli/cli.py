import sys
from argparse import ArgumentParser, Namespace
from .fantastic_beasts import transform_file


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
    parser.set_defaults(func=lambda _: parser.print_help())
    subparsers = parser.add_subparsers(help="sub-command help")
    fantastic_beasts_subparser = subparsers.add_parser(
        "beasts",
        description="Used to transform"
        "raw transcripts of the Real Fantastic Beasts podcast into beautified output.",
    )
    _add_fantastic_beasts_args(fantastic_beasts_subparser)
    return parser


def _add_fantastic_beasts_args(parser: ArgumentParser) -> ArgumentParser:
    """
    Add options specific to the Fantastic Beasts subcommand to a parser.

    :param parser: the parser to add the options to
    :returns: the parser with the fantastic beast options added
    """
    parser.add_argument(
        "-i",
        dest="input_transcript",
        action="store",
        help="A file path pointing to a raw transcript in need of tranformation",
        required=True,
    )
    parser.add_argument(
        "-o",
        dest="output_transcript",
        action="store",
        help="A file path pointing to where the tranformed transcript should be saved",
        required=True,
    )
    parser.set_defaults(func=transform_file)
    return parser


def parse_args() -> Namespace:
    """
    Parse CLI arguments.

    :returns: an argparse Namespace object containing the CLI arguments
    """
    return build_parser().parse_args(sys.argv[1:])
