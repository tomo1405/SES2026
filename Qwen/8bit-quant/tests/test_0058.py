import pytest
from src_0058 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_csv_file(tmpdir):
    csv_content = """A,B,C
1,2,3
4,5,6
7,8,9"""
    p = tmpdir.join("sample.csv")
    p.write(csv_content)
    return str(p)

def test_task_func(sample_csv_file):
    title = "Sample Correlation Heatmap"
    corr_matrix, ax = task_func(sample_csv_file, title)
    
    # Check if the correlation matrix is correct
    expected_corr_matrix = pd.DataFrame({
        'A': [1.00, 1.00, 1.00],
        'B': [1.00, 1.00, 1.00],
        'C': [1.00, 1.00, 1.00]
    }, index=['A', 'B', 'C'])
    pd.testing.assert_frame_equal(corr_matrix, expected_corr_matrix)
    
    # Check if the plot has the correct title
    assert ax.get_title() == title
    
    # Check if the plot is a heatmap
    assert isinstance(ax.collections[0], plt.matplotlib.collections.QuadMesh)

# Clean up the plot after testing
@pytest.fixture(autouse=True)
def cleanup():
    plt.close('all')