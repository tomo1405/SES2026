import pandas as pd
import pytest
import seaborn as sns
from src_0602 import task_func


def test_task_func_with_valid_data():
    df = pd.DataFrame({'Word': ['apple', 'apricot', 'banana', 'avocado']})
    letter = 'a'
    result = task_func(df, letter)
    assert isinstance(result, sns.axisgrid.AxesSubplot)

def test_task_func_with_no_matching_words():
    df = pd.DataFrame({'Word': ['banana', 'cherry', 'date']})
    letter = 'a'
    result = task_func(df, letter)
    assert result is None

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame(columns=['Word'])
    letter = 'a'
    result = task_func(df, letter)
    assert result is None

def test_task_func_without_word_column():
    df = pd.DataFrame({'Fruit': ['apple', 'banana', 'cherry']})
    letter = 'a'
    with pytest.raises(ValueError) as excinfo:
        task_func(df, letter)
    assert str(excinfo.value) == "The DataFrame should contain a 'Word' column."

def test_task_func_with_single_word():
    df = pd.DataFrame({'Word': ['apple']})
    letter = 'a'
    result = task_func(df, letter)
    assert isinstance(result, sns.axisgrid.AxesSubplot)

def test_task_func_with_multiple_same_words():
    df = pd.DataFrame({'Word': ['apple', 'apple', 'apple']})
    letter = 'a'
    result = task_func(df, letter)
    assert isinstance(result, sns.axisgrid.AxesSubplot)