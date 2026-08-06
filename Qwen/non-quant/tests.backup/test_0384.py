import pytest
from src_0384 import task_func
from collections import Counter
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    text = "This is a test. This test is only a test."
    n = 2
    top_k = 2
    
    # Expected output structure
    expected_ngrams = [('this is', 2), ('is a', 2)]
    
    # Call the function
    ax = task_func(text, n, top_k)
    
    # Check if the plot is created
    assert isinstance(ax, plt.Axes)
    
    # Check if the DataFrame is created correctly
    df = pd.DataFrame(expected_ngrams, columns=['n-gram', 'Frequency'])
    assert ax.get_title() == 'n-gram vs Frequency'
    assert ax.get_xlabel() == 'n-gram'
    assert ax.get_ylabel() == 'Frequency'
    assert list(ax.get_xticklabels()) == [item[0] for item in expected_ngrams]
    assert list(ax.get_yticklabels()) == [str(item[1]) for item in expected_ngrams]

# Run the tests
if __name__ == "__main__":
    pytest.main()