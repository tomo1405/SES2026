python
import subprocess
import pandas as pd
import pytest

from src_0461 import task_func

def test_task_func():
    # Test case 1: Valid script and output file path
    script_path = "script.py"
    output_file_path = "output.csv"
    df, ax = task_func(script_path, output_file_path)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 2: Invalid script path
    with pytest.raises(ValueError):
        task_func("invalid_script.py", output_file_path)

    # Test case 3: Invalid output file path
    with pytest.raises(ValueError):
        task_func(script_path, "invalid_output.csv")

    # Test case 4: Output file does not contain exactly 2 columns
    with open("output.csv", "w") as f:
        f.write("1,2,3\n4,5,6\n")
    with pytest.raises(ValueError):
        task_func(script_path, "output.csv")