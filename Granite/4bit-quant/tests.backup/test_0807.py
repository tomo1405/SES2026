import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter
from src_0807 import task_func

STOPWORDS = set(stopwords.words('english'))

def test_task_func():
    text = "This is a test sentence. It contains some words and punctuation."
    n = 2
    expected_output = Counter({('this', 'is'): 1, ('is', 'a'): 1, ('a', 'test'): 1, ('test', 'sentence.'): 1, ('sentence.', 'it'): 1, ('it', 'contains'): 1, ('contains', 'some'): 1, ('some', 'words'): 1, ('words', 'and'): 1, ('and', 'punctuation.'): 1})
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_stopwords():
    text = "This is a test sentence. It contains some stopwords like 'is' and 'a'."
    n = 2
    expected_output = Counter({('this', 'test'): 1, ('test', 'sentence.'): 1, ('sentence.', 'contains'): 1, ('contains', 'stopwords'): 1, ('stopwords', 'like'): 1, ('like', 'is'): 1, ('is', 'and'): 1, ('and', 'a'): 1})
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_punctuation():
    text = "This, is a test! sentence... It contains some words and punctuation."
    n = 2
    expected_output = Counter({('this', 'is'): 1, ('is', 'a'): 1, ('a', 'test'): 1, ('test', 'sentence'): 1, ('sentence', 'it'): 1, ('it', 'contains'): 1, ('contains', 'some'): 1, ('some', 'words'): 1, ('words', 'and'): 1, ('and', 'punctuation'): 1})
    actual_output = task_func(text, n)
    assert actual_output == expected_output, "Output does not match expected output"