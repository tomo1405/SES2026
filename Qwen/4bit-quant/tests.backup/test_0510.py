import pytest
from src_0510 import task_func

def test_task_func_with_identical_files(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    
    content = "name,age\nAlice,30\nBob,25"
    
    file1.write_text(content)
    file2.write_text(content)
    
    result_df = task_func(str(file1), str(file2))
    assert result_df.empty, "The files are identical, so the DataFrame should be empty."

def test_task_func_with_different_files(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    
    content1 = "name,age\nAlice,30\nBob,25"
    content2 = "name,age\nAlice,30\nCharlie,35"
    
    file1.write_text(content1)
    file2.write_text(content2)
    
    result_df = task_func(str(file1), str(file2))
    assert not result_df.empty, "The files are different, so the DataFrame should not be empty."
    assert result_df.shape == (1, 3), "There should be one difference in the files."
    assert result_df.iloc[0]['Status'] == '+', "The second file has an additional line."

def test_task_func_with_empty_file(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    
    content1 = ""
    content2 = "name,age\nAlice,30\nBob,25"
    
    file1.write_text(content1)
    file2.write_text(content2)
    
    with pytest.raises(ValueError, match="The file '.*' is empty."):
        task_func(str(file1), str(file2))

def test_task_func_with_missing_file(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    
    content1 = "name,age\nAlice,30\nBob,25"
    
    file1.write_text(content1)
    
    with pytest.raises(FileNotFoundError, match="File not found: .*"):
        task_func(str(file1), str(file2))

def test_task_func_with_different_delimiters(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    
    content1 = "name;age\nAlice;30\nBob;25"
    content2 = "name,age\nAlice,30\nCharlie,35"
    
    file1.write_text(content1)
    file2.write_text(content2)
    
    result_df = task_func(str(file1), str(file2), delimiter=';')
    assert not result_df.empty, "The files are different due to delimiters, so the DataFrame should not be empty."
    assert result_df.shape == (1, 3), "There should be one difference in the files."
    assert result_df.iloc[0]['Status'] == '+', "The second file has an additional line."

def test_task_func_with_quotechars(tmp_path):
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    
    content1 = 'name,"age"\nAlice,"30"\nBob,"25"'
    content2 = 'name,"age"\nAlice,"30"\nCharlie,"35"'
    
    file1.write_text(content1)
    file2.write_text(content2)
    
    result_df = task_func(str(file1), str(file2), quotechar='"')
    assert not result_df.empty, "The files are different, so the DataFrame should not be empty."
    assert result_df.shape == (1, 3), "There should be one difference in the files."
    assert result_df.iloc[0]['Status'] == '+', "The second file has an additional line."