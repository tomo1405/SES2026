import re
from nltk import word_tokenize
from collections import Counter
def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9 ]+', '', input_str)
    words = word_tokenize(cleaned_str)
    freq_dict = Counter(words)

    return freq_dict