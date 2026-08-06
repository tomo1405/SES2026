import pytest
from src_0694 import task_func

def test_task_func():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    columns = ['A', 'B', 'C']
    expected_result = [[-1.22474487, -1.22474487, -1.22474487],
                       [ 1.22474487,  1.22474487,  1.22474487],
                       [ 0. ,  0. ,  0. ]]

    result = task_func(tuples_list, columns)
    assert result.values.tolist() == expected_result

if __name__ == "__main__":
    pytest.main()