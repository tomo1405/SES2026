import codecs
import os
import zipfile

from src_0763 import task_func


def test_task_func():
    directory_name = "test_directory"
    content = "Sopetón"
    file_names = ["file1.txt", "file2.txt", "file3.txt"]
    encoding = "latin-1"

    zipped_file = task_func(directory_name, content, file_names, encoding)

    assert os.path.exists(zipped_file)
    assert os.path.isfile(zipped_file)
    assert zipfile.is_zipfile(zipped_file)

    with zipfile.ZipFile(zipped_file, 'r') as zipf:
        for file in file_names:
            assert file in zipf.namelist()
            with zipf.open(file) as f:
                assert codecs.decode(f.read(), encoding) == content

    os.remove(zipped_file)