import pytest
from src_0580 import task_func
import os
import io
from collections import Counter
import matplotlib.pyplot as plt

@pytest.fixture
def create_csv_file(tmpdir):
    content = "word1,word2\nword3,word4\nword1,word2"
    p = tmpdir.join("test.csv")
    p.write(content)
    return str(p)

def test_task_func(create_csv_file):
    ax, most_common_words = task_func(create_csv_file)
    assert isinstance(ax, plt.Axes)
    assert isinstance(most_common_words, list)
    assert len(most_common_words) == 10
    expected_counter = Counter(['word1', 'word2', 'word3', 'word4'])
    actual_counter = Counter(word for word, count in most_common_words)
    assert actual_counter == expected_counter

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.csv")
    assert str(excinfo.value) == "The file non_existent_file.csv was not found."

def test_task_func_io_error(create_csv_file):
    # Simulate an IO error by making the file unreadable
    os.chmod(create_csv_file, 0o000)
    with pytest.raises(IOError) as excinfo:
        task_func(create_csv_file)
    assert str(excinfo.value) == f"There was an error reading the file {create_csv_file}."
    # Restore file permissions
    os.chmod(create_csv_file, 0o644)