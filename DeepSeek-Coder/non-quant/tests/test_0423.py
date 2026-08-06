import pytest
from src_0423 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split

# Define the test cases
def test_task_func():
    # Create a sample DataFrame
    data = {
        'a': [1, 2, 3, 4, 5],
        'b': [5, 4, 3, 2, 1],
        'c': ['x', 'y', 'z', 'w', 'v']
    }
    df = pd.DataFrame(data)
    
    # Call the function with the sample DataFrame
    X_train, X_test, y_train, y_test = task_func(df=df, target_column='b', column_to_remove='c', test_size=0.2)
    
    # Assertions to check the output
    assert isinstance(X_train, pd.DataFrame)
    assert isinstance(X_test, pd.DataFrame)
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)
    assert len(X_train) + len(X_test) == len(df)
    assert len(set(df.columns) - {'c'}) == len(df.columns) - 1

# Run the test
if __name__ == "__main__":
    pytest.main()