python
import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# Make sure to download NLTK stopwords
nltk.download('stopwords')
# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')
# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')

def test_task_func():
    texts = ['This is a sample text.', 'Another sample text.']
    expected_result = pd.DataFrame([[0, 1], [1, 1]], columns=['another', 'is', 'sample', 'text.'])

    result = task_func(texts)

    assert result.equals(expected_result)