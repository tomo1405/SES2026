import pytest
from src_0909 import task_func
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

# Mocking os.listdir to simulate directory contents
@patch('os.listdir')
# Mocking re.match to simulate pattern matching
@patch('re.match')
# Mocking plt.show to prevent actual plotting
@patch('matplotlib.pyplot.show')
def test_task_func(mock_show, mock_match, mock_listdir):
    # Define mock data
    mock_listdir.return_value = ['data1.csv', 'data2.csv', 'data3.txt']
    mock_match.side_effect = [True, False, True]
    
    # Create temporary CSV files with sample data
    temp_dir = 'temp_test_dir'
    os.makedirs(temp_dir, exist_ok=True)
    for i in range(1, 4):
        file_path = os.path.join(temp_dir, f'data{i}.csv')
        if i % 2 != 0:  # Only create CSV files that match the pattern
            df = pd.DataFrame({'Month': ['Jan', 'Feb'], 'Sales': [100, 200]})
            df.to_csv(file_path, index=False)
    
    # Run the function
    plots = task_func(temp_dir, r'.*\.csv')
    
    # Assertions
    assert len(plots) == 2, "The number of plots should be 2"
    assert all(isinstance(plot, plt.Axes) for plot in plots), "All items in the plots list should be of type plt.Axes"
    
    # Clean up temporary files and directory
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)

    # Ensure plt.show was called
    mock_show.assert_called_once()

# Run the test
if __name__ == "__main__":
    pytest.main()