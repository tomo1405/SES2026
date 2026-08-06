import pandas as pd
import pytest
from sklearn.datasets import make_regression
from src_0365 import task_func


def create_sample_data():
    X, y = make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)
    df = pd.DataFrame(X, columns=['feature '+str(i) for i in range(1, 11)])
    df['target'] = y
    return df

def test_task_func_input_type():
    with pytest.raises(ValueError, match="The input df is not a DataFrame"):
        task_func([1, 2, 3])

def test_task_func_correct_output():
    df = create_sample_data()
    model = task_func(df)
    assert isinstance(model, LinearRegression)
    assert hasattr(model, 'coef_')
    assert hasattr(model, 'intercept_')

def test_task_func_data_split():
    df = create_sample_data()
    X = df[['feature '+str(i) for i in range(1, 11)]]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = task_func(df)
    assert len(X_train) == 80
    assert len(X_test) == 20
    assert len(y_train) == 80
    assert len(y_test) == 20