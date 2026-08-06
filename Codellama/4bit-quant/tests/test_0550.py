import pandas as pd
from src_0550 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    base64_string = task_func(df)
    assert base64_string == 'MTIzNDU2Nzg5OjEyMzQ1Ng=='