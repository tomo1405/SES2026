import pytest
from src_0335 import task_func
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def test_task_func():
    documents = ["This is a sample document", "This is another sample document"]
    expected_output = pd.DataFrame([[0.5, 0.5], [0.5, 0.5]], columns=["This", "is"])

    tfidf_df = task_func(documents)

    assert tfidf_df.equals(expected_output)