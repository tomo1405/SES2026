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
    with pytest.raises(ValueError):
        task_func("This is not a valid sentence.")  # Test if ValueError is raised for sentence without dollar words
    assert task_func("This is a $100 bill. This is a $50 bill.").equals(pd.DataFrame([["$100", 1], ["$50", 1]], columns=["Word", "Frequency"]))  # Test if the output DataFrame is correct for valid input