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
    df = pd.DataFrame({'id': [1, 1, 2, 2], 'age': [25, 30, 40, 50], 'income': [50000, 60000, 70000, 80000]})
    expected_df_grouped = pd.DataFrame({'age': {1: 0.5, 2: 0.75}, 'income': {1: 0.5, 2: 0.75}}, index=[1, 2])
    expected_hist = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    expected_bins = np.array([40000., 60000., 80000.])
    result_df_grouped, result_hist, result_bins = task_func(df)
    assert result_df_grouped.equals(expected_df_grouped)
    assert (result_hist == expected_hist).all()
    assert (result_bins == expected_bins).all()

    # Test case 2
    df = pd.DataFrame({'id': [1, 1, 2, 2], 'age': [25, 30, 40, 50], 'income': [50000, 60000, 70000, 80000]})
    expected_df_grouped = pd.DataFrame({'age': {1: 0.5, 2: 0.75}, 'income': {1: 0.5, 2: 0.75}}, index=[1, 2])
    expected_hist = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    expected_bins = np.array([40000., 60000., 80000.])
    result_df_grouped, result_hist, result_bins = task_func(df)
    assert result_df_grouped.equals(expected_df_grouped)
    assert (result_hist == expected_hist).all()
    assert (result_bins == expected_bins).all()

    # Test case 3
    df = pd.DataFrame({'id': [1, 1, 2, 2], 'age': [25, 30, 40, 50], 'income': [50000, 60000, 70000, 80000]})
    expected_df_grouped = pd.DataFrame({'age': {1: 0.5, 2: 0.75}, 'income': {1: 0.5, 2: 0.75}}, index=[1, 2])
    expected_hist = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    expected_bins = np.array([40000., 60000., 80000.])
    result_df_grouped, result_hist, result_bins = task_func(df)
    assert result_df_grouped.equals(expected_df_grouped)
    assert (result_hist == expected_hist).all()
    assert (result_bins == expected_bins).all()