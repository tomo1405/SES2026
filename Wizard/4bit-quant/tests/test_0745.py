python
import pytest
from src_0745 import task_func

def test_task_func():
    # Test case 1: Valid input
    text = "I have $100 in my pocket."
    expected_df = pd.DataFrame([["$100", 1]], columns=["Word", "Frequency"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid input (not a string)
    with pytest.raises(ValueError):
        task_func(123)

    # Test case 3: Empty input
    text = ""
    expected_df = pd.DataFrame([], columns=["Word", "Frequency"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

    # Test case 4: Input with no dollar words
    text = "I have no money in my pocket."
    expected_df = pd.DataFrame([], columns=["Word", "Frequency"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

    # Test case 5: Input with multiple dollar words
    text = "I have $100, $200, and $300 in my pocket."
    expected_df = pd.DataFrame([["$100", 1], ["$200", 1], ["$300", 1]], columns=["Word", "Frequency"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

    # Test case 6: Input with multiple dollar words and punctuation
    text = "I have $100, $200, and $300 in my pocket! How about $400?"
    expected_df = pd.DataFrame([["$100", 1], ["$200", 1], ["$300", 1]], columns=["Word", "Frequency"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)

    # Test case 7: Input with multiple dollar words and capitalization
    text = "I have $100, $200, and $300 in my pocket! How about $400? $500."
    expected_df = pd.DataFrame([["$100", 1], ["$200", 1], ["$300", 1], ["$400", 1], ["$500", 1]], columns=["Word", "Frequency"])
    actual_df = task_func(text)
    assert actual_df.equals(expected_df)