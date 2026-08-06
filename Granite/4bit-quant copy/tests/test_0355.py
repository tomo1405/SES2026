import collections
import matplotlib.pyplot as plt
import pandas as pd
from unittest.mock import patch

from src_0355 import task_func

def test_task_func():
    sentences_dict = {'1': 'the be to of and a', '2': 'in that have I'}
    word_keys = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
    word_counts = collections.Counter(' '.join(sentences_dict.values()).split())
    frequencies = [word_counts[word] for word in word_keys]
    word_series = pd.Series(frequencies, index=word_keys)
    with patch('matplotlib.pyplot.show') as mock_show:
        task_func(sentences_dict, word_keys)
        mock_show.assert_called_once()