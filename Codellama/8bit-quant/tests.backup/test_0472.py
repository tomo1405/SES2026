import pytest
from src_0472 import task_func

def test_task_func():
    myList = ["hello", "world", "hello", "world"]
    expected_output = pd.DataFrame({"Count": [2, 2]}, index=["hello", "world"])

    output = task_func(myList)

    assert output.equals(expected_output)