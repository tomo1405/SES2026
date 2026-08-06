import os
import re
import shutil
import zipfile

from src_0907 import task_func

def test_task_func(tmp_path):
    source_dir = tmp_path / 'source'
    target_dir = tmp_path / 'target'
    archive_name = 'archive.zip'
    
    source_dir.mkdir()
    target_dir.mkdir()
    
    file_name = 'file_processed.txt'
    file_path = source_dir / file_name
    file_path.write_text('test content')
    
    archive_path = task_func(str(source_dir), str(target_dir), archive_name)
    
    assert os.path.isfile(archive_path)
    assert os.path.isfile(os.path.join(target_dir, file_name))
    with zipfile.ZipFile(archive_path, 'r') as archive:
        assert file_name in archive.namelist()