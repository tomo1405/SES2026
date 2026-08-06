import re
import string
from nltk.stem import PorterStemmer
from collections import Counter
STEMMER = PorterStemmer()
def task_func(content):
    content = content.split(' ')[:-1]
    words = [word.strip(string.punctuation).lower() for word in re.split('\W+', ' '.join(content))]
    stemmed_words = [STEMMER.stem(word) for word in words]
    word_counts = Counter(stemmed_words)

    return dict(word_counts)