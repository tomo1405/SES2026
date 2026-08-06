import pandas as pd
from src_0335 import task_func


def test_task_func():
    documents = ["This is a sample text document.", "This is another sample text document."]
    expected_output = pd.DataFrame(
        [[0.5, 0.5], [0.5, 0.5]],
        columns=["sample", "text"]
    )
    output = task_func(documents)
    assert output.equals(expected_output)