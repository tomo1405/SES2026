import pytest
from src_0054 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_text():
    return """Name: Alice, Email: alice@example.com, Age: 30, Country: USA
Name: Bob, Email: bob@example.com, Age: 25, Country: Canada"""

def test_task_func(sample_text, monkeypatch):
    # Mock the plt.show() call to avoid opening a window
    monkeypatch.setattr(plt, 'show', lambda: None)

    # Call the function with the sample text
    result_df = task_func(sample_text)

    # Check if the returned DataFrame is correct
    expected_data = {
        "Name": ["Alice", "Bob"],
        "Email": ["alice@example.com", "bob@example.com"],
        "Age": [30, 25],
        "Country": ["USA", "Canada"]
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check if the DataFrame has the correct data types
    assert result_df["Age"].dtype == int