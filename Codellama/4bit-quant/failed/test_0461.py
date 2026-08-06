import pytest
from src_0461 import task_func

def test_task_func():
    script_path = "path/to/script.py"
    output_file_path = "path/to/output.csv"

    # Test that the function raises an error if the script is not found
    with pytest.raises(FileNotFoundError):
        task_func(script_path, output_file_path)

    # Test that the function raises an error if the script raises an error
    with pytest.raises(subprocess.CalledProcessError):
        task_func(script_path, output_file_path)

    # Test that the function returns a DataFrame and an Axes object
    df, ax = task_func(script_path, output_file_path)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test that the DataFrame has exactly 2 columns
    assert len(df.columns) == 2

    # Test that the Axes object has the correct x-label
    assert ax.get_xlabel() == df.columns[0]