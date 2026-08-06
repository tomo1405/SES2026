import re
import numpy as np
from scipy.stats import ttest_rel
def task_func(text1, text2):
    word_counts1 = np.array([len(word) for word in re.split(r'\W+', text1) if word])
    word_counts2 = np.array([len(word) for word in re.split(r'\W+', text2) if word])

    if len(word_counts1) != len(word_counts2):
        return (np.nan, np.nan)

    t_statistic, p_value = ttest_rel(word_counts1, word_counts2)
    return t_statistic, p_value