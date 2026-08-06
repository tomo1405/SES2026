import pytest
from src_0222 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [1, 2, 3, 4, 5], 'feature3': [1, 2, 3, 4, 5], 'feature4': [1, 2, 3, 4, 5], 'feature5': [1, 2, 3, 4, 5]})
    dct = {'feature1': 10, 'feature2': 20, 'feature3': 30, 'feature4': 40, 'feature5': 50}
    expected_statistics = {'feature1': {'mean': 10, 'median': 10, 'mode': 10, 'variance': 0}, 'feature2': {'mean': 20, 'median': 20, 'mode': 20, 'variance': 0}, 'feature3': {'mean': 30, 'median': 30, 'mode': 30, 'variance': 0}, 'feature4': {'mean': 40, 'median': 40, 'mode': 40, 'variance': 0}, 'feature5': {'mean': 50, 'median': 50, 'mode': 50, 'variance': 0}}
    assert task_func(df, dct) == expected_statistics

    # Test case 2: Test with invalid input
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [1, 2, 3, 4, 5], 'feature3': [1, 2, 3, 4, 5], 'feature4': [1, 2, 3, 4, 5], 'feature5': [1, 2, 3, 4, 5]})
    dct = {'feature1': 10, 'feature2': 20, 'feature3': 30, 'feature4': 40, 'feature5': 50}
    expected_statistics = "Invalid input"
    assert task_func(df, dct) == expected_statistics

if __name__ == '__main__':
    pytest.main()