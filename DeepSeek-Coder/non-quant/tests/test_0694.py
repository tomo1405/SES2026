import pytest
from src_0694 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    columns = ['A', 'B']
    expected_output = pd.DataFrame({
        'A': [-1.224744871391589, -0.7071067811865476, 0.2247448713915892],
        'B': [-1.224744871391589, -0.7071067811865476, 0.2247448713915892]
    })
    result = task_func(tuples_list, columns)
    pd.testing.assert_frame_equal(result, expected_output)

    # Add more test cases as needed

pytest.main()