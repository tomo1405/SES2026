import re
import numpy as np
from scipy.stats import ttest_rel
from src_0719 import task_func

def test_task_func():
    text1 = "This is a sample text"
    text2 = "This is another sample text"
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])
    t_statistic, p_value = task_func(text1, text2)
    assert isinstance(t_statistic, float) or isinstance(t_statistic, int)
    assert isinstance(p_value, float) or isinstance(p_value, int)
    if len(word_counts1) == len(word_counts2):
        assert t_statistic == ttest_rel(word_counts1, word_counts2)[0]
        assert p_value == ttest_rel(word_counts1, word_counts2)[1]
    else:
        assert np.isnan(t_statistic)
        assert np.isnan(p_value)