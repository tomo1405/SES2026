import pytest
from src_0659 import task_func

def test_task_func():
    texts = ['This is a sample text', 'This is another sample text']
    expected_output = pd.DataFrame({'this': [1, 1], 'is': [2, 2], 'a': [1, 1], 'sample': [2, 2], 'text': [2, 2]})
    output = task_func(texts)
    assert output.equals(expected_output)