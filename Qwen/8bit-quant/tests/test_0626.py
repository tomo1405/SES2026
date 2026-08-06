import pytest
from src_0626 import task_func
import pandas as pd

def test_task_func():
    # Test with a list of cities
    cities = ['New York', 'Los Angeles', 'Chicago']
    df = task_func(cities)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 2), "DataFrame should have 3 rows and 2 columns"
    
    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ['City', 'Population'], "DataFrame columns should be 'City' and 'Population'"
    
    # Check if the 'City' column contains the correct values
    assert all(city in df['City'].values for city in cities), "All cities should be present in the 'City' column"
    
    # Check if the 'Population' column contains valid population values
    for population in df['Population']:
        assert isinstance(population, int), "Population should be an integer"
        assert 1000 <= population <= 20000, "Population should be between 1000 and 20000"

# Run the tests
if __name__ == "__main__":
    pytest.main()