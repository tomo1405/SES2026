import pytest
from src_0384 import task_func

def test_task_func():
    text = "This is a sample text for testing"
    n = 2
    top_k = 3
    expected_output = pd.DataFrame({'n-gram': ['This is', 'is a', 'a sample'], 'Frequency': [2, 2, 1]})

    output = task_func(text, n, top_k)

    assert output.equals(expected_output)