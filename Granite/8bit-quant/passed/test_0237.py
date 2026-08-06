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
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 28, 32],
        'Score': [80, 90, 95, 85],
        'Category': ['A', 'B', 'A', 'B']
    })
    accuracy = task_func(df)
    assert accuracy >= 0 and accuracy <= 1, "Accuracy should be between 0 and 1"
def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('invalid input')