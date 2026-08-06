import pytest
from src_1071 import task_func

def test_task_func():
    list_of_lists = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dataframes = task_func(list_of_lists)

    assert len(dataframes) == 3
    assert all(isinstance(df, pd.DataFrame) for df in dataframes)
    assert all(df.shape[0] == 3 for df in dataframes)
    assert all(df.shape[1] == 3 for df in dataframes)
    assert all(df.columns.to_list() == list_of_lists[i] for i, df in enumerate(dataframes))
    assert all(df.index.to_list() == list(range(3)) for df in dataframes)
    assert all(df.values.tolist() == [POSSIBLE_VALUES.copy() for _ in range(3)] for df in dataframes)