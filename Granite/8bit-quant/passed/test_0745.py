import nltk
from string import punctuation
import pandas as pd
def task_func(text):
    if not isinstance(text, str):
        raise ValueError("The input should be a string.")

    tk = nltk.WhitespaceTokenizer()
    words = tk.tokenize(text)    
    dollar_words = [word for word in words if word.startswith('$') and not all(c in set(punctuation) for c in word)]
    freq = nltk.FreqDist(dollar_words)
    df = pd.DataFrame(list(freq.items()), columns=["Word", "Frequency"])
    return df
import pytest

def test_task_func_valid_input():
    assert task_func("This is a test.") is not None

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(123)

def test_task_func_output_type():
    assert isinstance(task_func("This is a test."), pd.DataFrame)

def test_task_func_output_columns():
    df = task_func("This is a test.")
    assert df.columns.tolist() == ["Word", "Frequency"]