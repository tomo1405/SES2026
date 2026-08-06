import pytest
from src_0510 import task_func

def test_task_func_identical_files(tmpdir):
    file1 = tmpdir.join("file1.csv")
    file1.write("name,age\nAlice,30\nBob,25")

    file2 = tmpdir.join("file2.csv")
    file2.write("name,age\nAlice,30\nBob,25")

    result_df = task_func(str(file1), str(file2))
    assert result_df.empty

def test_task_func_different_files(tmpdir):
    file1 = tmpdir.join("file1.csv")
    file1.write("name,age\nAlice,30\nBob,25")

    file2 = tmpdir.join("file2.csv")
    file2.write("name,age\nAlice,31\nCharlie,25")

    result_df = task_func(str(file1), str(file2))
    expected_data = [
        [1, '-', 'Alice,30'],
        [1, '+', 'Alice,31'],
        [2, '-', 'Bob,25'],
        [3, '+', 'Charlie,25']
    ]
    expected_df = pd.DataFrame(expected_data, columns=['Line Number', 'Status', 'Content'])
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_file(tmpdir):
    file1 = tmpdir.join("file1.csv")
    file1.write("name,age\nAlice,30\nBob,25")

    file2 = tmpdir.join("file2.csv")
    file2.write("")

    with pytest.raises(ValueError) as excinfo:
        task_func(str(file1), str(file2))
    assert "The file" in str(excinfo.value)

def test_task_func_nonexistent_file(tmpdir):
    file1 = tmpdir.join("file1.csv")
    file1.write("name,age\nAlice,30\nBob,25")

    file2 = tmpdir.join("file2.csv")

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(str(file1), str(file2))
    assert "File not found" in str(excinfo.value)

def test_task_func_custom_delimiter(tmpdir):
    file1 = tmpdir.join("file1.csv")
    file1.write("name;age\nAlice;30\nBob;25")

    file2 = tmpdir.join("file2.csv")
    file2.write("name;age\nAlice;31\nCharlie;25")

    result_df = task_func(str(file1), str(file2), delimiter=';')
    expected_data = [
        [1, '-', 'Alice;30'],
        [1, '+', 'Alice;31'],
        [2, '-', 'Bob;25'],
        [3, '+', 'Charlie;25']
    ]
    expected_df = pd.DataFrame(expected_data, columns=['Line Number', 'Status', 'Content'])
    pd.testing.assert_frame_equal(result_df, expected_df)