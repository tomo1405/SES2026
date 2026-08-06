import pytest
from src_0626 import task_func
import pandas as pd

def test_task_func():
    # Test with a list of cities
    cities = ['New York', 'Los Angeles', 'Chicago']
    df = task_func(cities)
    
    # Check if the DataFrame has the correct number of rows
    assert len(df) == len(cities), "The DataFrame should have one row per city"
    
    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ['City', 'Population'], "The DataFrame should have 'City' and 'Population' columns"
    
    # Check if each city is present in the DataFrame
    for city in cities:
        assert city in df['City'].values, f"City '{city}' is missing from the DataFrame"
    
    # Check if the population is within the expected range
    for population in df['Population']:
        assert 1000 <= population <= 20000, "Population should be between 1000 and 20000 (inclusive)"
        assert population % 1000 == 0, "Population should be a multiple of 1000"

# Test with an empty list of cities
def test_task_func_empty():
    df = task_func([])
    assert df.empty, "The DataFrame should be empty when no cities are provided"

# Test with a single city
def test_task_func_single_city():
    cities = ['Houston']
    df = task_func(cities)
    assert len(df) == 1, "The DataFrame should have one row for a single city"
    assert df.iloc[0]['City'] == 'Houston', "The city name should match the input"
    assert 1000 <= df.iloc[0]['Population'] <= 20000, "Population should be between 1000 and 20000 (inclusive)"
    assert df.iloc[0]['Population'] % 1000 == 0, "Population should be a multiple of 1000"