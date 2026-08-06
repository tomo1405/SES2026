python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(df):

    scaler = MinMaxScaler(feature_range=(0, 1))
    #Scaling the 'age' and 'income' columns
    df_grouped = df.groupby('id').apply(
        lambda x: pd.DataFrame(
            scaler.fit_transform(x[['age', 'income']]), 
            columns=['age', 'income'], 
            index=x.index
        )
    )

    # Creating a histogram of the 'income' column
    hist, bins = np.histogram(df_grouped['income'], bins=10)

    return df_grouped, (hist, bins)

def test_task_func():
    # Test case 1
    df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [25, 30, 35, 40, 45, 50], 'income': [50000, 60000, 70000, 80000, 90000, 100000]})
    expected_df_grouped = pd.DataFrame({'age': {1: 0.5, 2: 0.75, 3: 1.0}, 'income': {1: 0.5, 2: 0.75, 3: 1.0}}, index=[1, 2, 3])
    expected_hist = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    expected_bins = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    result_df_grouped, result_hist, result_bins = task_func(df)
    assert expected_df_grouped.equals(result_df_grouped)
    assert np.array_equal(expected_hist, result_hist)
    assert np.array_equal(expected_bins, result_bins)

    # Test case 2
    df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [25, 30, 35, 40, 45, 50], 'income': [50000, 60000, 70000, 80000, 90000, 100000]})
    expected_df_grouped = pd.DataFrame({'age': {1: 0.5, 2: 0.75, 3: 1.0}, 'income': {1: 0.5, 2: 0.75, 3: 1.0}}, index=[1, 2, 3])
    expected_hist = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    expected_bins = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    result_df_grouped, result_hist, result_bins = task_func(df)
    assert expected_df_grouped.equals(result_df_grouped)
    assert np.array_equal(expected_hist, result_hist)
    assert np.array_equal(expected_bins, result_bins)

    # Test case 3
    df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3], 'age': [25, 30, 35, 40, 45, 50], 'income': [50000, 60000, 70000, 80000, 90000, 100000]})
    expected_df_grouped = pd.DataFrame({'age': {1: 0.5, 2: 0.75, 3: 1.0}, 'income': {1: 0.5, 2: 0.75, 3: 1.0}}, index=[1, 2, 3])
    expected_hist = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    expected_bins = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    result_df_grouped, result_hist, result_bins = task_func(df)
    assert expected_df_grouped.equals(result_df_grouped)
    assert np.array_equal(expected_hist, result_hist)
    assert np.array_equal(expected_bins, result_bins)