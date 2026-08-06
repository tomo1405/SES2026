import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')
# Load NLTK's list of English stop words
STOPWORDS = stopwords.words('english')

def task_func(texts):
    cleaned_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    tokenized_texts = [' '.join(word for word in text.split() if word not in STOPWORDS) for text in cleaned_texts]

    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(tokenized_texts)
    dtm_df = pd.DataFrame(dtm.toarray(), columns= vectorizer.get_feature_names_out() if hasattr(vectorizer,
                                                                  'get_feature_names_out') else vectorizer.get_feature_names())

    return dtm_df

def test_task_func():
    texts = ['This is a test sentence', 'Another test sentence!']
    expected_output = pd.DataFrame({
        'word': ['a', 'another', 'sentence', 'test', 'this'],
        '0': [1, 1, 1, 2, 1],
        '1': [1, 1, 1, 2, 1]
    })
    output = task_func(texts)
    assert output.equals(expected_output)

def test_task_func_with_empty_text():
    texts = ['', '   ', '    ', None]
    expected_output = pd.DataFrame(columns=['word', '0', '1'])
    output = task_func(texts)
    assert output.equals(expected_output)

def test_task_func_with_no_text():
    texts = []
    expected_output = pd.DataFrame(columns=['word', '0', '1'])
    output = task_func(texts)
    assert output.equals(expected_output)