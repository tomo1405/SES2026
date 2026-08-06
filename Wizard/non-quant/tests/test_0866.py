python
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def task_func(data):
    # Extracting items, counts, and weights from the input data
    items, counts, weights = zip(*data)
    
    # Normalizing the counts and weights
    counts_normalized = zscore(counts)
    scaler = MinMaxScaler()
    weights_normalized = scaler.fit_transform(np.array(weights).reshape(-1, 1)).flatten()

    # Creating a DataFrame with the normalized data
    report_df = pd.DataFrame({
        'Item': items,
        'Normalized Count': counts_normalized,
        'Normalized Weight': weights_normalized
    })

    return report_df

# Testing the function
def test_task_func():
    # Creating a sample input data
    data = [('item1', 10, 2), ('item2', 5, 1), ('item3', 15, 3)]

    # Calling the function and storing the result in a variable
    result = task_func(data)

    # Creating a sample expected output data
    expected_output = pd.DataFrame({
        'Item': ['item1', 'item2', 'item3'],
        'Normalized Count': [-1.3416407864998738, 0.0, 1.3416407864998738],
        'Normalized Weight': [0.0, 0.0, 1.0]
    })

    # Comparing the result with the expected output
    assert result.equals(expected_output)

# Running the test function
test_task_func()