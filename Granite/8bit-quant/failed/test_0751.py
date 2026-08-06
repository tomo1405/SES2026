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
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    columns = ['height', 'weight', 'age']
    height = 180
    weight = 80
    expected_result = None
    actual_result = task_func(df, height, weight, columns)
    assert actual_result == expected_result

    # Test case 2: No rows match the condition
    df = pd.DataFrame({
        'height': [170, 180, 190],
        'weight': [70, 80, 90],
        'age': [25, 30, 35]
    })
    columns = ['height', 'weight', 'age']
    height = 180
    weight = 80
    expected_result = None
    actual_result = task_func(df, height, weight, columns)
    assert actual_result == expected_result

    # Test case 3: Valid input
    df = pd.DataFrame({
        'height': [170, 180, 190, 200],
        'weight': [70, 80, 90, 100],
        'age': [25, 30, 35, 40]
    })
    columns = ['height', 'weight', 'age']
    height = 180
    weight = 80
    expected_result = <statsmodels.regression.linear_model.RegressionResultsWrapper object at 0x7f8d2d28d510>
    actual_result = task_func(df, height, weight, columns)
    assert actual_result == expected_result

if __name__ == '__main__':
    pytest.main()