import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
# Constants
SENTENCES = ['This is a sentence', 'Another sentence here', 'More sentences']
def task_func(s: str) -> np.ndarray:
    s = re.sub(r'\W+', ' ', s)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([s] + SENTENCES)
    return X.toarray()[0]