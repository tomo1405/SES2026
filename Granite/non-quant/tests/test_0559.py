import pandas as pd
from src_0559 import task_func


def test_task_func():
    a = [1, 2, 3]
    b = [4, 5, 6]
    columns = ['A', 'B']
    expected_df = pd.DataFrame([[1.0, -1.22474487], [2.0, -0.61237244], [3.0, 0.0]], columns=columns)
    expected_ax = expected_df.plot(kind='bar')

    df, ax = task_func(a, b, columns)

    assert df.equals(expected_df)
    assert ax == expected_ax