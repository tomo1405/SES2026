from src_0557 import task_func


def test_task_func_min_length():
    s = "example"
    min_length = 5
    max_length = 10
    letters = "abcdefghijklmnopqrstuvwxyz"
    generated_s, is_similar = task_func(s, min_length, max_length, letters)
    assert len(generated_s) >= min_length

def test_task_func_max_length():
    s = "example"
    min_length = 5
    max_length = 10
    letters = "abcdefghijklmnopqrstuvwxyz"
    generated_s, is_similar = task_func(s, min_length, max_length, letters)
    assert len(generated_s) <= max_length

def test_task_func_letters():
    s = "example"
    min_length = 5
    max_length = 10
    letters = "xyz"
    generated_s, is_similar = task_func(s, min_length, max_length, letters)
    assert all(char in letters for char in generated_s)

def test_task_func_similarity():
    s = "example"
    min_length = 5
    max_length = 10
    letters = "abcdefghijklmnopqrstuvwxyz"
    generated_s, is_similar = task_func(s, min_length, max_length, letters)
    similarity = SequenceMatcher(None, s, generated_s).ratio()
    assert is_similar == (similarity >= 0.5)

def test_task_func_randomness():
    s = "example"
    min_length = 5
    max_length = 10
    letters = "abcdefghijklmnopqrstuvwxyz"
    results = [task_func(s, min_length, max_length, letters) for _ in range(10)]
    generated_ss = [result[0] for result in results]
    assert len(set(generated_ss)) > 1, "Generated strings should be different due to randomness"