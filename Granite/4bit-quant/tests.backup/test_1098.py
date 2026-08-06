import re
from string import punctuation
from src_1098 import task_func

# Constants
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}
PUNCTUATION = set(punctuation)

def test_task_func():
    text = "This is a test. Please ignore the URL: https://www.example.com"
    expected_output = "test"
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function returned unexpected output"

def test_task_func_punctuation():
    text = "This, is a test!"
    expected_output = "test"
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function returned unexpected output"

def test_task_func_stopwords():
    text = "This is a test. This is a common stopword: the."
    expected_output = "test a test common stopword"
    actual_output = task_func(text)
    assert actual_output == expected_output, "Task function returned unexpected output"