import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter
def task_func(content):
    words = content.split()[:-1]  # Split and remove the last word
    pos_tags = nltk.pos_tag(words)  # Tokenization is built into pos_tag for simple whitespace tokenization
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)