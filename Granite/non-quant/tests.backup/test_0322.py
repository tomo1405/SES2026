import pandas as pd
import re
from scipy import stats
from unittest.mock import patch

def task_func(text):
    # Extracting names from the text
    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    names = [name.strip() for name in names if name.strip()]  # Removing any empty or whitespace names

    # Counting name frequencies
    name_freqs = pd.Series(names).value_counts()
    
    # Creating a bar chart of name frequencies if there are names found
    if not name_freqs.empty:
        ax = name_freqs.plot(kind='bar', title="Name Frequencies")
        skewness = stats.skew(name_freqs)
        kurtosis = stats.kurtosis(name_freqs)
    else:
        ax = skewness = kurtosis = None

    if skewness == float('nan'):
        skewness = None
    if kurtosis == float('nan'):
        kurtosis = None
    
    return name_freqs, ax, skewness, kurtosis

def test_task_func():
    with patch('src_0322.pd.Series') as mock_series, patch('src_0322.stats.skew') as mock_skew, patch('src_0322.stats.kurtosis') as mock_kurtosis:
        # Test case 1: No names found in the text
        text1 = 'This is a sample text without any names.'
        name_freqs1, ax1, skewness1, kurtosis1 = task_func(text1)
        mock_series.assert_not_called()
        assert ax1 is None
        assert skewness1 is None
        assert kurtosis1 is None

        # Test case 2: Names found in the text
        text2 = 'John[1], Jane[2], and Bob[3] are the names in this text.'
        name_freqs2, ax2, skewness2, kurtosis2 = task_func(text2)
        mock_series.assert_called_once_with(re.findall(r'(.*?)(?:\[.*?\]|$)', text2))
        mock_skew.assert_called_once_with(name_freqs2)
        mock_kurtosis.assert_called_once_with(name_freqs2)
        assert ax2 is not None
        assert skewness2 is not None
        assert kurtosis2 is not None