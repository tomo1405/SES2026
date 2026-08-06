import re
from collections import Counter
# Predefined list of common stopwords
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}
def task_func(text):
    # Remove URLs
    text = re.sub('http[s]?://\S+', '', text)
    # Tokenize the text using regex (improved tokenization)
    words = re.findall(r'\b\w+\b', text)
    # Count the frequency of each word
    word_freq = Counter(words)
    result = Counter(words)
    for i in word_freq:
        if i not in PREDEFINED_STOPWORDS:
            del result[i]
    return list(result.items())