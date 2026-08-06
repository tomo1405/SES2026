import pytest
from src_0291 import task_func
import os
from collections import Counter

# Mocking os and nltk for testing
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockDir:
    def __init__(self, files):
        self.files = files

    def listdir(self, path):
        return self.files

def mock_os_path_join(path, filename):
    return f"{path}/{filename}"

def mock_nltk_download(resource):
    pass

def mock_stopwords_words(lang):
    return ["the", "and", "is", "in"]

# Patching
os.path.join = mock_os_path_join
nltk.download = mock_nltk_download
nltk.corpus.stopwords.words = mock_stopwords_words

@pytest.fixture
def setup_files(tmp_path):
    # Create temporary files
    d = tmp_path / "subdir"
    d.mkdir()
    (d / "file1.txt").write_text("The quick brown fox jumps over the lazy dog.")
    (d / "file2.txt").write_text("This is a test file.")
    (d / "file3.docx").write_text("This should not be counted.")
    return d

def test_task_func(setup_files):
    directory_path = str(setup_files)
    result = task_func(directory_path)
    expected_word_counts = Counter(['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'test', 'file'])
    assert result == len(expected_word_counts)

def test_task_func_no_txt_files(setup_files):
    directory_path = str(setup_files)
    (setup_files / "file4.pdf").write_text("Another file that shouldn't be counted.")
    result = task_func(directory_path)
    expected_word_counts = Counter(['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'test', 'file'])
    assert result == len(expected_word_counts)

def test_task_func_empty_directory(tmp_path):
    directory_path = str(tmp_path)
    result = task_func(directory_path)
    assert result == 0