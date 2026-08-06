import pytest
from src_0887 import task_func

def test_task_func():
    # Test case 1: Basic functionality with valid input
    data = [
        {'Name': 'Alice', 'Age': 25, 'Score': 85},
        {'Name': 'Bob', 'Age': 30, 'Score': 90},
        {'Name': 'Alice', 'Age': 25, 'Score': 95}
    ]
    df, avg_scores, most_common_age = task_func(data)
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(avg_scores, pd.Series)
    assert isinstance(most_common_age, int)
    
    assert df.equals(pd.DataFrame(data).sort_values(['Name', 'Age']))
    assert avg_scores.equals(pd.Series({'Alice': 90.0, 'Bob': 90.0}))
    assert most_common_age == 25

    # Test case 2: Check for correct average scores calculation
    data = [
        {'Name': 'Alice', 'Age': 25, 'Score': 85},
        {'Name': 'Alice', 'Age': 25, 'Score': 95},
        {'Name': 'Bob', 'Age': 30, 'Score': 100}
    ]
    df, avg_scores, most_common_age = task_func(data)
    
    assert avg_scores.equals(pd.Series({'Alice': 90.0, 'Bob': 100.0}))

    # Test case 3: Check for correct most common age calculation
    data = [
        {'Name': 'Alice', 'Age': 25, 'Score': 85},
        {'Name': 'Bob', 'Age': 30, 'Score': 90},
        {'Name': 'Alice', 'Age': 25, 'Score': 95},
        {'Name': 'Bob', 'Age': 30, 'Score': 100}
    ]
    df, avg_scores, most_common_age = task_func(data)
    
    assert most_common_age == 25

    # Test case 4: Check for ValueError when missing keys
    data_missing_key = [
        {'Name': 'Alice', 'Age': 25},
        {'Name': 'Bob', 'Age': 30, 'Score': 90}
    ]
    with pytest.raises(ValueError):
        task_func(data_missing_key)

    # Test case 5: Check for empty input list
    data_empty = []
    with pytest.raises(ValueError):
        task_func(data_empty)