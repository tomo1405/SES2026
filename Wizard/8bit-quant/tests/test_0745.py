python
import pytest
from src_0745 import task_func

def test_task_func():
    # Test case 1: Valid input
    text = "This is a test string with $100 and $200."
    expected_df = pd.DataFrame([["$100", 1], ["$200", 1]], columns=["Word", "Frequency"])
    assert task_func(text).equals(expected_df)

    # Test case 2: Invalid input (not a string)
    with pytest.raises(ValueError):
        task_func(123)

    # Test case 3: Input with no dollar words
    text = "This is a test string with no dollar words."
    expected_df = pd.DataFrame([], columns=["Word", "Frequency"])
    assert task_func(text).equals(expected_df)