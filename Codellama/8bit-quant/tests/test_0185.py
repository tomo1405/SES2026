import pandas as pd
from src_0185 import task_func


def test_task_func():
    dataframe = pd.DataFrame({'text': ['This is a sample text.', 'This is another sample text.']})
    text_column = 'text'
    expected_output = pd.DataFrame({'this': [1, 1], 'is': [1, 1], 'a': [1, 1], 'sample': [1, 1], 'text': [1, 1]})

    output = task_func(dataframe, text_column)

    assert output.equals(expected_output)