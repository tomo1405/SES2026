import pytest
from src_0384 import task_func
from textblob import TextBlob
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    text = "This is a test text for testing the task function. This test text is just for testing."
    n = 2
    top_k = 3
    
    # Expected output
    blob = TextBlob(text.lower())
    words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])
    words_freq_filtered = words_freq.most_common(top_k)
    expected_df = pd.DataFrame(words_freq_filtered, columns=['n-gram', 'Frequency'])
    
    # Actual output
    actual_plot = task_func(text, n, top_k)
    
    # Check if the DataFrame is correct
    assert actual_plot.get_figure().get_axes()[0].get_xticklabels() == [item.get_text() for item in expected_df['n-gram']]
    assert list(actual_plot.get_figure().get_axes()[0].get_yticks()) == list(expected_df['Frequency'])
    
    # Check if the plot is created correctly
    assert isinstance(actual_plot, sns.axisgrid.FacetGrid)
    assert actual_plot.get_figure().get_axes()[0].has_data()
    
    # Clean up the plot
    plt.close(actual_plot.get_figure())