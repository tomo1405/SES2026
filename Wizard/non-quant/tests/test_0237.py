python
import pandas as pd
import pytest
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

def test_task_func():
    # Test case 1
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    assert task_func(df) == 0.5
    
    # Test case 2
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    assert task_func(df, test_size=0.3) == 0.5
    
    # Test case 3
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    assert task_func(df, random_state=10) == 0.5
    
    # Test case 4
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    assert task_func(df, test_size=0.3, random_state=10) == 0.5
    
    # Test case 5
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    with pytest.raises(ValueError):
        task_func(123)
    
    # Test case 6
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    with pytest.raises(ValueError):
        task_func(df, test_size='abc')
    
    # Test case 7
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    with pytest.raises(ValueError):
        task_func(df, random_state='abc')
    
    # Test case 8
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 25, 40], 'Score': [85, 90, 75, 60], 'Category': ['A', 'B', 'A', 'C']})
    with pytest.raises(ValueError):
        task_func(df, test_size=0.3, random_state='abc')