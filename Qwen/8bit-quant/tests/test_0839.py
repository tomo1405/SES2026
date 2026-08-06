import pytest
from src_0839 import task_func
import pandas as pd
from nltk.stem import PorterStemmer

# Ensure the NLTK data is downloaded
import nltk
nltk.download('punkt')

def test_task_func():
    # Create a sample DataFrame
    data = {'text': ['Hello, world!', 'Python is great.', 'Data Science & AI']}
    df = pd.DataFrame(data)

    # Expected output after stemming
    expected_output = pd.Series(['hello world', 'python is great', 'data scienc ai'])

    # Call the function
    result = task_func(df['text'])

    # Check if the result matches the expected output
    assert result.equals(expected_output), f"Expected {expected_output}, but got {result}"

def test_task_func_empty_string():
    # Create a sample DataFrame with an empty string
    data = {'text': ['']}
    df = pd.DataFrame(data)

    # Expected output after stemming
    expected_output = pd.Series([''])

    # Call the function
    result = task_func(df['text'])

    # Check if the result matches the expected output
    assert result.equals(expected_output), f"Expected {expected_output}, but got {result}"

def test_task_func_special_characters():
    # Create a sample DataFrame with special characters
    data = {'text': ['!!!@#$', '###$$%^&*()']}
    df = pd.DataFrame(data)

    # Expected output after stemming
    expected_output = pd.Series(['', ''])

    # Call the function
    result = task_func(df['text'])

    # Check if the result matches the expected output
    assert result.equals(expected_output), f"Expected {expected_output}, but got {result}"