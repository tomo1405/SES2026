import pytest
from src_0232 import task_func

@pytest.fixture
def obj_list():
    class ValueObject:
        value = 0
        def __init__(self, mu=0, std=1, seed=77):
            random.seed(seed)
            self.value = random.gauss(mu, std)
    return [ValueObject() for _ in range(10)]

def test_task_func_with_empty_list(obj_list):
    ax = task_func([])
    assert ax.get_title() == "Fit results: mu = 0.00,  std = 0.00"

def test_task_func_with_non_empty_list(obj_list):
    ax = task_func(obj_list)
    assert ax.get_title().startswith("Fit results: mu =")

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func("invalid input")