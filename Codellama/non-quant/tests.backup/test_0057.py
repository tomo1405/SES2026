import pytest
from src_0057 import task_func

def test_task_func():
    text = "Score: 100, Category: A\nScore: 90, Category: B\nScore: 80, Category: C"
    expected_df = pd.DataFrame({"Score": [100, 90, 80], "Category": ["A", "B", "C"]})
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)