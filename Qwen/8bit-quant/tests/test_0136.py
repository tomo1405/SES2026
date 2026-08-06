import pytest
from src_0136 import task_func
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func(None)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]))

def test_task_func_imputation():
    df = pd.DataFrame({
        'A': [1, 2, np.nan],
        'B': [4, np.nan, 6]
    })
    df, ax = task_func(df)
    assert df['B'].isnull().sum() == 0
    assert df['B'].mean() == 5.0

def test_task_func_plot():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df, ax = task_func(df)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert image_base64.startswith('iVBORw0KGgoAAAANSUhEUg')

def test_task_func_plot_title_and_labels():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df, ax = task_func(df)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'B'