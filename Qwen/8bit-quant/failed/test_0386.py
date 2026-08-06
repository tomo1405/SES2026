import pytest
from src_0386 import task_func
from collections import Counter
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Mocking the plt.savefig to capture the plot
def mock_savefig(fig, fname, format=None):
    buf = BytesIO()
    fig.savefig(buf, format=format)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.gcf().clear()  # Clear the current figure
    return image_base64

@pytest.fixture
def patch_savefig(monkeypatch):
    monkeypatch.setattr(plt, 'savefig', mock_savefig)

def test_task_func_valid_input(patch_savefig):
    fruit_dict = {
        '1': 'Apple',
        '2': 'Banana',
        '3': 'Cherry',
        '4': 'Date',
        '5': 'Elderberry',
        '6': 'Fig',
        '7': 'Grape',
        '8': 'Honeydew',
        '9': 'Indian Prune',
        '10': 'Jackfruit'
    }
    expected_counter = Counter(fruit_dict.values())
    counter, ax = task_func(fruit_dict)
    assert counter == expected_counter
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_fruit(patch_savefig):
    fruit_dict = {
        '1': 'Apple',
        '2': 'Banana',
        '3': 'Orange',  # Invalid fruit
        '4': 'Date',
        '5': 'Elderberry',
        '6': 'Fig',
        '7': 'Grape',
        '8': 'Honeydew',
        '9': 'Indian Prune',
        '10': 'Jackfruit'
    }
    expected_counter = Counter(['Apple', 'Banana', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit'])
    counter, ax = task_func(fruit_dict)
    assert counter == expected_counter
    assert isinstance(ax, plt.Axes)

def test_task_func_non_string_values(patch_savefig):
    fruit_dict = {
        '1': 'Apple',
        '2': 123,  # Non-string value
        '3': 'Cherry',
        '4': None,  # Non-string value
        '5': 'Elderberry',
        '6': 'Fig',
        '7': 'Grape',
        '8': 'Honeydew',
        '9': 'Indian Prune',
        '10': 'Jackfruit'
    }
    expected_counter = Counter(['Apple', 'Cherry', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit'])
    counter, ax = task_func(fruit_dict)
    assert counter == expected_counter
    assert isinstance(ax, plt.Axes)

def test_task_func_empty_dict(patch_savefig):
    fruit_dict = {}
    expected_counter = Counter()
    counter, ax = task_func(fruit_dict)
    assert counter == expected_counter
    assert isinstance(ax, plt.Axes)