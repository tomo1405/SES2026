python
import re
import pytest
from nltk.stem import PorterStemmer

def task_func(text_series):
    stemmer = PorterStemmer()

    def process_text(text):
        # Remove non-alphanumeric characters (except spaces)
        text = re.sub('[^\sa-zA-Z0-9]', '', text).lower().strip()
        # Stem each word in the text
        text = " ".join([stemmer.stem(word) for word in text.split()])

        return text

    # Apply the processing to each entry in the Series
    return text_series.apply(process_text)

def test_task_func():
    # Test case 1
    text_series = pd.Series(['This is a test', 'Another test'])
    expected_output = pd.Series(['this is a test', 'anothertest'])
    assert task_func(text_series).equals(expected_output)

    # Test case 2
    text_series = pd.Series(['This is a test', 'Another test', 'A third test'])
    expected_output = pd.Series(['this is a test', 'anothertest', 'a third test'])
    assert task_func(text_series).equals(expected_output)

    # Test case 3
    text_series = pd.Series(['This is a test', 'Another test', 'A third test', 'Fourth test'])
    expected_output = pd.Series(['this is a test', 'anothertest', 'a third test', 'fourth test'])
    assert task_func(text_series).equals(expected_output)

    # Test case 4
    text_series = pd.Series(['This is a test', 'Another test', 'A third test', 'Fourth test', 'Fifth test'])
    expected_output = pd.Series(['this is a test', 'anothertest', 'a third test', 'fourth test', 'fifth test'])
    assert task_func(text_series).equals(expected_output)