import pytest
from src_0058 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@pytest.fixture
def sample_csv(tmpdir):
    # Create a sample CSV file for testing
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })
    csv_file = tmpdir.join("sample.csv")
    df.to_csv(csv_file, index=False)
    return str(csv_file)

def test_task_func(sample_csv):
    title = "Sample Correlation Heatmap"
    corr_matrix, ax = task_func(sample_csv, title)
    
    # Check if the correlation matrix is correct
    expected_corr = pd.DataFrame({
        'A': [1.0, 1.0, 1.0],
        'B': [1.0, 1.0, 1.0],
        'C': [1.0, 1.0, 1.0]
    }, index=['A', 'B', 'C'])
    pd.testing.assert_frame_equal(corr_matrix, expected_corr)
    
    # Check if the plot title is correct
    assert ax.get_title() == title
    
    # Check if the plot is a heatmap
    assert isinstance(ax.collections[0], plt.matplotlib.collections.QuadMesh)

def test_task_func_with_empty_data(tmpdir):
    # Create an empty CSV file for testing
    csv_file = tmpdir.join("empty.csv")
    csv_file.write("")
    
    with pytest.raises(pd.errors.EmptyDataError):
        task_func(str(csv_file), "Empty Data Heatmap")

def test_task_func_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent.csv", "Nonexistent File Heatmap")