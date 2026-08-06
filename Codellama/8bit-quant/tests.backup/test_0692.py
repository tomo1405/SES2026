import pytest
from src_0692 import task_func

def test_task_func():
    # Test case 1: Test that the function returns a numpy array
    df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 10]})
    labels = task_func(df)
    assert isinstance(labels, np.ndarray)

    # Test case 2: Test that the function returns the correct number of clusters
    assert len(labels) == 3

    # Test case 3: Test that the function returns the correct labels
    expected_labels = np.array([0, 1, 2, 0, 1])
    assert np.array_equal(labels, expected_labels)