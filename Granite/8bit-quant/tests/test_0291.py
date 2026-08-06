import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(directory_path):

    word_counts = Counter()

    for file_name in os.listdir(directory_path):
        if not file_name.endswith('.txt'):
            continue
        with open(os.path.join(directory_path, file_name), 'r') as file:
            words = [word for word in file.read().split() if word.lower() not in STOPWORDS]
            word_counts.update(words)

    return len(word_counts)
import pytest

def test_task_func():
    test_cases = [
        ("/path/to/directory1", 10),
        ("/path/to/directory2", 20),
        ("/path/to/directory3", 5)
    ]
    for directory_path, expected_output in test_cases:
        actual_output = task_func(directory_path)
        assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output} for directory {directory_path}"

if __name__ == "__main__":
    pytest.main()