from argparse import Namespace
from unittest.mock import patch

from alba_cli import cli as tp


def test_parse_args():
    with patch.object(tp, "sys") as m_sys:
        m_sys.argv = ["command"]
        assert isinstance(tp.parse_args(), Namespace)


def test_parse_args_fantastic_beasts():
    with patch.object(tp, "sys") as m_sys:
        m_sys.argv = [
            "command",
            "beasts",
            "-i",
            "foo",
            "-o",
            "bar",
        ]
        assert isinstance(tp.parse_args(), Namespace)
