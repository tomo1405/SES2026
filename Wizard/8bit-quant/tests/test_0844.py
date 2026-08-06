python
import random
import re
import pytest

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        sentence = " ".join(random.choice(WORD_LIST) for _ in range(sentence_len)) + "."
        sentences.append(sentence)

    # Join sentences and ensure no extra spaces around periods
    text = " ".join(sentences)
    # Remove unwanted characters, ensure only letters, spaces, or periods remain
    text = re.sub(r'[^\w\s.]', '', text).lower()
    # Normalize spaces ensuring single space between words and no trailing spaces before periods
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def test_task_func():
    # Test with 1 sentence
    assert task_func(1) == "sample text contains several words including."

    # Test with 2 sentences
    assert task_func(2) == "sample text contains several words including. text contains several words including."

    # Test with 3 sentences
    assert task_func(3) == "sample text contains several words including. text contains several words including. contains several words including."

    # Test with 4 sentences
    assert task_func(4) == "sample text contains several words including. text contains several words including. contains several words including. several words including."

    # Test with 5 sentences
    assert task_func(5) == "sample text contains several words including. text contains several words including. contains several words including. several words including. including."

    # Test with 6 sentences
    assert task_func(6) == "sample text contains several words including. text contains several words including. contains several words including. several words including. including. text contains several words including."

    # Test with 7 sentences
    assert task_func(7) == "sample text contains several words including. text contains several words including. contains several words including. several words including. including. text contains several words including. contains several words including."

    # Test with 8 sentences
    assert task_func(8) == "sample text contains several words including. text contains several words including. contains several words including. several words including. including. text contains several words including. contains several words including. several words including."

    # Test with 9 sentences
    assert task_func(9) == "sample text contains several words including. text contains several words including. contains several words including. several words including. including. text contains several words including. contains several words including. several words including. including."

    # Test with 10 sentences
    assert task_func(10) == "sample text contains several words including. text contains several words including. contains several words including. several words including. including. text contains several words including. contains several words including. several words including. including. text contains several words including."