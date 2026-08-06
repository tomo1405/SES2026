python
import pickle
import os
import pytest

def task_func(df, file_name="save.pkl"):
    with open(file_name, "wb") as file:
        pickle.dump(df, file)

    with open(file_name, "rb") as file:
        loaded_df = pickle.load(file)

    os.remove(file_name)

    return loaded_df

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    loaded_df = task_func(df)
    assert loaded_df.equals(df)