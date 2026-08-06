python
import pandas as pd
import statsmodels.api as sm
import pytest

def task_func(df: pd.DataFrame, height: int, weight: int, columns: list) -> sm.regression.linear_model.RegressionResultsWrapper:
    # Check for empty DataFrame
    if df.empty:
        return None

    # Filter the DataFrame based on provided column names
    selected_df = df[(df[columns[1]] > height) & (df[columns[2]] < weight)]
    
    # If no rows match the condition, return None
    if selected_df.empty:
        return None
    
    X = selected_df[columns[1:]]
    y = selected_df[columns[0]]
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    return results

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'height': [170, 180, 160], 'weight': [70, 80, 60], 'gender': ['M', 'M', 'F']})
    height = 175
    weight = 75
    columns = ['gender', 'height', 'weight']
    expected_result = sm.OLS(df['height'], sm.add_constant(df[['height', 'weight']]))
    expected_result = expected_result.fit()
    assert task_func(df, height, weight, columns) == expected_result
    
    # Test case 2: Empty DataFrame
    df = pd.DataFrame()
    height = 175
    weight = 75
    columns = ['gender', 'height', 'weight']
    assert task_func(df, height, weight, columns) is None
    
    # Test case 3: No rows match the condition
    df = pd.DataFrame({'height': [170, 180, 160], 'weight': [70, 80, 60], 'gender': ['M', 'M', 'F']})
    height = 185
    weight = 85
    columns = ['gender', 'height', 'weight']
    assert task_func(df, height, weight, columns) is None
    
    # Test case 4: Invalid input type
    df = pd.DataFrame({'height': [170, 180, 160], 'weight': [70, 80, 60], 'gender': ['M', 'M', 'F']})
    height = '175'
    weight = 75
    columns = ['gender', 'height', 'weight']
    with pytest.raises(TypeError):
        task_func(df, height, weight, columns)