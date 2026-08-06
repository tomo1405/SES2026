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
    report_df = task_func(animals=['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'], seed=42)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    assert report_df['Mean'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Median'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Mode'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Standard Deviation'].tolist() == [0, 0, 0, 0, 0]

    # Test with custom arguments and different seed
    report_df = task_func(animals=['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda'], seed=1234)
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    assert report_df['Mean'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Median'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Mode'].tolist() == [50, 50, 50, 50, 50]
    assert report_df['Standard Deviation'].tolist() == [0, 0, 0, 0, 0]