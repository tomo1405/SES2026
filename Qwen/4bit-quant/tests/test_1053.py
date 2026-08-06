import pytest
from src_1053 import task_func
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

# Mock data for testing
MOCK_DATA = """Hello world, this is a test.
This is another line of text.
Testing, one, two, three."""

@pytest.fixture
def mock_file():
    return StringIO(MOCK_DATA)

def test_task_func_with_save_path(mock_file, tmpdir):
    temp_file = tmpdir.join("test_output.png")
    result = task_func(mock_file, str(temp_file))
    assert result is None
    assert temp_file.exists()

def test_task_func_without_save_path(mock_file):
    result = task_func(mock_file)
    assert isinstance(result, plt.Axes)

def test_task_func_empty_data(tmpdir):
    empty_data = StringIO("")
    temp_file = tmpdir.join("empty_output.png")
    result = task_func(empty_data, str(temp_file))
    assert result is None
    assert not temp_file.exists()

def test_task_func_only_stop_words(tmpdir):
    stop_words_data = StringIO("a an the in on at and or")
    temp_file = tmpdir.join("stop_words_output.png")
    result = task_func(stop_words_data, str(temp_file))
    assert result is None
    assert not temp_file.exists()