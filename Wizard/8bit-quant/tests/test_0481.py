python
import pytest
from src_0481 import task_func

def test_task_func():
    data_list = ["apple, banana, cherry", "orange, peach, plum", "grape, lemon, melon"]
    expected_df = pd.DataFrame(
        {
            "Original String": ["apple, banana, cherry", "orange, peach, plum", "grape, lemon, melon"],
            "Shuffled String": ["cherry, apple, banana", "plum, peach, orange", "lemon, grape, melon"],
        }
    )
    result_df = task_func(data_list)
    pd.testing.assert_frame_equal(result_df, expected_df)