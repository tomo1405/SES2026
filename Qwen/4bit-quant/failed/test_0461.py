import pytest
from src_0461 import task_func
import os
import pandas as pd

@pytest.fixture
def create_temp_files(tmpdir):
    # Create a temporary script that writes a CSV file
    script_content = """
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
"""
    script_path = tmpdir.join("temp_script.py")
    script_path.write(script_content)

    output_file_path = tmpdir.join("output.csv")

    return str(script_path), str(output_file_path)

def test_task_func(create_temp_files):
    script_path, output_file_path = create_temp_files

    # Run the function
    df, ax = task_func(script_path, output_file_path)

    # Check if the DataFrame has the correct content
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    pd.testing.assert_frame_equal(df, expected_df)

    # Check if the plot is created correctly
    assert ax.get_xlabel() == 'A'
    assert len(ax.patches) == 6  # 3 bars for each column in the DataFrame

def test_task_func_script_error(tmpdir):
    script_path = tmpdir.join("non_existent_script.py")
    output_file_path = tmpdir.join("output.csv")

    with pytest.raises(ValueError, match="Error occurred while executing the script or script not found"):
        task_func(str(script_path), str(output_file_path))

def test_task_func_csv_format_error(create_temp_files):
    script_path, output_file_path = create_temp_files

    # Modify the script to write a CSV with more than 2 columns
    script_content = """
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)
"""
    script_path.write(script_content)

    with pytest.raises(ValueError, match="CSV file must contain exactly 2 columns"):
        task_func(str(script_path), str(output_file_path))