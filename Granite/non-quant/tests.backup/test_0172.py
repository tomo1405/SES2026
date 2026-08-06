import pytest
from src_0172 import task_func

def test_task_func():
    vegetable_dict = {'Carrot': 5, 'Potato': 3, 'Tomato': 7, 'Cabbage': 2, 'Spinach': 4}
    seed = 0
    expected_output = pd.DataFrame({
        'Vegetable': ['Tomato', 'Carrot', 'Spinach', 'Potato', 'Cabbage'],
        'Count': [7, 5, 4, 3, 2],
        'Percentage': [70.0, 50.0, 40.0, 30.0, 20.0]
    })

    random.seed(seed)
    actual_output = task_func(vegetable_dict, seed)

    assert actual_output.equals(expected_output)