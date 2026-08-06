import pytest
from src_0060 import task_func
import wikipedia
import wordcloud
import matplotlib.pyplot as plt

# Mocking the Wikipedia API call
class MockPage:
    def __init__(self, content):
        self.content = content

def mock_wikipedia_page(title):
    if title == "Valid Page":
        return MockPage("This is some sample text for testing.")
    else:
        raise Exception("Invalid page title")

# Patching the wikipedia module to use the mock
@pytest.fixture(autouse=True)
def patch_wikipedia(monkeypatch):
    monkeypatch.setattr(wikipedia, 'page', mock_wikipedia_page)

def test_task_func_valid_page():
    ax = task_func("Valid Page")
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_page(capsys):
    ax = task_func("Invalid Page")
    captured = capsys.readouterr()
    assert "An error occured: Invalid page title" in captured.err
    assert ax is None