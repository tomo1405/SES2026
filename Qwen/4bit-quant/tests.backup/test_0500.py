import pytest
from src_0500 import task_func
import os
import tempfile

def test_task_func():
    # Prepare test data
    csv_content = "name,age\nAlice,30\nBob,25"
    expected_output = "output.xls"

    # Create a temporary directory to save the file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Construct the full path for the output file
        full_path = os.path.join(temp_dir, expected_output)

        # Call the function
        result = task_func(csv_content, full_path)

        # Check if the file was created and the path is correct
        assert os.path.exists(result)
        assert result == os.path.abspath(full_path)

        # Verify the content of the Excel file
        import xlrd
        workbook = xlrd.open_workbook(full_path)
        sheet = workbook.sheet_by_index(0)

        # Check the first row (header)
        assert sheet.cell_value(0, 0) == "name"
        assert sheet.cell_value(0, 1) == "age"

        # Check the second row
        assert sheet.cell_value(1, 0) == "Alice"
        assert sheet.cell_value(1, 1) == 30

        # Check the third row
        assert sheet.cell_value(2, 0) == "Bob"
        assert sheet.cell_value(2, 1) == 25

# Run the test
if __name__ == "__main__":
    pytest.main()