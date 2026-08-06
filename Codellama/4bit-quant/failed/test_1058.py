import pytest
from src_1058 import task_func

def test_task_func():
    # Test with default lists
    df = task_func()
    assert df.shape == (10, 6)
    assert df.columns.tolist() == ["Meat", "Fish", "Grass", "Fruits", "Insects", "Seeds"]
    assert df.index.tolist() == ["Dog", "Cat", "Elephant", "Tiger", "Lion", "Zebra", "Giraffe", "Bear", "Monkey", "Kangaroo"]

    # Test with custom lists
    df = task_func(animals=["Dog", "Cat"], foods=["Meat", "Fish"])
    assert df.shape == (2, 2)
    assert df.columns.tolist() == ["Meat", "Fish"]
    assert df.index.tolist() == ["Dog", "Cat"]

    # Test with empty lists
    df = task_func(animals=[], foods=[])
    assert df.shape == (0, 0)

if __name__ == "__main__":
    pytest.main()