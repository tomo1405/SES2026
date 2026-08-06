python
import pytest
from src_0221 import task_func

@pytest.mark.parametrize("colors", [
    ["red", "green", "blue"],
    ["yellow", "orange", "purple"],
    ["black", "white", "gray"],
    ["pink", "brown", "tan"],
    ["cyan", "magenta", "gold"]
])
def test_task_func(colors):
    task_func(colors)