python
import random
import string
import pytest

def task_func(max_length, n_samples, seed=None):
    # Handling negative input
    if max_length < 1:
        raise ValueError("max_length must be larger than or equal to 1.")

    # Constants within the function for better encapsulation
    LETTERS = string.ascii_lowercase

    # Setting the seed for the random number generator for reproducibility
    if seed is not None:
        random.seed(seed)

    all_combinations = []

    for i in range(n_samples):
        random_length = random.randint(1, max_length)
        combination = ''.join(random.choices(LETTERS, k=random_length))
        all_combinations.append(combination)

    # Simplifying the reduction using native functionality
    return all_combinations

def test_task_func():
    # Test case 1: max_length = 5, n_samples = 3, seed = None
    assert task_func(5, 3) == ['y', 'z', 'x']

    # Test case 2: max_length = 5, n_samples = 3, seed = 42
    assert task_func(5, 3, seed=42) == ['y', 'z', 'x']

    # Test case 3: max_length = 1, n_samples = 3, seed = None
    with pytest.raises(ValueError):
        task_func(1, 3)

    # Test case 4: max_length = 5, n_samples = 0, seed = None
    with pytest.raises(ValueError):
        task_func(5, 0)

    # Test case 5: max_length = 5, n_samples = 3, seed = "not a number"
    with pytest.raises(TypeError):
        task_func(5, 3, seed="not a number")