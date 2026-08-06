python
import pytest
from src_0472 import task_func

def test_task_func():
    myList = ["Python is awesome", "I love Python", "Python is great"]
    expected_df = pd.DataFrame({"Count": [2, 1, 1]}, index=["python", "love", "is"])
    assert task_func(myList).equals(expected_df)