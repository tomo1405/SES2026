import pytest
from src_0126 import task_func

@pytest.mark.parametrize("LETTERS, n, expected_filename", [
    (["A", "B", "C"], 2, "letter_combinations_50.json"),
    (["X", "Y", "Z"], 3, "letter_combinations_98.json"),
    (["Q", "W", "E", "R"], 1, "letter_combinations_23.json"),
])
def test_task_func(LETTERS, n, expected_filename):
    filename = task_func(LETTERS, n)
    assert filename == expected_filename