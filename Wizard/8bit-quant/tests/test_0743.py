python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0743 import task_func

def test_task_func():
    # Test case 1: Empty input array
    with pytest.raises(Exception):
        task_func([])

    # Test case 2: Non-numeric values
    with pytest.raises(ValueError):
        task_func([('A', 'B'), ('C', 'D'), ('E', 'F')])

    # Test case 3: Valid input array
    input_array = [('A', 1), ('B', 2), ('C', 3)]
    expected_output = pd.DataFrame(input_array, columns=['Category', 'Value'])
    expected_output['Value'] = MinMaxScaler().fit_transform(expected_output[['Value']])
    assert task_func(input_array).equals(expected_output)