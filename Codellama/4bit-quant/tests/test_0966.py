import pytest
from src_0966 import task_func

def test_task_func():
    source_directory = "source_directory"
    target_directory = "target_directory"
    pattern = r"\d{4}"

    # Test case 1: source directory does not exist
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 2: source directory is not a directory
    with pytest.raises(ValueError):
        task_func("not_a_directory", target_directory, pattern)

    # Test case 3: target directory does not exist
    with pytest.raises(ValueError):
        task_func(source_directory, "not_a_directory", pattern)

    # Test case 4: target directory is not a directory
    with pytest.raises(ValueError):
        task_func(source_directory, "not_a_directory", pattern)

    # Test case 5: pattern is not a valid regular expression
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, "not_a_pattern")

    # Test case 6: source directory is empty
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 7: target directory is empty
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 8: source directory contains files that match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 9: target directory contains files that match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 10: source directory contains files that do not match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 11: target directory contains files that do not match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 12: source directory contains files that match the pattern and target directory contains files that match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 13: source directory contains files that match the pattern and target directory contains files that do not match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 14: source directory contains files that do not match the pattern and target directory contains files that match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)

    # Test case 15: source directory contains files that do not match the pattern and target directory contains files that do not match the pattern
    with pytest.raises(ValueError):
        task_func(source_directory, target_directory, pattern)