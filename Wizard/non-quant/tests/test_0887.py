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
    data = {'Name': ['John', 'Jane', 'John'], 'Age': [25, 30, 25], 'Score': [80, 90, 70]}
    df, avg_scores, most_common_age = task_func(data)
    assert df.shape == (3, 3)
    assert avg_scores.shape == (2,)
    assert most_common_age == 25

    # Test case 2: Missing key
    data = {'Name': ['John', 'Jane', 'John'], 'Age': [25, 30, 25], 'Score': [80, 90, 70], 'Gender': ['M', 'F', 'M']}
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 3: Empty input
    data = {}
    with pytest.raises(ValueError):
        task_func(data)