import pytest
from src_0351 import task_func

def test_task_func_valid_input():
    src_folder = 'test_src'
    dst_folder = 'test_dst'
    os.makedirs(src_folder, exist_ok=True)
    os.makedirs(dst_folder, exist_ok=True)
    for i in range(5):
        with open(os.path.join(src_folder, f'file{i}.txt'), 'w') as f:
            f.write('test')
    result = task_func(src_folder, dst_folder)
    assert result['success']
    assert not result['failed_files']
    assert os.path.isfile(os.path.join(dst_folder, 'file0.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file1.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file2.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file3.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file4.txt.gz'))
    shutil.rmtree(src_folder)
    shutil.rmtree(dst_folder)

def test_task_func_invalid_input():
    src_folder = 'test_src'
    dst_folder = 'test_dst'
    os.makedirs(src_folder, exist_ok=True)
    os.makedirs(dst_folder, exist_ok=True)
    for i in range(5):
        with open(os.path.join(src_folder, f'file{i}.txt'), 'w') as f:
            f.write('test')
    result = task_func(src_folder, dst_folder)
    assert result['success']
    assert not result['failed_files']
    assert os.path.isfile(os.path.join(dst_folder, 'file0.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file1.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file2.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file3.txt.gz'))
    assert os.path.isfile(os.path.join(dst_folder, 'file4.txt.gz'))
    shutil.rmtree(src_folder)
    shutil.rmtree(dst_folder)

def test_task_func_invalid_src_folder():
    src_folder = 'test_src'
    dst_folder = 'test_dst'
    os.makedirs(dst_folder, exist_ok=True)
    result = task_func(src_folder, dst_folder)
    assert not result['success']
    assert result['message'] == f"Source folder '{src_folder}' does not exist."
    assert not result['failed_files']
    shutil.rmtree(dst_folder)

def test_task_func_invalid_dst_folder():
    src_folder = 'test_src'
    dst_folder = 'test_dst'
    os.makedirs(src_folder, exist_ok=True)
    result = task_func(src_folder, dst_folder)
    assert not result['success']
    assert result['message'] == f"Destination folder '{dst_folder}' does not exist."
    assert not result['failed_files']
    shutil.rmtree(src_folder)

def test_task_func_invalid_file():
    src_folder = 'test_src'
    dst_folder = 'test_dst'
    os.makedirs(src_folder, exist_ok=True)
    os.makedirs(dst_folder, exist_ok=True)
    with open(os.path.join(src_folder, 'file.txt'), 'w') as f:
        f.write('test')
    result = task_func(src_folder, dst_folder)
    assert not result['success']
    assert result['message'] == 'Some files failed to compress or move.'
    assert result['failed_files'] == ['file.txt']
    shutil.rmtree(src_folder)
    shutil.rmtree(dst_folder)