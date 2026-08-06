import pytest
from src_0362 import task_func
import pandas as pd
import logging

# Set up logging for testing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_task_func():
    # Test case 1: Normal case
    result = task_func("Sheet1")
    assert isinstance(result, dict), "The result should be a dictionary"
    assert len(result) > 0, "The result dictionary should not be empty"

    # Test case 2: File not found
    with pytest.raises(FileNotFoundError):
        task_func("NonExistentSheet")

    # Test case 3: Handling ValueError
    with pytest.raises(ValueError):
        task_func("Sheet1", excel_file_location="non_existent_file.xlsx")

    # Test case 4: Check logging
    with pytest.raises(FileNotFoundError):
        task_func("Sheet1", excel_file_location="non_existent_file.xlsx")

    # Additional test cases can be added as needed

if __name__ == "__main__":
    pytest.main()