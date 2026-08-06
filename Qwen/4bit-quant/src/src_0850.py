import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(input_string):
    lines = input_string.split('\n')
    word_count = Counter()
    for line in lines:
        words = re.findall(r'\b\w+\b', line)
        words = [word for word in words if word not in STOPWORDS]
        word_count.update(words)
    return dict(word_count)