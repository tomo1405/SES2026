import pytest
from src_0127 import task_func

def test_task_func():
    # Test with default arguments
    report_df = task_func()
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df.dtypes.tolist() == ['object', 'float64', 'float64', 'object', 'float64']

    # Test with custom arguments
    report_df = task_func(animals=['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'], seed=1234)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df.dtypes.tolist() == ['object', 'float64', 'float64', 'object', 'float64']

    # Test with invalid arguments
    with pytest.raises(ValueError):
        report_df = task_func(animals=['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'], seed='abc')