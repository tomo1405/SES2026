import re
from collections import Counter
def task_func(text, top_n):
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)

    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_freq = Counter(words)

    return word_freq.most_common(top_n)