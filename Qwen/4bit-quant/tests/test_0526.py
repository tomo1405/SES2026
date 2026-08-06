import json

import matplotlib.pyplot as plt
import pytest
from src_0526 import task_func


# Mocking the file reading and plotting functionalities for testing
class MockFile:
    def __init__(self, content):
        self.content = content

    def read(self):
        return self.content

class MockJSON:
    @staticmethod
    def load(file):
        return json.loads(file.read())

class MockMatplotlib:
    @staticmethod
    def subplots():
        fig, ax = plt.subplots()
        return fig, ax

@pytest.fixture
def mock_data():
    return [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
        {"a": 5, "b": 6}
    ]

@pytest.fixture
def mock_file(mock_data):
    return MockFile(json.dumps(mock_data))

@pytest.fixture(autouse=True)
def patch_json(monkeypatch, mock_data):
    monkeypatch.setattr(json, 'load', MockJSON.load)

@pytest.fixture(autouse=True)
def patch_matplotlib(monkeypatch):
    monkeypatch.setattr(plt, 'subplots', MockMatplotlib.subplots)

def test_task_func(mock_file):
    expected_stats = {
        "a": {"mean": 3.0, "median": 3.0},
        "b": {"mean": 4.0, "median": 4.0}
    }
    
    result, plots = task_func(mock_file)
    
    assert result == expected_stats
    assert len(plots) == 2
    for ax in plots:
        assert isinstance(ax, plt.Axes)