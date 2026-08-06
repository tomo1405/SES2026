import gzip

from src_0511 import task_func


def test_task_func_identical_files(tmp_path):
    content = "This is a test file.\n"
    file1 = tmp_path / "file1.gz"
    file2 = tmp_path / "file2.gz"
    
    with gzip.open(file1, 'wt') as f:
        f.write(content)
    with gzip.open(file2, 'wt') as f:
        f.write(content)
    
    result = task_func(str(file1), str(file2))
    assert result == ""

def test_task_func_different_files(tmp_path):
    content1 = "Line 1\nLine 2\n"
    content2 = "Line 1\nDifferent Line 2\nLine 3\n"
    
    file1 = tmp_path / "file1.gz"
    file2 = tmp_path / "file2.gz"
    
    with gzip.open(file1, 'wt') as f:
        f.write(content1)
    with gzip.open(file2, 'wt') as f:
        f.write(content2)
    
    result = task_func(str(file1), str(file2))
    expected_diff = "- Line 2\n+ Different Line 2\n+ Line 3\n"
    assert result == expected_diff

def test_task_func_empty_files(tmp_path):
    file1 = tmp_path / "file1.gz"
    file2 = tmp_path / "file2.gz"
    
    with gzip.open(file1, 'wt') as f:
        pass
    with gzip.open(file2, 'wt') as f:
        pass
    
    result = task_func(str(file1), str(file2))
    assert result == ""

def test_task_func_one_empty_file(tmp_path):
    content = "This is a test file.\n"
    file1 = tmp_path / "file1.gz"
    file2 = tmp_path / "file2.gz"
    
    with gzip.open(file1, 'wt') as f:
        f.write(content)
    with gzip.open(file2, 'wt') as f:
        pass
    
    result = task_func(str(file1), str(file2))
    expected_diff = "- This is a test file.\n"
    assert result == expected_diff