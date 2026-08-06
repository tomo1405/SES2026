python
import re
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

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
    example_str = "This is an example string [with some [nested] [brackets]]."
    ax, top_n_words = task_func(example_str)
    assert isinstance(ax, plt.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == 30
    assert all(isinstance(k, str) for k in top_n_words.keys())
    assert all(isinstance(v, int) for v in top_n_words.values())