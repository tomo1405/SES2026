import pandas as pd
from src_0694 import task_func


def test_task_func():
    tuples_list = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]
    columns = ['a', 'b', 'c']
    df = pd.DataFrame(tuples_list, columns=columns)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    assert df_scaled.equals(task_func(tuples_list, columns))