import pytest
from src_0651 import task_func


def test_task_func_with_valid_input():
    date_str = "2022-01-01 00:00:00"
    tz_str = "America/New_York"
    expected_output = 82800

    output = task_func(date_str, tz_str)

    assert output == expected_output


def test_task_func_with_invalid_input():
    date_str = "2022-01-01 00:00:00"
    tz_str = "Invalid/Timezone"

    with pytest.raises(ValueError):
        task_func(date_str, tz_str)