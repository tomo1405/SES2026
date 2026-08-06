python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pytest

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    df = pd.read_csv(file_path, header=None, names=["Text"])
    df["Text"] = df["Text"].str.split("\\n").str.join(" ")

    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    try:
        word_count = vectorizer.fit_transform(df["Text"])
    except ValueError:
        # Handle the case where the DataFrame is empty or contains only stop words
        print("No valid words to plot. Returning None.")
        return None

    sum_words = word_count.sum(axis=0)
    words_freq = [
        (word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()
    ]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)

    top_words = words_freq[:10]
    df = pd.DataFrame(top_words, columns=["Word", "Count"])

    ax = df.plot.bar(x="Word", y="Count", rot=0)

    # Saving or displaying the plot
    if save_path:
        plt.savefig(save_path)
        plt.close()
        return None
    else:
        return ax

# Test cases
def test_task_func_valid_input():
    file_path = "data.csv"
    save_path = "plot.png"
    assert task_func(file_path, save_path) is None

def test_task_func_empty_input():
    file_path = "empty.csv"
    save_path = "plot.png"
    assert task_func(file_path, save_path) is None

def test_task_func_stop_words_input():
    file_path = "stop_words.csv"
    save_path = "plot.png"
    assert task_func(file_path, save_path) is None

def test_task_func_invalid_input():
    file_path = "invalid.csv"
    save_path = "plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, save_path)

def test_task_func_no_save_path():
    file_path = "data.csv"
    assert isinstance(task_func(file_path), plt.Axes)