import pytest
from src_0115 import task_func

def test_task_func():
    my_dict = {"array": np.array([1, 2, 3, 4, 5])}
    expected_result = {"array": np.array([1, 2, 3, 4, 5]), "normalized_array": np.array([0., 0.2, 0.4, 0.6, 0.8])}
    result = task_func(my_dict)
    assert result == expected_result, "The function did not return the expected result."

def test_task_func_with_invalid_input():
    my_dict = {"array": [1, 2, 3, 4, 5]}
    with pytest.raises(TypeError):
        task_func(my_dict)