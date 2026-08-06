import pytest
from src_0054 import task_func
import pandas as pd
import regex as re
import io
import sys

# Mocking plt.show() to prevent it from opening a window during tests
class Mock:
    def show(self):
        pass

@pytest.fixture
def mock_plt_show(monkeypatch):
    monkeypatch.setattr(plt, 'show', Mock().show)

def test_task_func(mock_plt_show):
    input_text = """Name: Alice, Email: alice@example.com, Age: 30, Country: USA
                   Name: Bob, Email: bob@example.com, Age: 25, Country: Canada"""
    
    expected_data = {
        "Name": ["Alice", "Bob"],
        "Email": ["alice@example.com", "bob@example.com"],
        "Age": [30, 25],
        "Country": ["USA", "Canada"]
    }
    expected_df = pd.DataFrame(expected_data)
    expected_df["Age"] = expected_df["Age"].astype(int)
    
    result_df = task_func(input_text)
    
    assert result_df.equals(expected_df), "The DataFrame returned by task_func does not match the expected DataFrame."

def test_task_func_no_matches(mock_plt_show):
    input_text = "No matching data here"
    expected_df = pd.DataFrame(columns=["Name", "Email", "Age", "Country"])
    
    result_df = task_func(input_text)
    
    assert result_df.equals(expected_df), "The DataFrame returned by task_func should be empty when no matches are found."