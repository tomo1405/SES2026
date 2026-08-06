import pytest
from src_0480 import task_func

def test_task_func():
    data_list = ["apple, banana, carrot", "dog, cat, fish", "", ""]
    seed = 0
    df = task_func(data_list, seed)
    assert df["Original String"].tolist() == data_list
    assert df["Modified String"].tolist() != data_list
    assert df["Modified String"].str.contains(", ").all()
    for s in df["Modified String"]:
        substrings = s.split(", ")
        assert all(len(ss) > 0 for ss in substrings)

if __name__ == "__main__":
    pytest.main()