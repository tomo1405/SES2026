import pandas as pd
from sklearn.preprocessing import StandardScaler
from src_0219 import task_func
import pytest

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def test_input_df_type():
    with pytest.raises(ValueError) as exc_info:
        task_func("not_a_df", {}, plot_histogram=False)
    assert "Input df is not a DataFrame." in str(exc_info.value)

def test_required_columns():
    df = pd.DataFrame()
    with pytest.raises(ValueError) as exc_info:
        task_func(df, {}, plot_histogram=False)
    assert "Missing columns in DataFrame" in str(exc_info.value)
    for col in FEATURES + [TARGET]:
        df[col] = [1] * len(df)
    task_func(df, {}, plot_histogram=False)

def test_replace_values():
    df = pd.DataFrame()
    for col in FEATURES + [TARGET]:
        df[col] = [1] * len(df)
    mapping = {"old1": "new1", "old2": "new2"}
    df_new = task_func(df, mapping, plot_histogram=False)[0]
    for col in FEATURES + [TARGET]:
        assert "old" not in df_new[col].values

def test_standardize_features():
    df = pd.DataFrame()
    for col in FEATURES + [TARGET]:
        df[col] = [1] * len(df)
    df_new = task_func(df, {}, plot_histogram=False)[0]
    scaler = StandardScaler()
    expected = scaler.fit_transform(df[FEATURES])
    assert (df_new[FEATURES] == expected).all().all()

def test_plot_histogram():
    df = pd.DataFrame()
    for col in FEATURES + [TARGET]:
        df[col] = [1] * len(df)
    df_new, ax = task_func(df, {}, plot_histogram=True)
    assert isinstance(ax, matplotlib.axes.Axes)