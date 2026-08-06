python
import shutil
import os
import fnmatch
import itertools

def task_func(src_dir, dst_dir):
    FILE_PATTERNS = ['*.txt', '*.docx']
    # Find all matching files
    matching_files = list(itertools.chain.from_iterable(
        fnmatch.filter(os.listdir(src_dir), pattern) for pattern in FILE_PATTERNS))

    for filename in matching_files:
        shutil.copy2(os.path.join(src_dir, filename), dst_dir)

    return dst_dir

def test_task_func():
    src_dir = 'src_dir'
    dst_dir = 'dst_dir'
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(dst_dir, exist_ok=True)
    with open(os.path.join(src_dir, 'file1.txt'), 'w') as f:
        f.write('test')
    with open(os.path.join(src_dir, 'file2.docx'), 'w') as f:
        f.write('test')
    task_func(src_dir, dst_dir)
    assert os.path.exists(os.path.join(dst_dir, 'file1.txt'))
    assert os.path.exists(os.path.join(dst_dir, 'file2.docx'))
    shutil.rmtree(src_dir)
    shutil.rmtree(dst_dir)