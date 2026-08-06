import pytest
from src_0501 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary directory to save the file
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "test_output.xls")
        
        # Sample data
        values = [
            {'ID': 1, 'Name': 'Alice', 'Age': 30},
            {'ID': 2, 'Name': 'Bob', 'Age': 25}
        ]
        
        # Expected output path
        expected_path = os.path.abspath(filename)
        
        # Call the function
        result = task_func(values, filename)
        
        # Check if the result is the expected path
        assert result == expected_path
        
        # Check if the file exists
        assert os.path.exists(result)
        
        # Additional checks can be added here to verify the content of the Excel file
        # For example, using a library like openpyxl to read and verify the contents

# Run the test
if __name__ == "__main__":
    pytest.main()