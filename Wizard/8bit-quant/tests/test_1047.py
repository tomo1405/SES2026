python
import pytest
from src_1047 import task_func

def test_task_func():
    # Test case 1
    date_str = "2022-01-01"
    expected_df = pd.DataFrame(
        [
            ["John", datetime.strptime("2022-01-01", "%Y-%m-%d")],
            ["Alice", datetime.strptime("2022-01-01", "%Y-%m-%d")],
            ["Bob", datetime.strptime("2022-01-01", "%Y-%m-%d")],
            ["Charlie", datetime.strptime("2022-01-01", "%Y-%m-%d")],
            ["Dave", datetime.strptime("2022-01-01", "%Y-%m-%d")],
        ],
        columns=["Employee", "Date"],
    )
    assert task_func(date_str).equals(expected_df)

    # Test case 2
    date_str = "2022-01-02"
    expected_df = pd.DataFrame(
        [
            ["John", datetime.strptime("2022-01-02", "%Y-%m-%d")],
            ["Alice", datetime.strptime("2022-01-02", "%Y-%m-%d")],
            ["Bob", datetime.strptime("2022-01-02", "%Y-%m-%d")],
            ["Charlie", datetime.strptime("2022-01-02", "%Y-%m-%d")],
            ["Dave", datetime.strptime("2022-01-02", "%Y-%m-%d")],
        ],
        columns=["Employee", "Date"],
    )
    assert task_func(date_str).equals(expected_df)

    # Test case 3
    date_str = "2022-01-03"
    expected_df = pd.DataFrame(
        [
            ["John", datetime.strptime("2022-01-03", "%Y-%m-%d")],
            ["Alice", datetime.strptime("2022-01-03", "%Y-%m-%d")],
            ["Bob", datetime.strptime("2022-01-03", "%Y-%m-%d")],
            ["Charlie", datetime.strptime("2022-01-03", "%Y-%m-%d")],
            ["Dave", datetime.strptime("2022-01-03", "%Y-%m-%d")],
        ],
        columns=["Employee", "Date"],
    )
    assert task_func(date_str).equals(expected_df)