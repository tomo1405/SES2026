import pytest
from src_0577 import task_func

def test_task_func():
    # Test with empty list
    assert task_func([]) == pd.Series()

    # Test with list of length 1
    assert task_func([1]) == pd.Series([1])

    # Test with list of length 2
    assert task_func([1, 2]) == pd.Series([1, 2])

    # Test with list of length 3
    assert task_func([1, 2, 3]) == pd.Series([1, 2, 3])

    # Test with list of length 4
    assert task_func([1, 2, 3, 4]) == pd.Series([1, 2, 3, 4])

    # Test with list of length 5
    assert task_func([1, 2, 3, 4, 5]) == pd.Series([1, 2, 3, 4, 5])

    # Test with list of length 6
    assert task_func([1, 2, 3, 4, 5, 6]) == pd.Series([1, 2, 3, 4, 5, 6])

    # Test with list of length 7
    assert task_func([1, 2, 3, 4, 5, 6, 7]) == pd.Series([1, 2, 3, 4, 5, 6, 7])

    # Test with list of length 8
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8])

    # Test with list of length 9
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Test with list of length 10
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Test with list of length 11
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    # Test with list of length 12
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    # Test with list of length 13
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    # Test with list of length 14
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    # Test with list of length 15
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    # Test with list of length 16
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    # Test with list of length 17
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    # Test with list of length 18
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    # Test with list of length 19
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    # Test with list of length 20
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])