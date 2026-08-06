import csv

from src_0772 import task_func


def test_task_func_no_matching_files(tmp_path):
    # Create a temporary directory and add some files that do not match the pattern
    (tmp_path / "file1.txt").touch()
    (tmp_path / "file2.docx").touch()
    
    result = task_func(str(tmp_path))
    
    assert result == []

def test_task_func_with_matching_files(tmp_path):
    # Create a temporary directory and add some files that match the pattern
    (tmp_path / "data-1.csv").touch()
    (tmp_path / "info-2.csv").touch()
    
    result = task_func(str(tmp_path))
    
    assert set(result) == {"data.csv", "info.csv"}
    assert (tmp_path / "data.csv").exists()
    assert (tmp_path / "info.csv").exists()

def test_task_func_with_empty_directory(tmp_path):
    # Create an empty temporary directory
    result = task_func(str(tmp_path))
    
    assert result == []

def test_task_func_with_nested_files(tmp_path):
    # Create a temporary directory with nested directories and files
    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()
    (nested_dir / "subdata-1.csv").touch()
    
    result = task_func(str(tmp_path))
    
    assert result == []

def test_task_func_with_non_csv_files(tmp_path):
    # Create a temporary directory with non-csv files that match the pattern
    (tmp_path / "data-1.csv").write_text("header1,header2\nvalue1,value2")
    (tmp_path / "info-2.csv").write_text("header3,header4\nvalue3,value4")
    
    result = task_func(str(tmp_path))
    
    assert set(result) == {"data.csv", "info.csv"}
    with open(tmp_path / "data.csv", 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert rows == [['header1', 'header2'], ['value1', 'value2']]
    
    with open(tmp_path / "info.csv", 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    assert rows == [['header3', 'header4'], ['value3', 'value4']]

def test_task_func_with_custom_pattern(tmp_path):
    # Create a temporary directory and add some files that match a custom pattern
    (tmp_path / "custom-data-1.csv").touch()
    (tmp_path / "custom-info-2.csv").touch()
    
    result = task_func(str(tmp_path), pattern=r'^custom-(.*?)-\d+\.csv$')
    
    assert set(result) == {"data.csv", "info.csv"}