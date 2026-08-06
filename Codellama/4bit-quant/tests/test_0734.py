import pytest
from src_0734 import task_func

def test_task_func():
    assert task_func("Hello World!") == 2
    assert task_func("The quick brown fox jumps over the lazy dog.") == 9
    assert task_func("") == 0
    assert task_func("a b c d e f g h i j k l m n o p q r s t u v w x y z") == 26
    assert task_func("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z") == 52

if __name__ == "__main__":
    pytest.main()