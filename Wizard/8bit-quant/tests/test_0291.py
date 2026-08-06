python
import nltk
nltk.download('stopwords')
from collections import Counter
import os
from nltk.corpus import stopwords

# Constants
STOPWORDS = set(stopwords.words('english'))

def test_task_func():
    directory_path = 'test_dir'
    os.makedirs(directory_path, exist_ok=True)
    with open(os.path.join(directory_path, 'test_file.txt'), 'w') as file:
        file.write('This is a test file.')
    assert task_func(directory_path) == 2

def task_func(directory_path):
    word_counts = Counter()

    for file_name in os.listdir(directory_path):
        if not file_name.endswith('.txt'):
            continue
        with open(os.path.join(directory_path, file_name), 'r') as file:
            words = [word for word in file.read().split() if word.lower() not in STOPWORDS]
            word_counts.update(words)

    return len(word_counts)