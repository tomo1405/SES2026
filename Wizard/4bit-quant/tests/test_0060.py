python
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pytest

def task_func(page_title):
    try:
        text = wikipedia.page(page_title).content
    except Exception as e:
        print(f"An error occured: {e}")
        return None
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    ax = plt.gca()
    return ax

def test_task_func():
    # Test case 1: Valid page title
    ax = task_func("Python (programming language)")
    assert ax is not None
    assert isinstance(ax, plt.Axes)

    # Test case 2: Invalid page title
    ax = task_func("Invalid page title")
    assert ax is None