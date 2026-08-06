import pytest
from src_0021 import task_func
import pandas as pd
import ast
import seaborn as sns

# Mocking the seaborn pairplot function to avoid actual plotting
def mock_pairplot(*args, **kwargs):
    return "Mocked Axes"

sns.pairplot = mock_pairplot

def test_task_func_with_valid_csv(tmp_path):
    # Create a temporary CSV file with sample data
    csv_content = """dict_column
{"key": "value"}
{"another_key": "another_value"}"""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(csv_content)

    # Call the function
    df, ax = task_func(str(csv_file))

    # Check if the DataFrame is correctly loaded
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "dict_column" in df.columns
    assert "hue_column" in df.columns

    # Check if 'dict_column' is converted to dictionary
    assert isinstance(df.iloc[0]["dict_column"], dict)
    assert df.iloc[0]["dict_column"] == {"key": "value"}

    # Check if 'hue_column' is string representation of 'dict_column'
    assert df.iloc[0]["hue_column"] == str({"key": "value"})

    # Check if the mocked pairplot is returned
    assert ax == "Mocked Axes"

def test_task_func_with_invalid_csv(tmp_path):
    # Create a temporary CSV file with invalid data
    csv_content = """dict_column
invalid_dict
{"another_key": "another_value"}"""
    csv_file = tmp_path / "invalid_sample.csv"
    csv_file.write_text(csv_content)

    # Call the function and expect it to raise an exception
    with pytest.raises(ValueError):
        task_func(str(csv_file))