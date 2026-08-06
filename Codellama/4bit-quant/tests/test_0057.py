import pandas as pd
from src_0057 import task_func


def test_task_func():
    text = "Score: 100, Category: A\nScore: 200, Category: B\nScore: 300, Category: C"
    expected_output = pd.DataFrame({"Score": [100, 200, 300], "Category": ["A", "B", "C"]})
    actual_output = task_func(text)
    assert actual_output.equals(expected_output)