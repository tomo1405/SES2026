python
import pytest
from src_0627 import task_func

@pytest.mark.parametrize("date_str, from_tz, expected_result", [
    ("2022-01-01 12:00:00", "America/New_York", "2022-01-01 06:00:00, America/New_York"),
    ("2022-07-01 12:00:00", "Europe/London", "2022-07-01 06:00:00, Europe/London"),
    ("2022-12-31 12:00:00", "Asia/Shanghai", "2022-12-31 08:00:00, Asia/Shanghai"),
    ("2023-05-15 12:00:00", "Asia/Tokyo", "2023-05-15 09:00:00, Asia/Tokyo"),
    ("2024-10-25 12:00:00", "Australia/Sydney", "2024-10-25 10:00:00, Australia/Sydney"),
])
def test_task_func(date_str, from_tz, expected_result):
    result = task_func(date_str, from_tz)
    assert result == expected_result