python
import pandas as pd
import numpy as np
import itertools
import pytest

def task_func(data_list=[('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]):

    # Unzip the data, filling missing values with NaN so they don't affect the mean calculation
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))

    # Calculate the mean of numerical values, skipping the first column assuming it's non-numerical
    # Filter out non-numeric values from the column before calculating the mean
    mean_values = []
    for column in unzipped_data[:]:
        numeric_values = [val for val in column if isinstance(val, (int, float))]
        if numeric_values:
            mean_values.append(np.nanmean(numeric_values))
        else:
            mean_values.append(np.nan)

    # Create a DataFrame with the results
    df = pd.DataFrame(mean_values, columns=['Mean Value'], 
                      index=['Position {}'.format(i) for i in range(len(mean_values))])

    return df

def test_task_func():
    # Test case 1: Test with default data_list
    assert task_func().equals(pd.DataFrame({'Mean Value': [2.1, 3.2, 4.3, 5.4, 6.5]}, 
                                            index=['Position {}'.format(i) for i in range(5)]))

    # Test case 2: Test with custom data_list
    assert task_func([('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5), ('f', 6, 7.6)]).equals(pd.DataFrame({'Mean Value': [2.1, 3.2, 4.3, 5.4, 6.5, np.nan]}, 
                                                                                                                                index=['Position {}'.format(i) for i in range(6)]))

    # Test case 3: Test with empty data_list
    assert task_func([]).empty

    # Test case 4: Test with non-list data_list
    with pytest.raises(TypeError):
        task_func('not a list')