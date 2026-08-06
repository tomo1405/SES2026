python
import re
import pytest
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

def task_func(df):
    pattern = re.compile(r'(how|what)', re.IGNORECASE)
    interesting_articles = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]
    if interesting_articles.empty:
        return []

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(interesting_articles['Content'])

    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans.fit(X)

    return list(kmeans.labels_)

def test_task_func():
    df = pd.DataFrame({'Title': ['How to train your dragon', 'What is the meaning of life', 'Why is the sky blue'],
                       'Content': ['Ever wonder how to train your dragon? It takes practice and time.',
                                   'The meaning of life is 42.',
                                   'The sky is blue because of the sun.']})

    assert task_func(df) == [0, 1, 1]