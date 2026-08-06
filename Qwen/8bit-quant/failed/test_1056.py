import pytest
from src_1056 import task_func

def test_task_func():
    colors = ['Red', 'Blue', 'Green']
    states = ['California', 'Texas', 'New York']

    df = task_func(colors, states)

    # Check if the DataFrame has the correct number of columns
    assert len(df.columns) == min(len(colors), len(states))

    # Check if the DataFrame has the correct number of rows
    assert len(df) == len(colors) * len(states)

    # Check if the DataFrame contains the correct data
    expected_combinations = [
        'Red:California', 'Red:Texas', 'Red:New York',
        'Blue:California', 'Blue:Texas', 'Blue:New York',
        'Green:California', 'Green:Texas', 'Green:New York'
    ]
    for col in df.columns:
        assert all(item in expected_combinations for item in df[col])

    # Check if the DataFrame is shuffled correctly
    # Since random.seed(42) is used, we can check against a known shuffled order
    expected_shuffled_order = [
        'Green:California', 'Blue:Texas', 'Red:New York',
        'Red:California', 'Green:Texas', 'Blue:New York',
        'Blue:California', 'Red:Texas', 'Green:New York'
    ]
    for i, col in enumerate(df.columns):
        assert df[col].tolist() == expected_shuffled_order[i::3]

if __name__ == "__main__":
    pytest.main()