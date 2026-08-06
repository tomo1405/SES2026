import pytest
from src_0362 import task_func
import pandas as pd
import os

@pytest.fixture
def create_test_excel(tmpdir):
    # Create a test Excel file with some data
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    excel_file_path = tmpdir.join("test.xlsx")
    df.to_excel(excel_file_path, sheet_name='Sheet1', index=False)
    return str(excel_file_path)

def test_task_func(create_test_excel, tmpdir):
    excel_file_location = create_test_excel
    csv_file_location = str(tmpdir.join("test.csv"))
    
    result = task_func(sheet_name='Sheet1', excel_file_location=excel_file_location, csv_file_location=csv_file_location)
    
    # Check if the CSV file was created
    assert os.path.exists(csv_file_location)
    
    # Check if the result is correct
    expected_result = {'A': 6, 'B': 15, 'C': 24}
    assert result == expected_result

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(sheet_name='Sheet1', excel_file_location='non_existent_file.xlsx')
    assert "Excel file not found at non_existent_file.xlsx" in str(excinfo.value)

def test_task_func_value_error(create_test_excel):
    # Introduce a value error by using an invalid sheet name
    excel_file_location = create_test_excel
    with pytest.raises(ValueError) as excinfo:
        task_func(sheet_name='InvalidSheet', excel_file_location=excel_file_location)
    assert "Error in processing Excel file" in str(excinfo.value)