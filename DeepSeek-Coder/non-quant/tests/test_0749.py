import pytest
from src_0749 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Create a sample DataFrame
    data = {
        'Age': [25, 30, 35, 40],
        'Weight': [50, 60, 70, 80]
    }
    df = pd.DataFrame(data)

    # Test case 1: Normal case
    result = task_func(df, 30, 65)
    assert result.equals(pd.DataFrame({
        'Age': [25, 30],
        'Weight': [50, 60]
    }))

    # Test case 2: Empty DataFrame
    result = task_func(df, 50, 50)
    assert result.empty

    # Test case 3: Standardization
    result = task_func(df, 30, 65)
    expected_df = pd.DataFrame({
        'Age': [25, 30],
        'Weight': [50, 60]
    })
    pd.testing.assert_frame_equal(result, expected_df)

if __name__ == "__main__":
    pytest.main()