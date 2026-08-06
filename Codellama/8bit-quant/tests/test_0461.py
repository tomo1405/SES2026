import pytest
from src_0461 import task_func

def test_task_func_valid_input():
    script_path = "path/to/script.py"
    output_file_path = "path/to/output.csv"
    df, ax = task_func(script_path, output_file_path)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_input():
    script_path = "path/to/script.py"
    output_file_path = "path/to/output.csv"
    with pytest.raises(ValueError):
        task_func(script_path, output_file_path)