python
import pandas as pd
import numpy as np
import itertools

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
    result = task_func()
    expected_result = pd.DataFrame([np.nan, 2.1, 3.2, 4.3, 5.4], columns=['Mean Value'], 
                                   index=['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4'])
    assert result.equals(expected_result)

    # Test case 2: Test with custom data_list
    custom_data_list = [('a', 1, 2.1), ('b', 2, 3.2), ('c', 3, 4.3), ('d', 4, 5.4), ('e', 5, '6.5')]
    result = task_func(custom_data_list)
    expected_result = pd.DataFrame([np.nan, 2.1, 3.2, 4.3, np.nan], columns=['Mean Value'], 
                                   index=['Position 0', 'Position 1', 'Position 2', 'Position 3', 'Position 4'])
    assert result.equals(expected_result)