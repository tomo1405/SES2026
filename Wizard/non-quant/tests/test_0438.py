python
import pytest
import pickle
import os

def task_func(df, file_name="save.pkl"):
    with open(file_name, "wb") as file:
        pickle.dump(df, file)

    with open(file_name, "rb") as file:
        loaded_df = pickle.load(file)

    os.remove(file_name)

    return loaded_df

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    task_func(df)
    assert os.path.isfile('save.pkl')
    os.remove('save.pkl')