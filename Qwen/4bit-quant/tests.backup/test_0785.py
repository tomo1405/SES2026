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
    assert all(column in df.columns for column in expected_columns)
    
    # Check if the 'Value' column contains only integers between 1 and 5
    assert all(isinstance(value, int) and 1 <= value <= 5 for value in df['Value'])

def test_task_func_file_creation():
    # Test with a small number of entries
    n = 3
    file_path = 'test_news_survey_data.csv'
    task_func(n, file_path=file_path)
    
    # Check if the file exists
    assert os.path.exists(file_path)
    
    # Read the CSV file and check its contents
    df = pd.read_csv(file_path)
    assert len(df) == n
    
    # Clean up: remove the created file
    os.remove(file_path)

def test_task_func_random_seed():
    # Test with a fixed random seed to ensure reproducibility
    n = 2
    random_seed = 42
    df1 = task_func(n, random_seed=random_seed)
    df2 = task_func(n, random_seed=random_seed)
    
    # Check if both DataFrames are identical
    assert df1.equals(df2)

def test_task_func_categories():
    # Test with custom categories
    n = 4
    categories = ['Health', 'Science', 'Travel']
    df = task_func(n, categories=categories)
    
    # Check if the 'Category' column contains only the specified categories
    assert all(category in categories for category in df['Category'])

def test_task_func_news_sites():
    # Test with custom news sites
    n = 4
    news_sites = ['Forbes', 'The Guardian', 'Reuters']
    df = task_func(n, news_sites=news_sites)
    
    # Check if the 'Site' column contains only the specified news sites
    assert all(site in news_sites for site in df['Site'])

def test_task_func_likert_scale():
    # Test with custom Likert scale
    n = 4
    likert_scale = ['Very Bad', 'Bad', 'Neutral', 'Good', 'Very Good']
    df = task_func(n, likert_scale=likert_scale)
    
    # Check if the 'Response' column contains only the specified responses
    assert all(response in likert_scale for response in df['Response'])
    
    # Check if the 'Value' column contains only integers between 1 and 5
    assert all(1 <= value <= 5 for value in df['Value'])