import pytest
from src_0127 import task_func

def test_task_func():
    # Test with default arguments
    report_df = task_func()
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    assert report_df['Mean'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Median'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Mode'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Standard Deviation'].tolist() == [0, 0, 0, 0, 0]

    # Test with custom arguments
    report_df = task_func(animals=['Lion', 'Tiger', 'Panda'], seed=123)
    assert report_df.shape == (3, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Tiger', 'Panda']
    assert report_df['Mean'].tolist() == [50, 50, 50]
    assert report_df['Median'].tolist() == [50, 50, 50]
    assert report_df['Mode'].tolist() == [50, 50, 50]
    assert report_df['Standard Deviation'].tolist() == [0, 0, 0]