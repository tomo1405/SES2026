import pytest
from src_0317 import task_func

def test_task_func():
    # Test that the function returns a DataFrame
    assert isinstance(task_func(), pd.DataFrame)

    # Test that the DataFrame has the correct columns
    assert list(task_func().columns) == ['Category', 'Count']

    # Test that the DataFrame has the correct number of rows
    assert len(task_func()) == len(CATEGORIES)

    # Test that the DataFrame has the correct values
    expected_values = {category: random.randint(*value_range) for category in CATEGORIES}
    assert all(task_func()['Count'] == expected_values)