import pytest
from src_1030 import task_func

def test_task_func():
    rows = 100
    columns = 3
    expected_column_names = [
        chr(97 + i) for i in range(columns)
    ]
    expected_values = list("abcdefghijklmnopqrstuvwxyz")
    expected_data = np.random.choice(expected_values, size=(rows, columns))
    expected_df = pd.DataFrame(expected_data, columns=expected_column_names)

    actual_df = task_func(rows, columns)

    assert actual_df.columns.tolist() == expected_column_names
    assert actual_df.values.tolist() == expected_data.tolist()