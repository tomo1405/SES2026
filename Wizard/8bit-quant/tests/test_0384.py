python
import pandas as pd
import seaborn as sns
from collections import Counter
from textblob import TextBlob
from matplotlib import pyplot as plt

def task_func(text, n, top_k):
    blob = TextBlob(text.lower())
    words_freq = Counter([' '.join(list(span)) for span in blob.ngrams(n=n)])  # Get n-grams and count frequency
    words_freq_filtered = words_freq.most_common(top_k)  # Get top k n-grams
    top_df = pd.DataFrame(words_freq_filtered, columns=['n-gram', 'Frequency'])
    plt.figure()
    return sns.barplot(x='n-gram', y='Frequency', data=top_df)

# Test the function
def test_task_func():
    text = "The quick brown fox jumps over the lazy dog"
    n = 2
    top_k = 3
    result = task_func(text, n, top_k)
    assert isinstance(result, sns.axisgrid.BarPlot)

test_task_func()