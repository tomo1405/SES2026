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
        {
            "directory_path": "/path/to/directory",
            "expected_output": 100,
        },
        {
            "directory_path": "/another/path/to/directory",
            "expected_output": 200,
        },
    ]
    for test_case in test_cases:
        result = task_func(test_case["directory_path"])
        assert result == test_case["expected_output"]
if __name__ == "__main__":
    pytest.main()