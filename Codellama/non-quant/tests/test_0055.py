import pandas as pd
from src_0055 import task_func


def test_task_func():
    text = "This is a sample text. It has multiple sentences."
    expected_output = pd.DataFrame({
        "This": [1],
        "is": [1],
        "a": [1],
        "sample": [1],
        "text": [1],
        "It": [1],
        "has": [1],
        "multiple": [1],
        "sentences": [1]
    })
    output = task_func(text)
    assert output.equals(expected_output)