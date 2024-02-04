import pytest
from um import count


def test_input():
    # Test case with one occurrence of "um"
    assert count("Um, thanks for the album.") == 1

    # Test case with a single "um"
    assert count("um") == 1

    # Test case with two occurrences of "um"
    assert count("Um, thanks, um...") == 2

    # Test case with one occurrence of "Um" (case-insensitive matching)
    assert count("Um?") == 1
