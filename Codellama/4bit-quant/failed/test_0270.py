import pytest
from src_0270 import task_func

def test_task_func():
    # Test that the function returns a dictionary
    data_dict = {"a": 1, "b": 2, "c": 3}
    result, stats, ax = task_func(data_dict)
    assert isinstance(result, dict)

    # Test that the function adds the key 'a' with value 1
    assert result["a"] == 1

    # Test that the function converts the values to a numpy array
    values = np.array(list(data_dict.values()))
    assert np.array_equal(values, result.values())

    # Test that the function performs statistical analysis
    mean = round(np.mean(values), 2)
    median = np.median(values)
    mode_value, _ = stats.mode(values)
    assert stats["mean"] == mean
    assert stats["median"] == median
    assert stats["mode"] == mode_value

    # Test that the function normalizes the values
    scaler = MinMaxScaler(feature_range=SCALER_RANGE)
    normalized_values = scaler.fit_transform(values.reshape(-1, 1))
    assert np.array_equal(normalized_values, result.values())

    # Test that the function plots a histogram of the normalized values
    fig, ax = plt.subplots()
    ax.hist(normalized_values, bins=10, edgecolor='black')
    ax.set_title("Histogram of Normalized Values")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    assert ax.get_title() == "Histogram of Normalized Values"
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"

    # Test that the function returns the correct statistical analysis
    assert result["mean"] == mean
    assert result["median"] == median
    assert result["mode"] == mode_value