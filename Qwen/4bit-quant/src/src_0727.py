import re
import random
from nltk.corpus import words
from random import sample
# Ensure the words corpus is downloaded
import nltk
nltk.download('words')
# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())  # Correct initialization
def task_func(s, n):

    word_list = re.findall(r'\b\w+\b', s.lower())  # Convert to lowercase for comparison
    english_words = [word for word in word_list if word in SAMPLE_ENGLISH_WORDS]
    if len(english_words) < n:
        return english_words
    else:
        return sample(english_words, n)