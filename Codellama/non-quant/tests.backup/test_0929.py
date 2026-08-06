import pytest
from src_0929 import task_func

def test_task_func():
    # Test case 1: Empty string
    assert task_func("") == {}

    # Test case 2: Single letter
    assert task_func("a") == {"aa": 1}

    # Test case 3: Two letters
    assert task_func("ab") == {"ab": 1, "ba": 1}

    # Test case 4: Three letters
    assert task_func("abc") == {"ab": 1, "bc": 1, "ca": 1}

    # Test case 5: Four letters
    assert task_func("abcd") == {"ab": 1, "bc": 1, "cd": 1, "da": 1}

    # Test case 6: Five letters
    assert task_func("abcde") == {"ab": 1, "bc": 1, "cd": 1, "de": 1, "ea": 1}

    # Test case 7: Six letters
    assert task_func("abcdef") == {"ab": 1, "bc": 1, "cd": 1, "de": 1, "ef": 1, "fa": 1}

    # Test case 8: Seven letters
    assert task_func("abcdefg") == {"ab": 1, "bc": 1, "cd": 1, "de": 1, "ef": 1, "fg": 1, "ga": 1}

    # Test case 9: Eight letters
    assert task_func("abcdefgh") == {"ab": 1, "bc": 1, "cd": 1, "de": 1, "ef": 1, "fg": 1, "gh": 1, "ha": 1}

    # Test case 10: Nine letters
    assert task_func("abcdefghi") == {"ab": 1, "bc": 1, "cd": 1, "de": 1, "ef": 1, "fg": 1, "gh": 1, "hi": 1, "ia": 1}