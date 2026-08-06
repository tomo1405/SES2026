import pytest
from src_0948 import task_func

def test_task_func():
    # Test case 1: Default arguments
    result = task_func()
    expected = np.array([[np.datetime64('2021-01-01'), np.datetime64('2021-01-02')],
                         [np.datetime64('2021-01-03'), np.datetime64('2021-01-04')],
                         [np.datetime64('2021-01-05'), np.datetime64('2021-01-06')]])
    assert np.array_equal(result, expected)

    # Test case 2: Custom arguments
    result = task_func(rows=2, columns=3, start_date=datetime(2022, 1, 1), end_date=datetime(2022, 12, 31), seed=1)
    expected = np.array([[np.datetime64('2022-01-01'), np.datetime64('2022-01-02'), np.datetime64('2022-01-03')],
                         [np.datetime64('2022-01-04'), np.datetime64('2022-01-05'), np.datetime64('2022-01-06')]])
    assert np.array_equal(result, expected)