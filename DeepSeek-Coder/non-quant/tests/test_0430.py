import pytest
from src_0430 import task_func
import pandas as pd
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_classif

# Define test cases
def test_task_func():
    # Create sample data
    data = {
        'id': [1, 2, 3, 4, 5],
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'feature1': [1, 2, 3, 4, 5],
        'target': [0, 1, 0, 1, 0]
    })

    # Call the function
    result = task_func(df1, df2)

    # Assertions
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert len(result[0]) == 2  # Check the number of selected features
    assert isinstance(result[1], sns.heatmap)  # Check if heatmap is returned

# Run the tests
if __name__ == "__main__":
    pytest.main()