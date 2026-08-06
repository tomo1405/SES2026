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

# Test the function with a sample input
def test_task_func():
    example_str = "This is a sample string [with some] [tags] [in it]."
    ax, top_n_words = task_func(example_str)
    assert isinstance(ax, plt.Axes)
    assert isinstance(top_n_words, dict)
    assert len(top_n_words) == 30
    assert 'is' in top_n_words
    assert 'a' in top_n_words
    assert 'sample' in top_n_words
    assert 'string' in top_n_words
    assert 'with' in top_n_words
    assert 'some' in top_n_words
    assert 'tags' in top_n_words
    assert 'in' in top_n_words
    assert 'it' in top_n_words

# Run the test
test_task_func()