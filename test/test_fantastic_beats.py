from pathlib import Path
from unittest.mock import call, patch

import alba_cli.fantastic_beasts as tp


def test__contains_alphabetical_characters():
    assert not tp._contains_alphabetical_characters("6\\")
    assert not tp._contains_alphabetical_characters("00:00:16,940 --> 00:00:21,748\\")
    assert tp._contains_alphabetical_characters(
        "[ian_macinnes]: all presently he burns in lust and\\"
    )


def test__strip_backslash():
    assert (
        tp._strip_backslash("[ian_macinnes]: \\all\\ presently he burns in lust and\\")
        == "[ian_macinnes]: all presently he burns in lust and"
    )


def test__identify_speaker_with_no_speaker():
    assert tp._identify_speaker("so limes the living dogs who are apt\\") is None


def test__identify_speaker_with_one_speaker():
    assert (
        tp._identify_speaker("[ian_macinnes]: all presently he burns in lust and")
        == "[ian_macinnes]"
    )


def test__identify_speaker_with_two_speaker_returns_first():
    assert (
        tp._identify_speaker("[ian_macinnes]: all [alexa] presently he burns in lust and")
        == "[ian_macinnes]"
    )


def test__remove_speakers_with_no_speakers():
    assert (
        tp._remove_speakers("so limes the living dogs who are apt\\")
        == "so limes the living dogs who are apt\\"
    )


def test__remove_speakers_with_two_speakers():
    assert (
        tp._remove_speakers("[ian_macinnes]: so limes the [alexa]:living dogs who are apt\\")
        == " so limes the living dogs who are apt\\"
    )


