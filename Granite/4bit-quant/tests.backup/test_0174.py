import pytest
import numpy as np
import pandas as pd
from src_0174 import task_func

def test_task_func():
    # Test case 1: empty country_dict
    country_dict = {}
    expected_output = pd.DataFrame(columns=['GDP'])
    actual_output = task_func(country_dict)
    assert actual_output.equals(expected_output)

    # Test case 2: one country in country_dict
    country_dict = {'USA': 'USA'}
    expected_output = pd.DataFrame({'USA': [np.random.randint(1000000000, 100000000000, dtype=np.int64)]}, index=['USA'], columns=['GDP'])
    actual_output = task_func(country_dict)
    assert actual_output.equals(expected_output)

    # Test case 3: multiple countries in country_dict
    country_dict = {'USA': 'USA', 'China': 'China', 'Japan': 'Japan'}
    expected_output = pd.DataFrame({'USA': [np.random.randint(1000000000, 100000000000, dtype=np.int64)],
                                   'China': [np.random.randint(1000000000, 100000000000, dtype=np.int64)],
                                   'Japan': [np.random.randint(1000000000, 100000000000, dtype=np.int64)]},
                                  index=['USA', 'China', 'Japan'], columns=['GDP'])
    actual_output = task_func(country_dict)
    assert actual_output.equals(expected_output)