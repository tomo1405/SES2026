import pandas as pd
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
import pytest
def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert len(predictions) == len(X_test)
    assert isinstance(model, LinearRegression)

    # Test case 2: Invalid input (empty dataframe)
    df = pd.DataFrame()
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 3: Invalid input (non-numeric data)
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['a', 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 4: Invalid input (missing column)
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 5: No data after filtering
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [100, 100, 100, 100, 100]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None