import pytest
from src_0785 import task_func
import pandas as pd
import os

def test_task_func_output():
    # Test with a small number of entries
    n = 5
    df = task_func(n)
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == n
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['Site', 'Category', 'Response', 'Value']
    assert list(df.columns) == expected_columns
    
    # Check if the 'Value' column contains integers between 1 and 5
    assert all(df['Value'].between(1, 5))
    
    # Clean up the created CSV file
    os.remove('news_survey_data.csv')

def test_task_func_file_creation():
    # Test with a small number of entries
    n = 3
    task_func(n)
    
    # Check if the file was created
    assert os.path.exists('news_survey_data.csv')
    
    # Read the file and check its contents
    df = pd.read_csv('news_survey_data.csv')
    assert len(df) == n
    
    # Clean up the created CSV file
    os.remove('news_survey_data.csv')

def test_task_func_random_seed():
    # Test with a fixed random seed
    n = 5
    random_seed = 42
    df1 = task_func(n, random_seed=random_seed)
    df2 = task_func(n, random_seed=random_seed)
    
    # Check if the DataFrames are identical
    pd.testing.assert_frame_equal(df1, df2)
    
    # Clean up the created CSV files
    os.remove('news_survey_data.csv')

def test_task_func_custom_categories_and_news_sites():
    # Test with custom categories and news sites
    n = 5
    categories = ['Health', 'Science']
    news_sites = ['Forbes', 'Nature']
    df = task_func(n, categories=categories, news_sites=news_sites)
    
    # Check if the DataFrame contains only the specified categories and news sites
    assert all(df['Category'].isin(categories))
    assert all(df['Site'].isin(news_sites))
    
    # Clean up the created CSV file
    os.remove('news_survey_data.csv')