import pandas as pd
from datetime import datetime
from src_0476 import task_func
import pytest

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'dates': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
        'values': [10, 20, 30, 40, 50]
    })

def test_invalid_input_types(sample_data):
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_data, 123, 'US')
    assert str(exc_info.value) == "Invalid input types."

def test_invalid_country_code(sample_data):
    with pytest.raises(ValueError) as exc_info:
        task_func(sample_data, '%Y-%m-%d', 'US')
    assert str(exc_info.value) == "Country 'US' not found in country codes."

def test_valid_input(sample_data):
    ax = task_func(sample_data, '%Y-%m-%d', 'US')
    assert ax is not None