python
import pandas as pd
from collections import Counter
import pytest

def task_func(data):

    if not all(key in data for key in ['Name', 'Age', 'Score']):
        raise ValueError("The dictionary must have the keys 'Name', 'Age', 'Score'")

    # Creating a dataframe and sorting it
    df = pd.DataFrame(data).sort_values(['Name', 'Age'])

    # Calculating average scores
    avg_scores = df.groupby('Name')['Score'].mean()

    # Getting the most common age
    age_counts = Counter(df['Age'])
    most_common_age = age_counts.most_common(1)[0][0] if age_counts else None

    return df, avg_scores, most_common_age

def test_task_func():
    # Test case 1: Valid input
    data = {'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 20], 'Score': [80, 90, 70]}
    expected_df = pd.DataFrame({'Name': ['Bob', 'Jane', 'John'], 'Age': [20, 30, 25], 'Score': [70, 90, 80]})
    expected_avg_scores = pd.Series({'Bob': 70.0, 'Jane': 90.0, 'John': 80.0})
    expected_most_common_age = 20
    df, avg_scores, most_common_age = task_func(data)
    assert df.equals(expected_df)
    assert avg_scores.equals(expected_avg_scores)
    assert most_common_age == expected_most_common_age

    # Test case 2: Missing key
    data = {'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 20], 'Score': [80, 90]}
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 3: Empty input
    data = {}
    with pytest.raises(ValueError):
        task_func(data)