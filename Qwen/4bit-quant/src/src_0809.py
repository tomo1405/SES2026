import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(text):
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in STOPWORDS]
    text = ' '.join(words)
    blob = TextBlob(text)
    
    return blob.sentiment