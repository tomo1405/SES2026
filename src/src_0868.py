import re
import string
def task_func(text1, text2):
    # Constants
    PUNCTUATION = string.punctuation

    cleaned_texts = []

    # Remove punctuation from each text string
    for text in [text1, text2]:
        cleaned_text = re.sub('['+re.escape(PUNCTUATION)+']', '', text)
        cleaned_texts.append(cleaned_text)

    return tuple(cleaned_texts)