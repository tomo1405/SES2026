python
import numpy as np
from scipy.stats import mode
from scipy.stats import entropy

def task_func(numbers):
    if len(numbers) == 0:
        raise ValueError
    my_dict = {'array': np.array(numbers)}
    mode_value = mode(my_dict['array']).mode[0]
    ent = entropy(my_dict['array'], base=2)
    my_dict['mode'] = mode_value
    my_dict['entropy'] = ent
    return my_dict

def test_task_func():
    # Test case 1: Empty list
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: List with one element
    assert task_func([1]) == {'array': np.array([1]), 'mode': 1, 'entropy': 0.0}

    # Test case 3: List with multiple elements
    assert task_func([1, 2, 3, 4, 5]) == {'array': np.array([1, 2, 3, 4, 5]), 'mode': 1, 'entropy': 2.32}