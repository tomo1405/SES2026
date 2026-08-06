from src_0794 import task_func


def test_task_func_default_list():
    result = task_func()
    assert len(result) == 10
    assert set(result) == set(ELEMENTS)

def test_task_func_custom_list():
    custom_list = ['X', 'Y', 'Z', 'W', 'V', 'U', 'T', 'S', 'R', 'Q']
    result = task_func(custom_list)
    assert len(result) == 10
    assert set(result) == set(custom_list)

def test_task_func_shuffle():
    result = task_func()
    assert list(result) != ELEMENTS

def test_task_func_concatenation():
    result = task_func()
    assert list(result)[3:] + list(result)[:3] == list(result)

def test_task_func_preserves_elements():
    result = task_func()
    assert all(elem in ELEMENTS for elem in result)

def test_task_func_randomness():
    result1 = task_func()
    result2 = task_func()
    assert result1 != result2