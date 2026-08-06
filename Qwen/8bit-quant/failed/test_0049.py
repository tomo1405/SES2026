import pytest
from src_0049 import task_func
from datetime import datetime
import os

@pytest.fixture
def mock_time(monkeypatch):
    def mock_time():
        return 1633072800  # Example fixed time
    monkeypatch.setattr(time, 'time', mock_time)

@pytest.fixture
def mock_random(monkeypatch):
    def mock_randint(a, b):
        return 1633072800  # Example fixed random time
    monkeypatch.setattr(random, 'randint', mock_randint)

def test_task_func_no_output_path(mock_time, mock_random):
    n = 5
    timestamps = task_func(n)
    assert len(timestamps) == n
    for ts in timestamps:
        assert isinstance(ts, str)
        assert datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

def test_task_func_with_output_path(mock_time, mock_random, tmpdir):
    n = 5
    output_path = str(tmpdir / "test_output.png")
    timestamps = task_func(n, output_path)
    assert len(timestamps) == n
    for ts in timestamps:
        assert isinstance(ts, str)
        assert datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    assert os.path.exists(output_path)

def test_task_func_plot(mock_time, mock_random, monkeypatch):
    n = 5
    mock_show_called = False
    def mock_show():
        nonlocal mock_show_called
        mock_show_called = True
    monkeypatch.setattr(plt, 'show', mock_show)
    task_func(n)
    assert mock_show_called