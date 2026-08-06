python
import pytest
from src_1047 import task_func

def test_task_func():
    # Test case 1: Valid input
    date_str = "2022-01-01"
    expected_df = pd.DataFrame(
        [
            ["John", datetime(2022, 1, 1, 0, 0)],
            ["Alice", datetime(2022, 1, 1, 0, 0)],
            ["Bob", datetime(2022, 1, 1, 0, 0)],
            ["Charlie", datetime(2022, 1, 1, 0, 0)],
            ["Dave", datetime(2022, 1, 1, 0, 0)],
        ],
        columns=["Employee", "Date"],
    )
    actual_df = task_func(date_str)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid input (not a date string)
    date_str = "2022-13-32"
    with pytest.raises(ValueError):
        task_func(date_str)