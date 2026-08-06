from src_0280 import task_func


def test_task_func():
    result, card_counts = task_func()
    assert isinstance(result, list)
    assert all(isinstance(item, list) for item in result)
    assert all(len(item) == 5 for item in result)
    assert all(item in CARDS for item in result)
    assert isinstance(card_counts, dict)
    assert all(isinstance(key, str) for key in card_counts)
    assert all(isinstance(value, int) for value in card_counts.values())
    assert sum(card_counts.values()) == 5 * len(result)