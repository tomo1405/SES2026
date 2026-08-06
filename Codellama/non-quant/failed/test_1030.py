import pytest
from src_1030 import task_func

def test_task_func():
    rows = 100
    columns = 3
    column_names = [chr(97 + i) for i in range(columns)]
    values = list("abcdefghijklmnopqrstuvwxyz")
    data = np.random.choice(values, size=(rows, columns))
    df = pd.DataFrame(data, columns=column_names)
    assert task_func(rows, columns) == df