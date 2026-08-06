import numpy as np
from src_0930 import task_func


def test_task_func():
    # Test case 1: Empty string
    word = ""
    expected_result = np.array([])
    assert np.array_equal(task_func(word), expected_result)

    # Test case 2: Single character string
    word = "a"
    expected_result = np.array([0])
    assert np.array_equal(task_func(word), expected_result)

    # Test case 3: Multi-character string
    word = "hello"
    expected_result = np.array([4, 1, 1, 1, 1])
    assert np.array_equal(task_func(word), expected_result)

    # Test case 4: Non-ASCII characters
    word = "résumé"
    expected_result = np.array([195, 163, 195, 169, 195, 177])
    assert np.array_equal(task_func(word), expected_result)

    # Test case 5: Unicode characters
    word = "😊😞😍😘😜"
    expected_result = np.array([128522, 128522, 128522, 128522, 128522])
    assert np.array_equal(task_func(word), expected_result)