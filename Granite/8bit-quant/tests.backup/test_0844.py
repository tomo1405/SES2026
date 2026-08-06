import pytest
from src_0844 import task_func
import random
import re

def test_task_func():
    n_sentences = random.randint(1, 10)
    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        sentence = " ".join(random.choice(["sample", "text", "contains", "several", "words", "including"]) for _ in range(sentence_len)) + "."
        sentences.append(sentence)

    text = " ".join(sentences)
    text = re.sub(r'[^\w\s.]', '', text).lower()
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+', ' ', text)

    assert task_func(n_sentences) == text.strip()

def test_task_func_with_zero_sentences():
    assert task_func(0) == ""

def test_task_func_with_one_sentence():
    sentence = " ".join(random.choice(["sample", "text", "contains", "several", "words", "including"]) for _ in range(random.randint(5, 10))) + "."
    assert task_func(1) == sentence.strip()

def test_task_func_with_multiple_sentences():
    n_sentences = random.randint(2, 10)
    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        sentence = " ".join(random.choice(["sample", "text", "contains", "several", "words", "including"]) for _ in range(sentence_len)) + "."
        sentences.append(sentence)

    text = " ".join(sentences)
    text = re.sub(r'[^\w\s.]', '', text).lower()
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+', ' ', text)

    assert task_func(n_sentences) == text.strip()