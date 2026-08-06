import pytest
from src_0849 import task_func

@pytest.fixture
def example_data():
    return [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 30},
        {'id': 4, 'value': 40},
        {'id': 5, 'value': 50}
    ]

def test_task_func(example_data):
    obj_list = example_data
    attr = 'value'
    top_n = 3
    seed = 42

    top_values, random_value = task_func(obj_list=obj_list, attr=attr, top_n=top_n, seed=seed)

    assert isinstance(top_values, list)
    assert isinstance(random_value, int)
    assert len(top_values) == min(top_n, len(obj_list))
    assert len(set(top_values)) == len(top_values)
    assert random_value in [obj[attr] for obj in obj_list]

if __name__ == "__main__":
    pytest.main()