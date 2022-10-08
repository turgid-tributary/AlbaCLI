from unittest.mock import patch

import alba_cli.main as tp


def test_main():
    with patch.object(tp, "parse_args") as m_parse_args:
        tp.main()
        m_parse_args.assert_called_once()
