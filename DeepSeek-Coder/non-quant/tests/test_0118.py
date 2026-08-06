import pytest
from src_0118 import task_func

def test_task_func():
    # Test with default parameters
    result = task_func(5)
    assert len(result) == 5
    assert all(col in result.columns for col in ['Name', 'Age', 'Gender', 'Score'])

    # Test with custom parameters
    result = task_func(3, seed=123, name_list=['Alice', 'Bob'], gender_list=['Female', 'Male'], age_range=(16, 20), score_range=(60, 90))
    assert len(result) == 3
    assert all(result['Gender'].isin(['Female', 'Male']))

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(-5)