import pytest
from src_0500 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define CSV content and expected file path
        csv_content = "name,age\nAlice,30\nBob,25"
        filename = os.path.join(temp_dir, "test_output.xls")
        
        # Call the function
        result_path = task_func(csv_content, filename)
        
        # Check if the file exists
        assert os.path.exists(result_path)
        
        # Check if the returned path is absolute
        assert os.path.isabs(result_path)
        
        # Verify the content of the generated Excel file
        import xlrd
        workbook = xlrd.open_workbook(result_path)
        sheet = workbook.sheet_by_name("sheet1")
        
        # Check number of rows and columns
        assert sheet.nrows == 3
        assert sheet.ncols == 2
        
        # Check specific cell values
        assert sheet.cell_value(0, 0) == "name"
        assert sheet.cell_value(0, 1) == "age"
        assert sheet.cell_value(1, 0) == "Alice"
        assert sheet.cell_value(1, 1) == 30
        assert sheet.cell_value(2, 0) == "Bob"
        assert sheet.cell_value(2, 1) == 25

# Run the tests
if __name__ == "__main__":
    pytest.main()