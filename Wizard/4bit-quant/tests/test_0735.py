python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from collections import Counter

def task_func(content):
    words = content.split()[:-1]
    pos_tags = nltk.pos_tag(words)
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)