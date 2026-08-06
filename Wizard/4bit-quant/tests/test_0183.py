python
import re
import pytest
from src_0183 import task_func
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

def test_task_func():
    df = pd.DataFrame({'Title': ['How to train your dragon', 'What is the meaning of life', 'The Great Gatsby'], 'Content': ['One morning, when <NAME> woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections.', 'The meaning of life is 42.', 'Fans of The Great Gatsby will be pleased to know that the author of this classic novel, Scott Fitzgerald, was a man of culture and refined taste.']})

    pattern = re.compile(r'(how|what)', re.IGNORECASE)
    interesting_articles = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]
    assert not interesting_articles.empty

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(interesting_articles['Content'])

    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans.fit(X)

    assert len(kmeans.labels_) == 2
    assert kmeans.labels_[0] != kmeans.labels_[1]