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
def task_func(texts):
    cleaned_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    tokenized_texts = [' '.join(word for word in text.split() if word not in STOPWORDS) for text in cleaned_texts]

    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(tokenized_texts)
    dtm_df = pd.DataFrame(dtm.toarray(), columns= vectorizer.get_feature_names_out() if hasattr(vectorizer,
                                                                  'get_feature_names_out') else vectorizer.get_feature_names())

    return dtm_df