def test__transform_content():
    lines = [
        "{\\*\\expandedcolortbl;;}\n",
        "\\margl1440\\margr1440\\vieww11520\\viewh8400\\viewkind0\n",
        "\\pard\\tx720\\tx1440\\tx2160\\tx2880\\tx3600\\tx4320\\tx5040\\tx5760\\tx6480\\tx7200\\tx7920\\tx8640\\pardirnatural\\partightenfactor0\n",
        "\n",
        "\\f0\\fs24 \\cf0 1\\\n",
        "00:00:01,100 --> 00:00:06,826\\\n",
        "[ian_macinnes]: the dogs of india are conceived by\\\n",
        "tigers were the indians will take diverse females\\\n",
        "\\\n",
        "2\\\n",
        "00:00:06,966 --> 00:00:12,333\\\n",
        "[ian_macinnes]: and fasten them to trees and woods\\\n",
        "where tigers abide whereunto the greedy ravening tiger\\\n",
        "\\\n",
        "3\\\n",
        "00:00:12,513 --> 00:00:16,880\\\n",
        "[ian_macinnes]: comes and instantly devours some one or\\\n",
        "two of them if his lusts do not\\\n",
        "\\\n",
        "4\\\n",
        "00:00:16,940 --> 00:00:21,748\\\n",
        "[ian_macinnes]: restrain him and then being so filled\\\n",
        "with meat which thing tigers seldom meet with\\\n",
        "\\\n",
        "5\\\n",
        "00:00:21,829 --> 00:00:26,336\\\n",
        "[ian_macinnes]: all presently he burns in lust and\\\n",
        "so limes the living dogs who are apt\\\n",
        "\\\n",
        "6\\\n",
        "00:00:26,376 --> 00:00:30,603\\\n",
        "[ian_macinnes]: to conceive by him which being performed\\\n",
        "he retires to some secret place and in\\\n",
        "\\\n",
        "7\\\n",
        "00:00:30,643 --> 00:00:35,391\\\n",
        "[ian_macinnes]: the meantime the indians take away the\\\n",
        "dogs of whom come these valor dogs which\\\n",
        "\\\n",
        "8\\\n",
        "00:00:35,471 --> 00:00:40,199\\\n",
        "[ian_macinnes]: retain the stomach and courage of their\\\n",
        "father but the shape and proportion of their\\\n",
        "\\\n",
        "9\\\n",
        "00:00:40,259 --> 00:00:44,226\\\n",
        "[ian_macinnes]: mother yet they do not keep any\\\n",
        "of the first or second litter for fear\\\n",
        "\\\n",
        "10\\\n",
        "00:00:44,446 --> 00:00:49,006\\\n",
        "[ian_macinnes]: of their tiger and stomachs but make\\\n",
        "them away and reserve the third letter\\\n",
        "\\\n",
        "11\\\n",
        "00:00:51,861 --> 00:00:52,769\\\n",
        "[alexa]: i'm lexasand\\\n",
        "\\\n",
        "12\\\n",
        "00:00:54,121 --> 00:00:55,006\\\n",
        "[ian_macinnes]: i'm an mckhinnis\\\n",
        "\\\n",
        "13\\\n",
        "00:00:55,675 --> 00:00:56,017\\\n",
        "[alexa]: this is\\\n",
        "\\\n",
        "14\\\n",
        "00:00:56,001 --> 00:00:56,324\\\n",
        "[ian_macinnes]: oh\\\n",
        "\\\n",
        "15\\\n",
        "00:00:56,479 --> 00:00:59,673\\\n",
        "[alexa]: real fantastic beasts of the middle ages\\\n",
        "and renaissance\\\n",
        "\\\n",
        "16\\\n",
        "00:01:01,030 --> 00:01:05,375\\\n",
        "[ian_macinnes]: because we believe that learning about animals\\\n",
        "in history and literature and art helps us\\\n",
        "\\\n",
        "17\\\n",
        "00:01:05,495 --> 00:01:08,919\\\n",
        "[ian_macinnes]: understand our place among our fellow fellow\\\n",
        "creatures today\\\n",
        "\\\n",
        "18\\\n",
        "00:01:11,036 --> 00:01:19,026\\\n",
        "[alexa]: that is quite a lurid story i\\\n",
        "mean no appetites of all sorts where does\\\n",
        "\\\n",
        "19\\\n",
        "00:01:19,066 --> 00:01:25,291\\\n",
        "[alexa]: that come from can you tell me\\\n",
        "a little bit more about this biologically unlikely\\\n",
        "\\\n",
        "20\\\n",
        "00:01:26,185 --> 00:01:26,670\\\n",
    ]
    res = tp._transform_content(lines)
    assert (
        res
        == "[ian_macinnes]:  the dogs of india are conceived by tigers were the indians will take diverse females  and fasten them to trees and woods where tigers abide whereunto the greedy ravening tiger  comes and instantly devours some one or two of them if his lusts do not  restrain him and then being so filled with meat which thing tigers seldom meet with  all presently he burns in lust and so limes the living dogs who are apt  to conceive by him which being performed he retires to some secret place and in  the meantime the indians take away the dogs of whom come these valor dogs which  retain the stomach and courage of their father but the shape and proportion of their  mother yet they do not keep any of the first or second litter for fear  of their tiger and stomachs but make them away and reserve the third letter\n[alexa]:  i'm lexasand\n[ian_macinnes]:  i'm an mckhinnis\n[alexa]:  this is\n[ian_macinnes]:  oh\n[alexa]:  real fantastic beasts of the middle ages and renaissance\n[ian_macinnes]:  because we believe that learning about animals in history and literature and art helps us  understand our place among our fellow fellow creatures today\n[alexa]:  that is quite a lurid story i mean no appetites of all sorts where does  that come from can you tell me a little bit more about this biologically unlikely"
    )


def test__transform_file():
    with patch.object(tp, "open"), patch.object(tp, "_transform_content") as m__tranform_content:
        foo = Path("foo")
        bar = Path("bar")
        assert tp._transform_file(foo, bar)
        m__tranform_content.assert_called_once()


def test__transform_file_with_exception_returns_false():
    with patch.object(tp, "open") as m_open:
        m_open.side_effect = RuntimeError("foo")

        foo = Path("foo")
        bar = Path("bar")
        assert not tp._transform_file(foo, bar)
