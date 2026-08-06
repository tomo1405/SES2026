import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import pytest

def task_func(example_str, top_n=30):
    text = ' '.join(re.findall('(.*?)\\[.*?\\]', example_str))
    words = text.split()
    fdist = FreqDist(words)

    if top_n > len(fdist):
        top_n = len(fdist)
    # Initialize a fresh plot for the frequency distribution but do not show it
    plt.figure()
    ax = fdist.plot(top_n, cumulative=False, show=False)
    plt.close()

    top_n_words = dict(fdist.most_common(top_n))
    return ax, top_n_words

def test_task_func():
    example_str = "This is an example string with words and frequencies[word1=10, word2=5, word3=3]"
    top_n = 5
    ax, top_n_words = task_func(example_str, top_n)
    assert isinstance(ax, plt.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == top_n
    assert all(isinstance(word, str) for word in top_n_words.keys())
    assert all(isinstance(count, int) for count in top_n_words.values())

if __name__ == "__main__":
    pytest.main()