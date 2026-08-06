import pandas as pd
from src_0355 import task_func


def test_task_func():
    sentences_dict = {'sentence1': 'This is a sample sentence', 'sentence2': 'This is another sample sentence'}
    word_keys = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
    expected_frequencies = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    expected_word_series = pd.Series(expected_frequencies, index=word_keys)
    expected_plot = expected_word_series.plot(kind='bar')
    actual_plot = task_func(sentences_dict, word_keys)
    assert actual_plot == expected_plot