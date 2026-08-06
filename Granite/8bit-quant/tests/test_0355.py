import collections
import matplotlib.pyplot as plt
import pandas as pd
from unittest.mock import patch

from src_0355 import task_func

def test_task_func():
    sentences_dict = {'1': 'The quick brown fox', '2': 'jumped over the lazy dog'}
    word_keys = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'lazy', 'dog']
    with patch('matplotlib.pyplot.show') as mock_show:
        word_series = task_func(sentences_dict, word_keys)
        mock_show.assert_called_once()
    assert isinstance(word_series, pd.Series)
    assert word_series.index.tolist() == word_keys
    assert word_series.tolist() == [2, 1, 1, 1, 1, 1, 1, 1]