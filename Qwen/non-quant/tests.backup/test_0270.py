import pytest
from src_0270 import task_func
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple dictionary
    data_dict = {'b': 2, 'c': 3}
    result_dict, stats_dict, ax = task_func(data_dict)

    # Check if the key 'a' is added with value 1
    assert 'a' in result_dict and result_dict['a'] == 1

    # Check if the values are correctly converted to a numpy array
    values = np.array([2, 3, 1])
    assert np.array_equal(result_dict.values(), values)

    # Check if the mean is calculated correctly
    mean = round(np.mean(values), 2)
    assert stats_dict['mean'] == mean

    # Check if the median is calculated correctly
    median = np.median(values)
    assert stats_dict['median'] == median

    # Check if the mode is calculated correctly
    mode_value, _ = stats.mode(values)
    assert stats_dict['mode'] == mode_value

    # Check if the values are normalized correctly
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_values = scaler.fit_transform(values.reshape(-1, 1)).flatten()
    assert np.allclose(normalized_values, ax.patches[0].get_height() * 0.1)

    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Histogram of Normalized Values"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"

# Run the tests
if __name__ == "__main__":
    pytest.main()