import pytest
from src_0291 import task_func
from collections import Counter
import os
from nltk.corpus import stopwords

# Mocking os and nltk functions for testing
class MockedList(list):
    def endswith(self, suffix):
        return self[0].endswith(suffix)

class MockedFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockedOpen:
    def __init__(self, files):
        self.files = files

    def __call__(self, path, mode):
        file_name = path.split('/')[-1]
        for file in self.files:
            if file[0] == file_name:
                return MockedFile(file[1])
        raise FileNotFoundError(f"No such file: '{path}'")

class MockedOS:
    def listdir(self, directory_path):
        return [file[0] for file in self.files]

    def __getattr__(self, name):
        return lambda *args, **kwargs: None

class MockedNltk:
    class CorpusReader:
        def words(self, lang='english'):
            return ['stopword1', 'stopword2', 'stopword3']

    def download(self, resource):
        pass

    corpus = CorpusReader()

@pytest.fixture
def mock_os(monkeypatch):
    mock_os_instance = MockedOS()
    mock_os_instance.files = [
        ('file1.txt', 'This is a test file with some words.'),
        ('file2.txt', 'Another file with different words.')
    ]
    monkeypatch.setattr(os, 'listdir', mock_os_instance.listdir)
    monkeypatch.setattr(os, 'open', MockedOpen(mock_os_instance.files))

@pytest.fixture
def mock_nltk(monkeypatch):
    mock_nltk_instance = MockedNltk()
    monkeypatch.setattr(nltk, 'download', mock_nltk_instance.download)
    monkeypatch.setattr(nltk.corpus, 'stopwords', mock_nltk_instance.corpus)

def test_task_func(mock_os, mock_nltk, tmpdir):
    # Create temporary directory and files
    temp_dir = tmpdir.mkdir("test_dir")
    temp_dir.join("file1.txt").write("This is a test file with some words.")
    temp_dir.join("file2.txt").write("Another file with different words.")

    result = task_func(str(temp_dir))
    assert result == 7  # There are 7 unique words after removing stopwords

def test_task_func_no_txt_files(mock_os, mock_nltk, tmpdir):
    # Create temporary directory without any .txt files
    temp_dir = tmpdir.mkdir("test_dir")
    temp_dir.join("file1.docx").write("This is a test file with some words.")
    temp_dir.join("file2.pdf").write("Another file with different words.")

    result = task_func(str(temp_dir))
    assert result == 0  # No .txt files, so no words to count

def test_task_func_empty_directory(mock_os, mock_nltk, tmpdir):
    # Create empty temporary directory
    temp_dir = tmpdir.mkdir("test_dir")

    result = task_func(str(temp_dir))
    assert result == 0  # Empty directory, so no words to count