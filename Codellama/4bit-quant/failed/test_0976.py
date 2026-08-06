import pytest
from src_0976 import task_func

def test_task_func():
    rows = 5
    columns = ["A", "B", "C", "D", "E"]
    seed = 0
    expected_columns = ["A", "B", "C", "D", "E"]
    expected_data = np.random.rand(rows, len(expected_columns))
    np.random.seed(seed)
    np.random.shuffle(expected_columns)
    expected_df = pd.DataFrame(expected_data, columns=expected_columns)
    actual_df = task_func(rows, columns, seed)
    assert actual_df.equals(expected_df)