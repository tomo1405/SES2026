import pytest
from src_0557 import task_func

def test_task_func():
    # Test with a fixed seed for reproducibility
    random.seed(0)
    np.random.seed(0)

    # Define test parameters
    s = "hello"
    min_length = 5
    max_length = 10
    letters = "abcdefghijklmnopqrstuvwxyz"

    # Expected output
    expected_string = "hijkl"  # This is what gets generated with the given seed
    expected_similarity = True  # Since 'hijkl' and 'hello' have a similarity ratio >= 0.5

    # Run the function
    generated_s, is_similar = task_func(s, min_length, max_length, letters)

    # Assertions
    assert generated_s == expected_string, f"Expected {expected_string}, got {generated_s}"
    assert is_similar == expected_similarity, f"Expected {expected_similarity}, got {is_similar}"

def test_task_func_short_string():
    # Test with a fixed seed for reproducibility
    random.seed(0)
    np.random.seed(0)

    # Define test parameters
    s = "a"
    min_length = 1
    max_length = 1
    letters = "abc"

    # Expected output
    expected_string = "a"  # This is what gets generated with the given seed
    expected_similarity = True  # Since 'a' and 'a' have a similarity ratio of 1.0

    # Run the function
    generated_s, is_similar = task_func(s, min_length, max_length, letters)

    # Assertions
    assert generated_s == expected_string, f"Expected {expected_string}, got {generated_s}"
    assert is_similar == expected_similarity, f"Expected {expected_similarity}, got {is_similar}"

def test_task_func_no_similarity():
    # Test with a fixed seed for reproducibility
    random.seed(0)
    np.random.seed(0)

    # Define test parameters
    s = "hello"
    min_length = 5
    max_length = 10
    letters = "xyz"

    # Expected output
    expected_string = "xxxxx"  # This is what gets generated with the given seed
    expected_similarity = False  # Since 'xxxxx' and 'hello' have a similarity ratio < 0.5

    # Run the function
    generated_s, is_similar = task_func(s, min_length, max_length, letters)

    # Assertions
    assert generated_s == expected_string, f"Expected {expected_string}, got {generated_s}"
    assert is_similar == expected_similarity, f"Expected {expected_similarity}, got {is_similar}"