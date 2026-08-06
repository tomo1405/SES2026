import os
import re
import shutil
import zipfile

import pytest

from src_0907 import task_func

def test_task_func(tmp_path):
    source_dir = tmp_path / 'source'
    target_dir = tmp_path / 'target'
    
    source_dir.mkdir()
    target_dir.mkdir()
    
    file_names = ['file1.txt', 'file2_processed.txt', 'file3.txt']
    
    for file_name in file_names:
        source_file = source_dir / file_name
        source_file.write_text('test')
    
    archive_path = task_func(str(source_dir), str(target_dir))
    
    assert os.path.isfile(archive_path)
    
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(target_dir)
    
    for file_name in file_names:
        if re.search(r'_processed$', file_name):
            assert (target_dir / file_name).read_text() == 'test'
            assert (source_dir / file_name).read_text() != 'test'
        else:
            assert (target_dir / file_name).read_text() != 'test'