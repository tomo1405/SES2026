import pytest
from src_0438 import task_func
import pandas as pd
import os

def test_task_func():
    # Create a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    
    # Define a temporary file name
    temp_file_name = "temp_save.pkl"
    
    # Call the function
    result_df = task_func(df, file_name=temp_file_name)
    
    # Check if the returned DataFrame is equal to the original DataFrame
    assert result_df.equals(df), "The loaded DataFrame does not match the original DataFrame"
    
    # Check if the temporary file was deleted
    assert not os.path.exists(temp_file_name), "The temporary file was not deleted"

# Run the test
if __name__ == "__main__":
    pytest.main()