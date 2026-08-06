import pandas as pd
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df, age, weight):
    selected_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # Check if the selected DataFrame is empty
    if selected_df.empty:
        return selected_df

    # Standardizing the selected data
    scaler = StandardScaler()
    selected_df = pd.DataFrame(scaler.fit_transform(selected_df), columns=selected_df.columns)

    return selected_df

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'Age': [25, 30, 35, 40, 45],
        'Weight': [70, 80, 90, 100, 110]
    })

    # Test case 1: No data should be selected
    selected_df = task_func(df, 30, 80)
    assert selected_df.empty

    # Test case 2: Data should be selected and standardized
    selected_df = task_func(df, 40, 90)
    expected_df = pd.DataFrame({
        'Age': [0.0, 0.5, 1.0, 1.5, 2.0],
        'Weight': [-1.22474487, -0.63245553, 0.0, 0.63245553, 1.22474487]
    })
    assert selected_df.equals(expected_df)

if __name__ == '__main__':
    pytest.main()