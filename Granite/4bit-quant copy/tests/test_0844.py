import pytest
from src_0844 import task_func

def test_task_func():
    n_sentences = random.randint(5, 10)
    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        sentence = " ".join(random.choice(WORD_LIST) for _ in range(sentence_len)) + "."
        sentences.append(sentence)

    text = " ".join(sentences)
    text = re.sub(r'[^\w\s.]', '', text).lower()
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+', ' ', text)

    assert task_func(n_sentences) == text.strip()