import pytest
from src_0384 import task_func

def test_task_func():
    text = "This is a sample text for testing"
    n = 2
    top_k = 5
    expected_output = pd.DataFrame({'n-gram': ['This is', 'is a', 'a sample', 'sample text', 'text for'],
                                   'Frequency': [1, 1, 1, 1, 1]},
                                  columns=['n-gram', 'Frequency'])
    output = task_func(text, n, top_k)
    assert output.equals(expected_output)