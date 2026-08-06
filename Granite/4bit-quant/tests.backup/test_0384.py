import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt
import pytest

def task_func(text, n, top_k):
    blob = TextBlob(text.lower())
    words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])  # Get n-grams and count frequency
    words_freq_filtered = words_freq.most_common(top_k)  # Get top k n-grams
    top_df = pd.DataFrame(words_freq_filtered, columns=['n-gram', 'Frequency'])
    plt.figure()

    return sns.barplot(x='n-gram', y='Frequency', data=top_df)

def test_task_func():
    text = "This is a sample text for testing."
    n = 2
    top_k = 5
    expected_output = sns.barplot(x='n-gram', y='Frequency', data=pd.DataFrame({'n-gram': ['this is', 'is a', 'a sample', 'sample text', 'text for'], 'Frequency': [1, 1, 1, 1, 1]}))
    actual_output = task_func(text, n, top_k)
    assert actual_output == expected_output, "Output does not match expected output"

if __name__ == "__main__":
    pytest.main()