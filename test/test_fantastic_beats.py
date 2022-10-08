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
