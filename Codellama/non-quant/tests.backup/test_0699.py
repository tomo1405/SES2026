import pytest
from src_0699 import task_func

def test_task_func():
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [6, 7, 8, 9, 10], 'target': [11, 12, 13, 14, 15]})
    X_train, X_test, y_train, y_test = task_func(df)

    assert X_train.shape == (3, 2)
    assert X_test.shape == (2, 2)
    assert y_train.shape == (3,)
    assert y_test.shape == (2,)

    assert X_train.equals(pd.DataFrame({'feature1': [1, 2, 3], 'feature2': [6, 7, 8]}, index=[0, 1, 2]))
    assert X_test.equals(pd.DataFrame({'feature1': [4, 5], 'feature2': [9, 10]}, index=[3, 4]))
    assert y_train.equals(pd.Series([11, 12, 13], index=[0, 1, 2]))
    assert y_test.equals(pd.Series([14, 15], index=[3, 4]))