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

def test_task_func():
    with pytest.raises(ValueError):
        task_func(123)  # Test if ValueError is raised for non-string input
    assert task_func("Hello, world!").equals(pd.DataFrame([["Hello", 1], ["world", 1]], columns=["Word", "Frequency"]))  # Test if the output DataFrame is correct for a sample input