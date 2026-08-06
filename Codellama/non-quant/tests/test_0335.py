import pytest
from src_0335 import task_func
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def test_task_func():
    documents = ["This is a sample text", "This is another sample text"]
    expected_output = pd.DataFrame({"This": [0.5, 0.5], "is": [0.5, 0.5], "a": [0.5, 0.5], "sample": [0.5, 0.5], "text": [0.5, 0.5]})

    tfidf_df = task_func(documents)

    assert tfidf_df.equals(expected_output)