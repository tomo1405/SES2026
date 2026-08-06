import pytest
from src_0472 import task_func

def test_task_func():
    myList = ["hello", "world", "hello", "world", "hello"]
    expected_output = pd.DataFrame({"Count": [3, 2]}, index=["hello", "world"])

    output = task_func(myList)

    assert output.equals(expected_output)