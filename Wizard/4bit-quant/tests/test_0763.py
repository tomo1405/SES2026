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
    # Test case 1: Test with default parameters
    assert task_func() == 'latin_files.zip'

    # Test case 2: Test with custom parameters
    assert task_func(directory_name='custom_dir', content='Custom content', file_names=['file1.txt', 'file2.txt'], encoding='utf-8') == 'custom_dir.zip'

    # Test case 3: Test with non-latin characters
    assert task_func(content='Sopetón') == 'latin_files.zip'

    # Test case 4: Test with non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func(directory_name='non_existent_dir')

    # Test case 5: Test with non-existent encoding
    with pytest.raises(LookupError):
        task_func(encoding='non_existent_encoding')