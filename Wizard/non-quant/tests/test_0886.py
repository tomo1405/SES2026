python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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
    # Test case 1: Valid input dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is not None
    assert model is not None

    # Test case 2: Invalid input dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 3: Non-numeric data in input dataframe
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 'a']})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 4: Empty dataframe
    df = pd.DataFrame({'A': [], 'B': [], 'C': []})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 5: Dataframe with no rows meeting the condition
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [49, 50, 51, 52, 53], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 6: Dataframe with no columns meeting the condition
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'D': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 7: Dataframe with no rows meeting the condition and no columns meeting the condition
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df)
    assert predictions is None
    assert model is None

    # Test case 8: Dataframe with no rows meeting the condition and no columns meeting the condition
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df, col_a='A', col_b='C', col_c='B')
    assert predictions is None
    assert model is None

    # Test case 9: Dataframe with no rows meeting the condition and no columns meeting the condition
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [51, 52, 53, 54, 55], 'C': [900, 900, 900, 900, 900]})
    predictions, model = task_func(df, col_a='A', col_b='B', col_c='C', seed=42)
    assert predictions is not None
    assert model is not None