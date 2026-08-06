import pytest
from src_0749 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Fixture to create a sample DataFrame
@pytest.fixture
def sample_df():
    data = {
        'Age': [25, 30, 35, 40, 45],
        'Weight': [60, 70, 80, 90, 100],
        'Height': [165, 170, 175, 180, 185]
    }
    return pd.DataFrame(data)

def test_task_func_empty_result(sample_df):
    # Test case where no rows meet the criteria
    result = task_func(sample_df, 20, 150)
    assert result.empty

def test_task_func_non_empty_result(sample_df):
    # Test case where some rows meet the criteria
    result = task_func(sample_df, 45, 60)
    assert not result.empty
    assert list(result.columns) == ['Age', 'Weight', 'Height']
    assert isinstance(result, pd.DataFrame)

def test_task_func_standardization(sample_df):
    # Test case to check if standardization is applied correctly
    result = task_func(sample_df, 45, 60)
    scaler = StandardScaler()
    expected = pd.DataFrame(scaler.fit_transform(sample_df[sample_df['Age'] < 45 & sample_df['Weight'] > 60]), 
                           columns=sample_df[sample_df['Age'] < 45 & sample_df['Weight'] > 60].columns)
    assert result.equals(expected)

def test_task_func_no_columns(sample_df):
    # Test case where the DataFrame has no columns
    empty_df = pd.DataFrame()
    result = task_func(empty_df, 30, 70)
    assert result.empty

def test_task_func_invalid_age_weight(sample_df):
    # Test case with invalid age and weight values
    result = task_func(sample_df, -10, 150)
    assert result.empty
    result = task_func(sample_df, 50, -50)
    assert result.empty