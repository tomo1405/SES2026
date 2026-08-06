python
import re
import nltk
from nltk.stem import PorterStemmer
import pandas as pd
import pytest

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
    # Test case 1: Test with a single string
    text = "This is a test string."
    expected_output = "this test string"
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 2: Test with a list of strings
    text_list = ["This is a test string.", "Another test string."]
    expected_output_list = ["this test string", "another test string"]
    assert task_func(pd.Series(text_list)).tolist() == expected_output_list

    # Test case 3: Test with a Series of strings
    text_series = pd.Series(["This is a test string.", "Another test string."])
    expected_output_series = pd.Series(["this test string", "another test string"])
    assert task_func(text_series).equals(expected_output_series)

    # Test case 4: Test with an empty string
    text = ""
    expected_output = ""
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 5: Test with a string with only non-alphanumeric characters
    text = "This is a test string!@#$"
    expected_output = "this test string"
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 6: Test with a string with only one word
    text = "test"
    expected_output = "test"
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 7: Test with a string with multiple words
    text = "This is a test string with multiple words."
    expected_output = "this test string with multiple word"
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 8: Test with a string with multiple words and non-alphanumeric characters
    text = "This is a test string!@#$ with multiple words."
    expected_output = "this test string with multiple word"
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 9: Test with a string with multiple words and stemming
    text = "This is a test string with multiple words."
    expected_output = "this test string with multiple word"
    assert task_func(pd.Series([text]))[0] == expected_output

    # Test case 10: Test with a string with multiple words and stemming and non-alphanumeric characters
    text = "This is a test string!@#$ with multiple words."
    expected_output = "this test string with multiple word"
    assert task_func(pd.Series([text]))[0] == expected_output