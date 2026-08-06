import pytest
from collections import Counter
import pandas as pd

def task_func(myList):
    words = [w.lower().strip() for w in myList]
    word_counts = dict(Counter(words))
    report_df = pd.DataFrame.from_dict(word_counts, orient="index", columns=["Count"])

    return report_df

def test_task_func():
    myList = ["Hello", "World", "Hello", "World", "hello"]
    expected_output = pd.DataFrame({"Count": [3, 3]}, index=["hello", "world"])
    actual_output = task_func(myList)
    assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()