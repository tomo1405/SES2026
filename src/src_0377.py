import nltk
import re
from collections import Counter
# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(text):
    words = re.split(r'\W+', text.lower())
    words = [word for word in words if word not in STOPWORDS and word != '']
    word_freq = dict(Counter(words))

    return word_freq