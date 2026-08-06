import pandas as pd
import pytest
from src_0224 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({'A': ['cat', 'dog', 'mouse'], 'B': [1, 2, 3]})

@pytest.fixture
def input_dct():
    return {'cat': 'kitten', 'dog': 'puppy'}

def test_input_df(input_df):
    assert isinstance(input_df, pd.DataFrame)

def test_input_dct(input_dct):
    assert isinstance(input_dct, dict)

def test_replace_values(input_df, input_dct):
    expected_df = input_df.replace(input_dct)
    actual_df = task_func(input_df, input_dct)
    assert expected_df.equals(actual_df)

def test_encode_categorical_features(input_df):
    expected_df = input_df.copy()
    expected_df['A'] = expected_df['A'].astype('category').cat.codes
    actual_df = task_func(input_df, {})
    assert expected_df.equals(actual_df)

def test_standardize_numerical_features(input_df):
    expected_df = (input_df - input_df.mean()) / input_df.std()
    actual_df = task_func(input_df, {}, columns=['B'])
    assert expected_df.equals(actual_df)