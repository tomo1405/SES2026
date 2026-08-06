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

# Define a sample DataFrame to use for testing
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 30, 28, 32],
    'Weight': [150, 120, 160, 140]
})

# Test case 1: Select data based on age and weight criteria
selected_df = task_func(df, 30, 140)
assert selected_df.shape == (2, 3)
assert selected_df.columns.tolist() == ['Name', 'Age', 'Weight']

# Test case 2: Select data based on age and weight criteria, and standardize the selected data
selected_df = task_func(df, 30, 140)
scaler = StandardScaler()
expected_df = pd.DataFrame(scaler.fit_transform(selected_df), columns=selected_df.columns)
assert expected_df.equals(selected_df)

# Test case 3: Select an empty DataFrame based on age and weight criteria
selected_df = task_func(df, 35, 150)
assert selected_df.empty