import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from src_0657 import task_func

sia = SentimentIntensityAnalyzer()

def test_task_func():
    text = "This is a test sentence."
    expected_output = {'neg': 0.0, 'neu': 0.444, 'pos': 0.556, 'compound': 0.556}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_punctuation():
    text = "This, is a test! sentence."
    expected_output = {'neg': 0.0, 'neu': 0.444, 'pos': 0.556, 'compound': 0.556}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_numbers():
    text = "This is a test 1 sentence."
    expected_output = {'neg': 0.0, 'neu': 0.444, 'pos': 0.556, 'compound': 0.556}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_special_characters():
    text = "This #is a $ test^ sentence."
    expected_output = {'neg': 0.0, 'neu': 0.444, 'pos': 0.556, 'compound': 0.556}
    actual_output = task_func(text, sia)
    assert actual_output == expected_output, "Task function returned incorrect output"