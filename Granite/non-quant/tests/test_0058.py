import pytest
from src_0058 import task_func


@pytest.mark.parametrize("csv_file_path, title, expected_output", [
    ("path/to/csv_file.csv", "Correlation Heatmap", expected_corr_object),
    ("path/to/another_csv_file.csv", "Another Title", expected_corr_object),
])
def test_task_func(csv_file_path, title, expected_output):
    corr, ax = task_func(csv_file_path, title)
    assert corr == expected_output
    assert ax == expected_ax_object