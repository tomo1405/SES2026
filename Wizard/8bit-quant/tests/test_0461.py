python
import subprocess
import pandas as pd
import pytest

from src_0461 import task_func

def test_task_func_valid_script():
    script_path = "test_script.py"
    output_file_path = "output.csv"

    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")

    try:
        subprocess.run([script_path], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise ValueError(
            "Error occurred while executing the script or script not found"
        )

    df, ax = task_func(script_path, output_file_path)

    assert len(df.columns) == 2
    assert df.columns[0] == "Column 1"
    assert df.columns[1] == "Column 2"
    assert df.shape[0] == 1
    assert df.iloc[0, 0] == 1
    assert df.iloc[0, 1] == 2
    assert ax.get_xlabel() == "Column 1"

def test_task_func_invalid_script():
    script_path = "test_script.py"
    output_file_path = "output.csv"

    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")

    try:
        subprocess.run([script_path], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise ValueError(
            "Error occurred while executing the script or script not found"
        )

    with open(script_path, "w") as f:
        f.write("print('Invalid syntax!')")

    with pytest.raises(ValueError):
        task_func(script_path, output_file_path)

def test_task_func_invalid_csv():
    script_path = "test_script.py"
    output_file_path = "output.csv"

    with open(script_path, "w") as f:
        f.write("print('Hello, world!')")

    try:
        subprocess.run([script_path], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise ValueError(
            "Error occurred while executing the script or script not found"
        )

    with open(output_file_path, "w") as f:
        f.write("Column 1, Column 2\n1, 2, 3")

    with pytest.raises(ValueError):
        task_func(script_path, output_file_path)