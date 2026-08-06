import pytest
from src_0569 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([lambda x: x])

    df = task_func([lambda x, y: x + y, lambda x, y, z: x * y * z])
    assert df.loc['<lambda>', 'Number of Arguments'] == 2
    assert df.loc['<lambda>', 'Number of Arguments'] == 3