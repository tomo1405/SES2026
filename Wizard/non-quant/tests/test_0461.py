python
import subprocess
import pandas as pd
import pytest

def task_func(script_path, output_file_path):
    try:
        subprocess.run([script_path], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise ValueError(
            "Error occurred while executing the script or script not found"
        )

    df = pd.read_csv(output_file_path)

    if len(df.columns) != 2:
        raise ValueError("CSV file must contain exactly 2 columns")

    ax = df.plot(kind="bar", x=df.columns[0], legend=False)
    ax.set_xlabel(df.columns[0])

    return df, ax

def test_task_func():
    # Test case 1: Valid input
    script_path = "script.py"
    output_file_path = "output.csv"
    df, ax = task_func(script_path, output_file_path)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)

    # Test case 2: Invalid input - script not found
    script_path = "invalid_script.py"
    output_file_path = "output.csv"
    with pytest.raises(ValueError):
        task_func(script_path, output_file_path)

    # Test case 3: Invalid input - output file not found
    script_path = "script.py"
    output_file_path = "invalid_output.csv"
    with pytest.raises(ValueError):
        task_func(script_path, output_file_path)

    # Test case 4: Invalid input - output file contains more than 2 columns
    script_path = "script.py"
    output_file_path = "output_invalid.csv"
    with open(output_file_path, "w") as f:
        f.write("col1,col2,col3\n1,2,3\n4,5,6\n")
    with pytest.raises(ValueError):
        task_func(script_path, output_file_path)