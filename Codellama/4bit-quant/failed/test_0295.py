import pytest
from src_0295 import task_func

def test_task_func():
    df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [20, 25, 30, 35, 40, 45], 'income': [100, 200, 300, 400, 500, 600]})
    expected_output = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [0, 0, 0, 0, 0, 0], 'income': [0, 0, 0, 0, 0, 0]})
    output = task_func(df)
    assert output.equals(expected_output)