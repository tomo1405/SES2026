python
import pytest
from src_0730 import task_func

def test_task_func():
    strings = ['hello', 'world']
    loaded_strings = task_func(strings)
    assert loaded_strings == strings

    loaded_strings = task_func(strings, filename='test.pkl')
    assert loaded_strings == strings
    assert os.path.isfile('test.pkl')
    os.remove('test.pkl')

    with pytest.raises(TypeError):
        task_func('not a list')

    with pytest.raises(TypeError):
        task_func(['hello', 'world'], filename=123)