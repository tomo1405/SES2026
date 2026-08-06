python
import numpy as np
import pytest
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
    with pytest.raises(ValueError):
        task_func([])
    assert task_func([1, 2, 3, 4, 5]) == {'array': np.array([1, 2, 3, 4, 5]), 'mode': 1, 'entropy': 2.321928094887362}
    assert task_func([1, 1, 2, 2, 3, 3]) == {'array': np.array([1, 1, 2, 2, 3, 3]), 'mode': 1, 'entropy': 1.560964047443681}
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == {'array': np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 'mode': 1, 'entropy': 3.321928094887362}