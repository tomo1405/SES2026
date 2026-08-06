import pytest
from src_0375 import task_func
import os
import tempfile
import shutil
from openpyxl import Workbook

@pytest.fixture
def setup_test_directory():
    test_dir = tempfile.mkdtemp()
    yield test_dir
    shutil.rmtree(test_dir)

@pytest.fixture
def create_test_xlsx_files(test_dir):
    wb1 = Workbook()
    ws1 = wb1.active
    ws1['A1'] = 'Test "String"'
    wb1.save(os.path.join(test_dir, 'test1.xlsx'))

    wb2 = Workbook()
    ws2 = wb2.active
    ws2['A1'] = 'Another "Test" String'
    wb2.save(os.path.join(test_dir, 'test2.xlsx'))

@pytest.mark.usefixtures("setup_test_directory", "create_test_xlsx_files")
def test_task_func(setup_test_directory):
    processed_files = task_func(setup_test_directory)
    assert processed_files == 2

    # Check if files are modified
    for file_name in ['test1.xlsx', 'test2.xlsx']:
        workbook = load_workbook(filename=os.path.join(setup_test_directory, file_name))
        for sheet in workbook.sheetnames:
            for row in workbook[sheet].iter_rows():
                for cell in row:
                    if isinstance(cell.value, str):
                        assert '"' not in cell.value, f'Unescaped quote found in {file_name}'

@pytest.mark.usefixtures("setup_test_directory")
def test_task_func_non_existent_directory(setup_test_directory):
    with pytest.raises(FileNotFoundError):
        task_func(os.path.join(setup_test_directory, 'non_existent_dir'))