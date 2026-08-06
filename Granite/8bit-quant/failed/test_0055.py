import pandas as pd
import pytest
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    sentences = re.split(r"\.\s*", text)
    sentences = [sentence for sentence in sentences if len(sentence.strip()) != 0]
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(sentences)
    df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    return df

def test_task_func():
    text = "This is a sample text. It contains multiple sentences."
    expected_df = pd.DataFrame([[1, 0, 0, 1], [0, 1, 1, 0]], columns=["sample", "text", "multiple", "sentences"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

def test_task_func_empty_text():
    text = ""
    expected_df = pd.DataFrame(columns=["sample", "text", "multiple", "sentences"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

def test_task_func_single_sentence():
    text = "This is a single sentence."
    expected_df = pd.DataFrame([[1, 1, 0, 0]], columns=["sample", "text", "multiple", "sentences"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)