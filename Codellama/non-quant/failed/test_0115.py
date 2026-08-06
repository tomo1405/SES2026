import pytest
from src_0115 import task_func

def test_task_func_type_error():
    my_dict = {'array': 'not an array'}
    with pytest.raises(TypeError):
        task_func(my_dict)

def test_task_func_normalization():
    my_dict = {'array': np.array([1, 2, 3])}
    expected_normalized_array = np.array([0.5, 1, 1.5])
    task_func(my_dict)
    assert np.allclose(my_dict['normalized_array'], expected_normalized_array)