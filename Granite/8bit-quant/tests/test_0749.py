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
    # Test case 1: Empty DataFrame
    df = pd.DataFrame({'Age': [20, 30, 40], 'Weight': [50, 60, 70]})
    age = 30
    weight = 65
    expected_result = pd.DataFrame(columns=['Age', 'Weight'])
    result = task_func(df, age, weight)
    assert result.equals(expected_result)

    # Test case 2: Non-empty DataFrame
    df = pd.DataFrame({'Age': [20, 30, 40], 'Weight': [50, 60, 70]})
    age = 35
    weight = 55
    expected_result = pd.DataFrame({'Age': [20], 'Weight': [50]})
    result = task_func(df, age, weight)
    assert result.equals(expected_result)

    # Test case 3: Standardization
    df = pd.DataFrame({'Age': [20, 30, 40], 'Weight': [50, 60, 70]})
    age = 35
    weight = 55
    expected_result = pd.DataFrame({'Age': [-1.22474487], 'Weight': [-1.22474487]})
    result = task_func(df, age, weight)
    assert result.equals(expected_result)

if __name__ == '__main__':
    pytest.main()