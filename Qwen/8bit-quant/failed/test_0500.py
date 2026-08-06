import pytest
from src_0500 import task_func
import os
import tempfile

def test_task_func():
    # Test data
    csv_content = "name,age\nAlice,30\nBob,25"
    filename = "test_output.xls"

    # Create a temporary directory to store the output file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Construct the full path for the output file
        full_path = os.path.join(temp_dir, filename)

        # Call the function
        result = task_func(csv_content, full_path)

        # Check if the function returns the correct absolute path
        assert result == os.path.abspath(full_path)

        # Check if the file exists
        assert os.path.exists(full_path)

        # Open the Excel file and check its contents
        import xlrd
        workbook = xlrd.open_workbook(full_path)
        sheet = workbook.sheet_by_name("sheet1")

        # Check the number of rows and columns
        assert sheet.nrows == 3
        assert sheet.ncols == 2

        # Check the content of the first row
        assert sheet.cell_value(0, 0) == "name"
        assert sheet.cell_value(0, 1) == "age"

        # Check the content of the second row
        assert sheet.cell_value(1, 0) == "Alice"
        assert sheet.cell_value(1, 1) == 30

        # Check the content of the third row
        assert sheet.cell_value(2, 0) == "Bob"
        assert sheet.cell_value(2, 1) == 25

# Run the test
if __name__ == "__main__":
    pytest.main()