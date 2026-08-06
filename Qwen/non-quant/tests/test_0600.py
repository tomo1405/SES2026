import pytest
from src_0600 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'Word': ['apple', 'banana', 'apricot', 'cherry', 'avocado']
    }
    return pd.DataFrame(data)

def test_task_func_with_existing_letter(sample_data, monkeypatch):
    letter = 'a'
    
    # Mocking the print statement
    monkeypatch.setattr('builtins.print', lambda x: None)
    
    result = task_func(sample_data, letter)
    
    assert isinstance(result, plt.Axes)
    assert result.get_title() == f"Histogram of Word Lengths starting with '{letter}'"
    assert result.get_xlabel() == "Word Length"
    assert result.get_ylabel() == "Frequency"

def test_task_func_with_non_existing_letter(sample_data, capsys, monkeypatch):
    letter = 'z'
    
    # Mocking the print statement
    monkeypatch.setattr('builtins.print', lambda x: None)
    
    result = task_func(sample_data, letter)
    
    captured = capsys.readouterr()
    assert captured.out.strip() == f"No words start with the letter '{letter}'."
    assert result is None

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Word'])
    letter = 'a'
    
    result = task_func(df, letter)
    
    assert result is None

def test_task_func_with_invalid_input():
    df = [1, 2, 3]  # Invalid input, not a DataFrame
    letter = 'a'
    
    with pytest.raises(AttributeError) as excinfo:
        task_func(df, letter)
    
    assert "DataFrame" in str(excinfo.value)