import pytest
from src_0237 import task_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def test_task_func():
    # Create a sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 88, 92],
        'Category': ['A', 'B', 'A', 'B']
    }
    df = pd.DataFrame(data)

    # Call the function with the sample DataFrame
    result = task_func(df)

    # Assert the result (assuming a valid accuracy score)
    assert result > 0.5  # Placeholder assertion

if __name__ == "__main__":
    pytest.main()