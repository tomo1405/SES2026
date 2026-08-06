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
    directory_name = "test_directory"
    content = "Test content"
    file_names = ["test_file1.txt", "test_file2.txt", "test_file3.txt"]
    encoding = "utf-8"

    zipped_file = task_func(directory_name, content, file_names, encoding)

    assert os.path.exists(zipped_file)
    assert zipfile.is_zipfile(zipped_file)

    with zipfile.ZipFile(zipped_file, 'r') as zipf:
        zip_contents = zipf.namelist()
        for file_name in file_names:
            assert os.path.join(directory_name, file_name) in zip_contents

if __name__ == "__main__":
    pytest.main()