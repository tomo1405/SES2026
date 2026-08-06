import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(data_dict, data_keys):
    # Extract and transform the data for the specified keys
    data_for_keys = {key: data_dict[key] for key in data_keys if key in data_dict}
    df = pd.DataFrame(data_for_keys)

    # Check if DataFrame is empty (i.e., no keys matched)
    if df.empty:
        raise ValueError("No matching keys found in data dictionary, or keys list is empty.")

    # Apply MinMax normalization
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(normalized_data, columns=data_keys)

    # Plot the normalized data
    ax = normalized_df.plot(kind='line')
    ax.set_title('Normalized Data')
    ax.set_ylabel('Normalized Value')
    ax.set_xlabel('Index')

    return normalized_df, ax

def test_task_func():
    data_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}
    data_keys = ['key1', 'key2']

    # Test if the function raises a ValueError when no matching keys are found
    with pytest.raises(ValueError):
        task_func(data_dict, ['key4', 'key5'])

    # Test if the function returns the expected output when matching keys are found
    normalized_df, ax = task_func(data_dict, data_keys)
    assert isinstance(normalized_df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)