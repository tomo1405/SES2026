import pytest
from src_1101 import task_func

def test_task_func():
    texts = ["This is a test", "Another test", "A third test"]
    expected_output = [
        ([(0.2, 0.2, 0.2), (0.2, 0.2, 0.2), (0.2, 0.2, 0.2)], ['a', 'another', 'test']),
        ([(0.4, 0.4), (0.4, 0.4), (0.4, 0.4)], ['a', 'third']),
        ([(0.6, 0.6, 0.6), (0.6, 0.6, 0.6), (0.6, 0.6, 0.6)], ['is', 'this'])
    ]

    for i, text in enumerate(texts):
        output = task_func([text] * 3)
        assert output == expected_output[i], f"Test failed for input: {text}"

    assert task_func([""] * 3) == ([], []), "Test failed for empty input"

if __name__ == "__main__":
    pytest.main()