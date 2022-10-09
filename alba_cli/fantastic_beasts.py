import logging
import re
from pathlib import Path
from typing import List, NamedTuple, Optional

log = logging.getLogger(__name__)


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


class SpeakerMonologue(NamedTuple):
    """
    Represents a single monologue of speaker in the podcast.
    """

    speaker: str
    thoughts: List[str]

    def to_string(self):
        thought_string = " ".join(self.thoughts)
        return f"{self.speaker}: {thought_string}".replace("\n", "").replace("\r", "")


def _transform_content(content_lines: List[str]) -> str:
    """
    Transform a single file from its raw representation into beautified output.

    :param content_lines: a list of strings representing the content of a file to be transformed
    :returns: the entire file content, beautified
    """
    current_speaker = ""
    consistent_thoughts = []  # type: List[SpeakerMonologue]
    for line in content_lines:
        # Skip lines which don't have any actual content
        if not _contains_alphabetical_characters(line):
            continue
        speaker = _identify_speaker(line)
        if speaker is None and len(consistent_thoughts) == 0:
            log.warning(
                "Encountered line of what looks like transcription "
                f"before any speaker has been identified. Skipping: {line}"
            )
            continue

        clean_line = _strip_backslash(_remove_speakers(line))
        if speaker is None or speaker == current_speaker:
            consistent_thoughts[-1].thoughts.append(clean_line)
        else:
            current_speaker = speaker
            consistent_thoughts.append(SpeakerMonologue(speaker=speaker, thoughts=[clean_line]))

    return "\n".join([thought.to_string() for thought in consistent_thoughts])


def _transform_file(file_path_input: Path, file_path_output: Path) -> bool:
    """
    Transform a single file represnting a podcast transcript.

    :param file_path_input: the input file path
    :param file_path_output: the output file path
    :returns: True if the file could be transformed, false otherwise
    """
    try:
        with open(file_path_input, "r") as input_fp:
            lines = input_fp.readlines()
            transformed = _transform_content(lines)
        with open(file_path_output, "w+") as output_fp:
            output_fp.write(transformed)
        return True
    except Exception:
        log.exception(
            f"Unexpected error transorming {file_path_input}"
            f"and writing it to {file_path_output}"
        )
        return False
