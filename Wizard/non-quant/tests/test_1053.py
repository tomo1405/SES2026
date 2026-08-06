python
import pandas as pd
import pytest
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

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

def test_task_func():
    # Test case 1: Valid input file and save path
    file_path = "data/input.csv"
    save_path = "data/output.png"
    assert task_func(file_path, save_path) is None
    assert plt.imread(save_path) is not None

    # Test case 2: Valid input file and no save path
    file_path = "data/input.csv"
    assert task_func(file_path) is not None

    # Test case 3: Invalid input file
    file_path = "data/invalid.csv"
    with pytest.raises(FileNotFoundError):
        task_func(file_path)

    # Test case 4: Empty input file
    file_path = "data/empty.csv"
    with pytest.raises(ValueError):
        task_func(file_path)

    # Test case 5: Input file with only stop words
    file_path = "data/stop_words.csv"
    with pytest.raises(ValueError):
        task_func(file_path)