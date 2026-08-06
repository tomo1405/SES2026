import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def task_func(df, test_size=0.2, random_state=42):

    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    
    df = df.drop_duplicates(subset='Name')

    X = df[['Age', 'Score']]
    y = df['Category']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = RandomForestClassifier(random_state=random_state)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    return accuracy
import pytest
def test_task_func():
    df = pd.DataFrame({'Name': ['John', 'Jane', 'John'],
                       'Age': [25, 30, 25],
                       'Score': [80, 90, 80],
                       'Category': ['A', 'B', 'A']})
    with pytest.raises(ValueError):
        task_func(df)
    df = pd.DataFrame({'Name': ['John', 'Jane', 'John'],
                       'Age': [25, 30, 25],
                       'Score': [80, 90, 80],
                       'Category': ['A', 'B', 'A']})
    accuracy = task_func(df)
    assert 0 <= accuracy <= 1
def test_task_func_2():
    df = pd.DataFrame({'Name': ['John', 'Jane', 'John'],
                       'Age': [25, 30, 25],
                       'Score': [80, 90, 80],
                       'Category': ['A', 'B', 'A']})
    accuracy = task_func(df)
    assert accuracy == 1.0
def test_task_func_3():
    df = pd.DataFrame({'Name': ['John', 'Jane', 'John'],
                       'Age': [25, 30, 25],
                       'Score': [80, 90, 80],
                       'Category': ['A', 'B', 'A']})
    accuracy = task_func(df)
    assert accuracy == 1.0