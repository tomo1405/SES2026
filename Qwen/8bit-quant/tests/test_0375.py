import glob
import os

import pytest
from openpyxl import Workbook
from src_0375 import task_func


def test_task_func_directory_not_exists():
    with pytest.raises(FileNotFoundError):
        task_func(directory_path='./non_existent_dir/')

def test_task_func_no_xlsx_files():
    temp_dir = './temp_test_dir/'
    os.makedirs(temp_dir, exist_ok=True)
    assert task_func(directory_path=temp_dir) == 0
    os.rmdir(temp_dir)

def test_task_func_with_xlsx_files(tmpdir):
    # Create a temporary directory and add some xlsx files
    temp_dir = tmpdir.mkdir('xlsx_files')
    wb1 = Workbook()
    ws1 = wb1.active
    ws1['A1'] = 'Test "Quote"'
    wb1.save(os.path.join(temp_dir, 'test1.xlsx'))

    wb2 = Workbook()
    ws2 = wb2.active
    ws2['A1'] = 'Another "Quote"'
    wb2.save(os.path.join(temp_dir, 'test2.xlsx'))

    # Run the function
    processed_files = task_func(directory_path=str(temp_dir))

    # Check that the function processed the correct number of files
    assert processed_files == 2

    # Check that the quotes were escaped correctly
    for filename in glob.glob(os.path.join(temp_dir, '*.xlsx')):
        workbook = load_workbook(filename=filename)
        for sheet in workbook.sheetnames:
            for row in workbook[sheet].iter_rows():
                for cell in row:
                    if isinstance(cell.value, str):
                        assert cell.value == 'Test \"Quote\"' or cell.value == 'Another \"Quote\"'

# Clean up temporary files after tests
def pytest_sessionfinish(session, exitstatus):
    for root, dirs, files in os.walk('./temp_test_dir/', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    if os.path.exists('./temp_test_dir/'):
        os.rmdir('./temp_test_dir/')