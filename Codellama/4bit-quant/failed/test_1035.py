import pytest
from src_1035 import task_func

def test_task_func():
    # Test case 1: Both stores exceed the sales threshold
    s1 = pd.Series([201, 199, 202, 198, 200], index=CATEGORIES)
    s2 = pd.Series([205, 203, 201, 199, 202], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 0.0

    # Test case 2: One store does not exceed the sales threshold
    s1 = pd.Series([201, 199, 202, 198, 200], index=CATEGORIES)
    s2 = pd.Series([205, 203, 201, 199, 198], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is None
    assert edit_distance == 0.0

    # Test case 3: Both stores exceed the sales threshold, but the series are different
    s1 = pd.Series([201, 199, 202, 198, 200], index=CATEGORIES)
    s2 = pd.Series([205, 203, 201, 199, 202], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 1.0