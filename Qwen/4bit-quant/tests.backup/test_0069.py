import pytest
from src_0069 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'Employee ID': ['EMP123', 'EMP456', 'XYZ789', 'EMP789'],
        'Age': [28, 34, 45, 30]
    }
    return pd.DataFrame(data)

def test_task_func_with_valid_data(sample_data, tmpdir):
    # Create a temporary CSV file
    temp_file = tmpdir.join("temp_data.csv")
    sample_data.to_csv(temp_file, index=False)

    # Call the function with the temporary file
    df, ax = task_func(str(temp_file), 'EMP')

    # Check if the returned DataFrame is filtered correctly
    assert all(df['Employee ID'].str.startswith('EMP'))

    # Check if the plot is created
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_prefix(sample_data, tmpdir):
    # Create a temporary CSV file
    temp_file = tmpdir.join("temp_data.csv")
    sample_data.to_csv(temp_file, index=False)

    # Call the function with an invalid prefix
    df, ax = task_func(str(temp_file), 'XYZ')

    # Check if the returned DataFrame is empty
    assert df.empty

    # Check if the plot is created
    assert isinstance(ax, plt.Axes)

def test_task_func_with_nonexistent_file():
    # Call the function with a non-existent file path
    with pytest.raises(FileNotFoundError):
        task_func('/path/to/nonexistent.csv', 'EMP')