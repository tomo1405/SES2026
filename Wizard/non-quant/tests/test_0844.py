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
    # Test case 1
    assert task_func(1) == "sample text contains several words including."

    # Test case 2
    assert task_func(2) == "text contains several words including. sample text contains several words including."

    # Test case 3
    assert task_func(3) == "contains several words including. sample text contains several words including. text contains several words including."

    # Test case 4
    assert task_func(4) == "several words including. sample text contains several words including. text contains several words including. contains several words including."

    # Test case 5
    assert task_func(5) == "sample text contains several words including. text contains several words including. contains several words including. several words including. sample text contains several words including."

    # Test case 6
    assert task_func(6) == "text contains several words including. sample text contains several words including. contains several words including. several words including. sample text contains several words including. text contains several words including."

    # Test case 7
    assert task_func(7) == "contains several words including. sample text contains several words including. text contains several words including. several words including. sample text contains several words including. text contains several words including. contains several words including."

    # Test case 8
    assert task_func(8) == "several words including. sample text contains several words including. text contains several words including. contains several words including. sample text contains several words including. text contains several words including. contains several words including. several words including."

    # Test case 9
    assert task_func(9) == "sample text contains several words including. text contains several words including. contains several words including. several words including. sample text contains several words including. text contains several words including. contains several words including. several words including. sample text contains several words including."

    # Test case 10
    assert task_func(10) == "text contains several words including. sample text contains several words including. contains several words including. several words including. sample text contains several words including. text contains several words including. contains several words including. several words including. sample text contains several words including. text contains several words including."