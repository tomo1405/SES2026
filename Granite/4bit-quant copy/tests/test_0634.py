import re
from nltk.corpus import stopwords
from collections import Counter

def task_func(text: str) -> dict:
    # Remove duplicate words
    stop_words = set(stopwords.words('english'))
    text = ' '.join(sorted(set(text.split()), key=text.index))
    # Tokenize and remove stopwords
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in stop_words]
    
    # Create frequency distribution
    freq_dist = {}
    for word in words:
        freq_dist[word] = freq_dist.get(word, 0) + 1
    
    return freq_dist

def test_task_func():
    text = "This is a sample text. This text contains some duplicate words."
    expected_output = Counter({'this': 2, 'is': 1, 'a': 1, 'sample': 1, 'text.': 1, 'contains': 1, 'some': 1, 'duplicate': 1, 'words.': 1})
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_no_duplicates():
    text = "This is a unique text with no duplicate words."
    expected_output = Counter({'this': 1, 'is': 1, 'a': 1, 'unique': 1, 'text': 1, 'with': 1, 'no': 1, 'duplicate': 1, 'words.': 1})
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_stopwords():
    text = "This is a sample text. This text contains some stop words like 'the' and 'is'."
    expected_output = Counter({'text': 2, 'contains': 1, 'some': 1, 'stop': 1, 'words': 1, 'like': 1, 'the': 1, 'and': 1})
    actual_output = task_func(text)
    assert actual_output == expected_output, "Output does not match expected output"