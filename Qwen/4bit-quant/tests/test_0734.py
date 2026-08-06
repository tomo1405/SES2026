from src_0734 import task_func


def test_task_func_empty_string():
    assert task_func("") == 0

def test_task_func_single_word():
    assert task_func("Hello") == 0

def test_task_func_single_non_stopword():
    assert task_func("Python") == 1

def test_task_func_multiple_words_with_stopwords():
    assert task_func("This is a test") == 1

def test_task_func_multiple_words_no_stopwords():
    assert task_func("Python programming is fun") == 2

def test_task_func_punctuation():
    assert task_func("Hello, world!") == 1

def test_task_func_mixed_case():
    assert task_func("PYTHON is FUN") == 1

def test_task_func_large_input():
    assert task_func(" ".join(["word"] * 1000)) == 999

def test_task_func_only_stopwords():
    assert task_func(" ".join(STOPWORDS)) == 0

def test_task_func_no_words_after_split():
    assert task_func("This is the end.") == 0