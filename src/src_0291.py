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