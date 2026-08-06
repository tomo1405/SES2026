python
import pytest
from src_0126 import task_func

def test_task_func():
    LETTERS = 'abcde'
    n = 3
    filename = task_func(LETTERS, n)
    assert filename.startswith('letter_combinations_')
    assert filename.endswith('.json')
    assert len(filename.split('_')) == 3
    assert filename.split('_')[1].isdigit()
    assert len(filename.split('_')[1]) == 3
    assert len(filename.split('.')[0]) == 24