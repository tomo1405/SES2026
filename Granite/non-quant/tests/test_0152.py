import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(data_dict, data_keys):
    data_for_keys = {key: data_dict[key] for key in data_keys if key in data_dict}
    df = pd.DataFrame(data_for_keys)

    if df.empty:
        raise ValueError("No matching keys found in data dictionary, or keys list is empty.")

    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df)
    normalized_df = pd.DataFrame(normalized_data, columns=data_keys)

    ax = normalized_df.plot(kind='line')
    ax.set_title('Normalized Data')
    ax.set_ylabel('Normalized Value')
    ax.set_xlabel('Index')

    return normalized_df, ax

def test_task_func():
    data_dict = {'key1': [1, 2, 3], 'key2': [4, 5, 6], 'key3': [7, 8, 9]}
    data_keys = ['key1', 'key2']

    expected_normalized_df = pd.DataFrame([[0.0, 0.5], [0.5, 1.0], [1.0, 1.5]], columns=['key1', 'key2'])
    expected_ax_title = 'Normalized Data'
    expected_ax_ylabel = 'Normalized Value'
    expected_ax_xlabel = 'Index'

    normalized_df, ax = task_func(data_dict, data_keys)

    assert normalized_df.equals(expected_normalized_df)
    assert ax.get_title() == expected_ax_title
    assert ax.get_ylabel() == expected_ax_ylabel
    assert ax.get_xlabel() == expected_ax_xlabel

if __name__ == '__main__':
    pytest.main()