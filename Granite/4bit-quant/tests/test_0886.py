import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    # Validating the input dataframe
    if df.empty or not all(col in df for col in [col_a, col_b, col_c]):
        return None  # Invalid input scenario
    
    try:
        # Ensuring the columns contain numeric data
        df[[col_a, col_b, col_c]] = df[[col_a, col_b, col_c]].apply(pd.to_numeric, errors='raise')
    except ValueError:
        return None  # Non-numeric data encountered

    # Filtering the data based on the conditions
    selected = df[(df[col_b] > 50) & (df[col_c] == 900)][[col_a, col_b]]

    if selected.empty:
        return None
    
    # Preparing the data for linear regression
    X_train, X_test, y_train, _ = train_test_split(selected[col_a].values.reshape(-1, 1),
                                                   selected[col_b].values,
                                                   test_size=0.2,
                                                   random_state=seed)

    # Applying linear regression
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return predictions, model

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [60, 70, 80, 90, 100], 'C': [900, 900, 900, 900, 900]})
    expected_output = ([62.0, 68.0], LinearRegression())
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Empty dataframe
    df = pd.DataFrame()
    expected_output = None
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 2 failed"

    # Test case 3: Non-numeric data
    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'], 'B': [60, 70, 80, 90, 100], 'C': [900, 900, 900, 900, 900]})
    expected_output = None
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 3 failed"

    # Test case 4: No data satisfies the conditions
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [900, 900, 900, 900, 900]})
    expected_output = None
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 4 failed"

if __name__ == "__main__":
    pytest.main()