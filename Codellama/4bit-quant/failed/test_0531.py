import pytest
from src_0531 import task_func

def test_task_func():
    # Test 1: Empty input
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test 2: Invalid age
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [-1, 20]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test 3: Valid input
    df = pd.DataFrame({"name": ["Alice", "Bob"], "age": [20, 30]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter()
    assert ax is None

    # Test 4: Valid input with duplicates
    df = pd.DataFrame({"name": ["Alice", "Bob", "Alice"], "age": [20, 30, 40]})
    duplicates_counter, ax = task_func(df)
    assert duplicates_counter == Counter({20: 2})
    assert ax is not None
    assert ax.get_xlabel() == "Age"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Distribution of Ages for Duplicate Names"