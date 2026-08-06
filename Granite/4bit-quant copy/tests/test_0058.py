import pytest
from src_0058 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    title = "Correlation Heatmap"
    corr, ax = task_func(csv_file_path, title)
    assert isinstance(corr, pd.DataFrame), "Expected a DataFrame, but got a different type"
    assert ax.get_title() == title, "Expected the title to be {}, but got {}".format(title, ax.get_title())