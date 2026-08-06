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
    
    file_names = ['file1.txt', 'file2_processed.txt', 'file3.txt']
    for file_name in file_names:
        source_file = source_dir / file_name
        source_file.write_text('Test content')
    
    archive_path = task_func(str(source_dir), str(target_dir), archive_name)
    
    assert os.path.isfile(archive_path)
    assert os.path.dirname(archive_path) == str(target_dir)
    assert os.path.basename(archive_path) == archive_name
    
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive_file_names = archive.namelist()
    
    expected_file_names = [file_name for file_name in file_names if re.search(r'_processed$', file_name)]
    assert archive_file_names == expected_file_names
    
    for file_name in expected_file_names:
        target_file = target_dir / file_name
        assert target_file.read_text() == 'Test content'