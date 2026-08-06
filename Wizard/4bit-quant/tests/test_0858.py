python
import pytest
from src_0858 import task_func

def test_task_func():
    SOURCE_DIR = 'source_dir'
    DEST_DIR = 'dest_dir'
    EXTENSIONS = ['.txt', '.pdf']

    # Test case 1: Move all files with extension .txt and .pdf from SOURCE_DIR to DEST_DIR
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2.pdf'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file4.pdf'), 'w') as f:
        f.write('test')

    transferred_files = task_func(SOURCE_DIR, DEST_DIR, EXTENSIONS)
    assert transferred_files == ['file1.txt', 'file2.pdf', 'file3.txt', 'file4.pdf']

    # Test case 2: Move all files with extension .txt and .pdf from SOURCE_DIR to DEST_DIR, but only move file1.txt
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2.pdf'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file4.pdf'), 'w') as f:
        f.write('test')

    transferred_files = task_func(SOURCE_DIR, DEST_DIR, ['.txt'])
    assert transferred_files == ['file1.txt']

    # Test case 3: Move all files with extension .txt and .pdf from SOURCE_DIR to DEST_DIR, but only move file1.txt and file3.txt
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2.pdf'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file4.pdf'), 'w') as f:
        f.write('test')

    transferred_files = task_func(SOURCE_DIR, DEST_DIR, ['.txt', '.pdf'])
    assert transferred_files == ['file1.txt', 'file3.txt', 'file4.pdf']

    # Test case 4: Move all files with extension .txt and .pdf from SOURCE_DIR to DEST_DIR, but only move file1.txt and file3.txt, but raise an exception when moving file2.pdf
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2.pdf'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file4.pdf'), 'w') as f:
        f.write('test')

    with pytest.raises(Exception) as e:
        transferred_files = task_func(SOURCE_DIR, DEST_DIR, ['.txt', '.pdf'])
    assert str(e.value) == "Unable to move file source_dir/file2.pdf: [Errno 2] No such file or directory: 'source_dir/file2.pdf'"

    # Test case 5: Move all files with extension .txt and .pdf from SOURCE_DIR to DEST_DIR, but only move file1.txt and file3.txt, but raise an exception when moving file2.pdf, but ignore the exception
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(os.path.join(SOURCE_DIR, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file2.pdf'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file3.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(SOURCE_DIR, 'file4.pdf'), 'w') as f:
        f.write('test')

    transferred_files = task_func(SOURCE_DIR, DEST_DIR, ['.txt', '.pdf'], ignore_exceptions=True)
    assert transferred_files == ['file1.txt', 'file3.txt', 'file4.pdf']