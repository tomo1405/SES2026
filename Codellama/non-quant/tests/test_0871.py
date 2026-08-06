import pandas as pd
from src_0871 import task_func


def test_task_func():
    # Test case 1: Test with a list of tuples
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]
    expected_output = pd.DataFrame({'Mean Value': [2.1, 3.2, 4.3, 5.4, 6.5]}, 
                                  index=['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4'])
    assert task_func(data_list) == expected_output

    # Test case 2: Test with a list of tuples with missing values
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5), ('f', np.nan, np.nan)]
    expected_output = pd.DataFrame({'Mean Value': [2.1, 3.2, 4.3, 5.4, 6.5, np.nan]}, 
                                  index=['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4', 'Position 5'])
    assert task_func(data_list) == expected_output

    # Test case 3: Test with a list of tuples with non-numerical values
    data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5), ('f', 'non-numerical', np.nan)]
    expected_output = pd.DataFrame({'Mean Value': [2.1, 3.2, 4.3, 5.4, 6.5, np.nan]}, 
                                  index=['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4', 'Position 5'])
    assert task_func(data_list) == expected_output