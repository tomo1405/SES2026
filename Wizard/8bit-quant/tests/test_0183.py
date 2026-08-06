python
import re
import pytest
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
from src_0183 import task_func

def test_task_func():
    df = {
        'Title': ['How to train your dragon', 'What is the meaning of life', 'Why is the sky blue'],
        'Content': ['Ever wonder how to train your dragon? It takes a special technique called taekwondo!',
                    'The meaning of life is 42.',
                    'The sky is blue because of the sun.']
    }
    df = pd.DataFrame(df)

    pattern = re.compile(r'(how|what)', re.IGNORECASE)
    interesting_articles = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]
    assert not interesting_articles.empty

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(interesting_articles['Content'])

    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans.fit(X)

    assert len(kmeans.labels_) == 2