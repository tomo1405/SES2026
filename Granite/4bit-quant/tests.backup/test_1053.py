import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from src_1053 import task_func

def test_task_func_with_valid_data():
    file_path = "path/to/valid/data.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is not None

def test_task_func_with_empty_data():
    file_path = "path/to/empty/data.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is None

def test_task_func_with_only_stop_words():
    file_path = "path/to/data/with/only/stop/words.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is None