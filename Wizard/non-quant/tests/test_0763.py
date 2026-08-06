python
import codecs
import os
import zipfile
import pytest

def task_func(directory_name="latin_files",
          content='Sopetón',
          file_names=['file1.txt', 'file2.txt', 'file3.txt'],
          encoding="latin-1"):

    os.makedirs(directory_name, exist_ok=True)

    for file_name in file_names:
        with open(os.path.join(directory_name, file_name), 'wb') as f:
            f.write(codecs.encode(content, encoding))

    zipped_file = directory_name + '.zip'
    with zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                zipf.write(os.path.join(root, file))

    return zipped_file 

def test_task_func():
    # Test case 1: Default parameters
    assert task_func() == 'latin_files.zip'

    # Test case 2: Custom parameters
    assert task_func(directory_name='custom_dir', content='Custom content', file_names=['file1.txt', 'file2.txt'], encoding='utf-8') == 'custom_dir.zip'

    # Test case 3: Invalid parameters
    with pytest.raises(TypeError):
        task_func(123)