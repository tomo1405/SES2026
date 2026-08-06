import pytest
from src_0115 import task_func

def test_task_func():
    my_dict = {'array': np.array([1, 2, 3, 4, 5])}
    result = task_func(my_dict)
    assert isinstance(result, dict)
    assert 'normalized_array' in result
    assert isinstance(result['normalized_array'], np.ndarray)
    assert result['normalized_array'].shape == (5,)

def test_task_func_invalid_input():
    my_dict = {'array': 'invalid'}
    with pytest.raises(TypeError):
        task_func(my_dict)