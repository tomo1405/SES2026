python
import pytest
from src_0472 import task_func

def test_task_func():
    myList = ["Hello", "World", "Hello", "Python", "Python", "Programming"]
    expected_df = pd.DataFrame({"Count": [1, 1, 2, 2, 1]}, index=["hello", "world", "python", "programming"])
    assert task_func(myList).equals(expected_df)