import pytest
from src_0636 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_empty_input():
    text = ""
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_no_stopwords():
    text = "hello hello world"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_with_stopwords():
    text = "this is a sample text with some stopwords"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_n_3():
    text = "this is a sample text with some stopwords"
    df, ax = task_func(text, n=3)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_single_word():
    text = "hello"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_duplicate_words():
    text = "hello hello hello world"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)