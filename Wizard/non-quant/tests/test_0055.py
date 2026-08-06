python
import pandas as pd
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
    text = "This is a test sentence. This is another test sentence. This is a third test sentence."
    expected_df = pd.DataFrame(
        [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],
        columns=["this", "is", "a", "test", "sentence"],
    )
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)