import pytest
from src_1054 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

@pytest.fixture
def sample_data():
    data = {
        "Text": [
            "This is a simple test case.",
            "This is another example.",
            "A simple test case.",
            "Another example here."
        ]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    file_path = "dummy_path"
    save_path = "dummy_save_path"
    result = task_func(file_path=file_path, save_path=save_path)
    
    assert result is None
    assert plt.gcf().get_axes() is not None

def test_task_func_file_not_found(monkeypatch):
    monkeypatch.setattr('builtins.open', lambda: None)
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")