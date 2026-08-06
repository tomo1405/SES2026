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
    # Test case 1: No articles match the pattern
    df = pd.DataFrame({'Title': ['some title'], 'Content': ['some content']})
    expected_result = []
    assert task_func(df) == expected_result

    # Test case 2: Some articles match the pattern
    df = pd.DataFrame({'Title': ['How to do it', 'What is it'], 'Content': ['some content', 'some other content']})
    expected_result = [0, 1]  # Assuming KMeans assigns labels 0 and 1
    assert task_func(df) == expected_result