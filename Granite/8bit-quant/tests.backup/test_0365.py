import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pytest import raises

# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'

def task_func(df):

    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def test_task_func():
    # Test case 1: input is not a DataFrame
    df = 'not a DataFrame'
    with raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "The input df is not a DataFrame"

    # Test case 2: input is a DataFrame with correct shape
    df = pd.DataFrame({col: [i for i in range(10)] for col in FEATURES+[TARGET]})
    model = task_func(df)
    assert isinstance(model, LinearRegression)

    # Test case 3: input is a DataFrame with incorrect shape
    df = pd.DataFrame({col: [i for i in range(11)] for col in FEATURES+[TARGET]})
    with raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "The input df is not a DataFrame"