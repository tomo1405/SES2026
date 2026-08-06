import pytest
from src_0342 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Test cases for task_func

def test_task_func_valid_input():
    # Create a sample DataFrame
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': ['A', 'B', 'C', 'D', 'E']
    }
    df = pd.DataFrame(data)
    
    # Call the function with the sample DataFrame
    fig = task_func(df, 'col1')
    
    # Add assertions to verify the output
    assert fig is not None
    plt.close(fig)

def test_task_func_invalid_input():
    # Test with invalid input (empty DataFrame)
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df, 'non_existent_column')