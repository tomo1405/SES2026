import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pytest

from src_0759 import task_func

@pytest.fixture
def input_args():
    return {
        'num_samples': 100,
        'countries': ['Russia', 'China', 'USA', 'India', 'Brazil'], 
        'ages': np.arange(18, 60), 
        'genders': ['Male', 'Female'], 
        'rng_seed': 42
    }

def test_task_func_input_types(input_args):
    result = task_func(**input_args)
    assert isinstance(result, pd.DataFrame)

def test_task_func_num_samples(input_args):
    input_args['num_samples'] = 'not_an_int'
    with pytest.raises(ValueError) as exc_info:
        task_func(**input_args)
    assert 'num_samples should be an integer.' in str(exc_info.value)

def test_task_func_output_values(input_args):
    result = task_func(**input_args)
    assert len(result) == input_args['num_samples']
    assert set(result['Country'].unique()) == set(input_args['countries'])
    assert set(result['Age'].unique()) == set(input_args['ages'])
    assert set(result['Gender'].unique()) == set([0, 1])