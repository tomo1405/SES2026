import pytest
from src_0270 import task_func

def test_task_func():
    data_dict = {"a": 1, "b": 2, "c": 3}
    expected_dict = {"a": 1, "b": 2, "c": 3}
    expected_mean = 2
    expected_median = 2
    expected_mode = 1

    output_dict, output_stats, output_ax = task_func(data_dict)

    assert output_dict == expected_dict
    assert output_stats["mean"] == expected_mean
    assert output_stats["median"] == expected_median
    assert output_stats["mode"] == expected_mode
    assert output_ax.get_title() == "Histogram of Normalized Values"
    assert output_ax.get_xlabel() == "Value"
    assert output_ax.get_ylabel() == "Frequency"

if __name__ == "__main__":
    pytest.main()