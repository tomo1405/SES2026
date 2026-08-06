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
    # Test with default data_list
    assert task_func() == pd.DataFrame([np.nan, 2.1, 3.2, 4.3, 5.4], columns=['Mean Value'], 
                                        index=['Position {}'.format(i) for i in range(5)])

    # Test with custom data_list
    assert task_func([('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, 6.5)]) == pd.DataFrame([2.1, 3.2, 4.3, 5.4], columns=['Mean Value'], 
                                                                                                                    index=['Position {}'.format(i) for i in range(4)])