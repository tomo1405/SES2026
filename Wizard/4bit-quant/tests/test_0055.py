python
import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer
import pytest

def task_func(text):
    sentences = re.split(r"\.\s*", text)
    sentences = [sentence for sentence in sentences if len(sentence.strip()) != 0]
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(sentences)
    df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    return df

def test_task_func():
    text = "This is a sample text. This is another sample text. This is a third sample text."
    expected_df = pd.DataFrame(
        [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]],
        columns=['a', 'an', 'another', 'is', 'sample', 'text', 'this', 'third', 'to', '']
    )
    df = task_func(text)
    assert df.equals(expected_df)