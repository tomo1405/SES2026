import gzip

from src_0511 import task_func


def test_task_func_identical_files(tmpdir):
    # Create two identical compressed files
    content = "This is a test file.\nIt contains some text.\n"
    file1 = tmpdir.join("file1.txt.gz")
    file2 = tmpdir.join("file2.txt.gz")
    
    with gzip.open(file1, 'wt') as f1:
        f1.write(content)
    with gzip.open(file2, 'wt') as f2:
        f2.write(content)
    
    result = task_func(str(file1), str(file2))
    assert result == ""

def test_task_func_different_files(tmpdir):
    # Create two different compressed files
    content1 = "This is a test file.\nIt contains some text.\n"
    content2 = "This is a test file.\nIt contains different text.\n"
    file1 = tmpdir.join("file1.txt.gz")
    file2 = tmpdir.join("file2.txt.gz")
    
    with gzip.open(file1, 'wt') as f1:
        f1.write(content1)
    with gzip.open(file2, 'wt') as f2:
        f2.write(content2)
    
    result = task_func(str(file1), str(file2))
    expected_diff = "- It contains some text.\n+ It contains different text.\n"
    assert result == expected_diff

def test_task_func_empty_files(tmpdir):
    # Create two empty compressed files
    file1 = tmpdir.join("file1.txt.gz")
    file2 = tmpdir.join("file2.txt.gz")
    
    with gzip.open(file1, 'wt') as f1:
        pass
    with gzip.open(file2, 'wt') as f2:
        pass
    
    result = task_func(str(file1), str(file2))
    assert result == ""

def test_task_func_one_empty_file(tmpdir):
    # Create one empty and one non-empty compressed file
    content = "This is a test file.\nIt contains some text.\n"
    file1 = tmpdir.join("file1.txt.gz")
    file2 = tmpdir.join("file2.txt.gz")
    
    with gzip.open(file1, 'wt') as f1:
        f1.write(content)
    with gzip.open(file2, 'wt') as f2:
        pass
    
    result = task_func(str(file1), str(file2))
    expected_diff = "- It contains some text.\n"
    assert result == expected_diff

def test_task_func_line_order_difference(tmpdir):
    # Create two files with the same content but in different order
    content1 = "Line 1\nLine 2\n"
    content2 = "Line 2\nLine 1\n"
    file1 = tmpdir.join("file1.txt.gz")
    file2 = tmpdir.join("file2.txt.gz")
    
    with gzip.open(file1, 'wt') as f1:
        f1.write(content1)
    with gzip.open(file2, 'wt') as f2:
        f2.write(content2)
    
    result = task_func(str(file1), str(file2))
    expected_diff = "- Line 1\n+ Line 2\n- Line 2\n+ Line 1\n"
    assert result == expected_diff