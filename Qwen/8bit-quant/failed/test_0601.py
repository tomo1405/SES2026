import pytest
from src_0601 import task_func

def test_task_func():
    # Test with a simple DataFrame
    data = {'Word': ['apple', 'apricot', 'banana', 'avocado', 'berry']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    expected = {
        'mean': 6.0,
        'median': 6.0,
        'mode': 6
    }
    assert result == expected

def test_task_func_no_matches():
    # Test with no matches
    data = {'Word': ['cherry', 'date', 'fig', 'grape']}
    df = pd.DataFrame(data)
    letter = 'a'
    result = task_func(df, letter)
    expected = {
        'mean': np.nan,
        'median': np.nan,
        'mode': np.nan
    }
    assert pd.isna(result['mean']) and pd.isna(result['median']) and pd.isna(result['mode'])

def test_task_func_single_match():
    # Test with a single match
    data = {'Word': ['kiwi']}
    df = pd.DataFrame(data)
    letter = 'k'
    result = task_func(df, letter)
    expected = {
        'mean': 4.0,
        'median': 4.0,
        'mode': 4
    }
    assert result == expected

def test_task_func_empty_dataframe():
    # Test with an empty DataFrame
    df = pd.DataFrame(columns=['Word'])
    letter = 'a'
    result = task_func(df, letter)
    expected = {
        'mean': np.nan,
        'median': np.nan,
        'mode': np.nan
    }
    assert pd.isna(result['mean']) and pd.isna(result['median']) and pd.isna(result['mode'])

def test_task_func_multiple_modes():
    # Test with multiple modes
    data = {'Word': ['cat', 'bat', 'rat', 'hat', 'mat']}
    df = pd.DataFrame(data)
    letter = 'c'
    result = task_func(df, letter)
    expected = {
        'mean': 3.0,
        'median': 3.0,
        'mode': 3
    }
    assert result == expected