import pytest
from src_0636 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_empty_input():
    text = ""
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_no_words_after_stopwords_removal():
    text = "the quick brown fox jumps over the lazy dog"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.empty
    assert isinstance(ax, plt.Axes)

def test_task_func_single_word():
    text = "hello"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)
    assert df.shape == (1, 1)

def test_task_func_multiple_words():
    text = "hello world hello"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)
    assert df.shape == (1, 1)

def test_task_func_n_3():
    text = "hello world hello"
    df, ax = task_func(text, n=3)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)
    assert df.shape == (1, 1)

def test_task_func_with_duplicates():
    text = "hello hello world"
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)
    assert df.shape == (1, 1)

def test_task_func_with_special_characters():
    text = "hello! world? hello."
    df, ax = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(ax, plt.Axes)
    assert df.shape == (1, 1)