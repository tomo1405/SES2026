import pytest
from src_0699 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)

    # Expected split sizes
    expected_train_size = 3
    expected_test_size = 2

    # Call the function
    X_train, X_test, y_train, y_test = task_func(df)

    # Check the sizes of the splits
    assert len(X_train) == expected_train_size
    assert len(X_test) == expected_test_size
    assert len(y_train) == expected_train_size
    assert len(y_test) == expected_test_size

    # Check that the splits are correct
    combined_X = pd.concat([X_train, X_test])
    combined_y = pd.concat([y_train, y_test])

    assert combined_X.equals(df.drop('target', axis=1))
    assert combined_y.equals(df['target'])

    # Check that the random_state ensures reproducibility
    X_train_1, _, y_train_1, _ = task_func(df)
    X_train_2, _, y_train_2, _ = task_func(df)

    assert X_train_1.equals(X_train_2)
    assert y_train_1.equals(y_train_2)