import pytest
from src_0560 import task_func

def test_task_func():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected_euclidean_distance = 5.196152422706632
    expected_df = pd.DataFrame({'A': a, 'B': b})
    expected_ax = None  # You can't easily test the plot, so we'll set this to None
    
    euclidean_distance, df, ax = task_func(a, b)
    
    assert euclidean_distance == expected_euclidean_distance
    assert df.equals(expected_df)
    assert ax is expected_ax