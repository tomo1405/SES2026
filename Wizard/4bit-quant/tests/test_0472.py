python
import pytest
from src_0472 import task_func

def test_task_func():
    myList = ["Hello", "World", "Hello", "Python", "Python"]
    expected_df = pd.DataFrame({"Count": [2, 1, 2, 2]}, index=["hello", "world", "python"])
    actual_df = task_func(myList)
    assert actual_df.equals(expected_df)