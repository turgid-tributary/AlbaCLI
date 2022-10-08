import re
from typing import Optional


def _contains_alphabetical_characters(content: str) -> bool:
    """
    Returns true if line contains alphabetical characters.

    :param content: the string to check for alphabetical characters
    :returns: True if the string contains any alphabetical character, False otherwise
    """
    return re.match(r".*[a-zA-Z].*", content) is not None


def _strip_backslash(content: str) -> str:
    """
    Removes backslashes from the content

    :param content: the string to remove backslashes from
    :returns: The string removed of backslashes
    """
    return content.replace("\\", "")


def _identify_speaker(content: str) -> Optional[str]:
    """
    Identifies the first speaker in a line of the transcript

    :param content: the string to find a first speaker in
    :returns: None if a speaker can't be found; othwerwise the token identifying the speaker is
        returned (eg "[ian_macinnes]")
    """
    _match = re.match(r"\[[^\]]*\]", content)
    if _match is None:
        return None
    return _match.group(0)


def _remove_speakers(content: str) -> str:
    """
    Removes any speaker in a string

    :param content: the string to remove speakers from
    :returns: the string cleaned of all speakers
    """
    return re.sub(r"\[[^\]]*\]:", "", content)
