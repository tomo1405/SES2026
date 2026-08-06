python
import pandas as pd
import numpy as np
import pytest
from src_0753 import task_func

def test_task_func():
    # Test case 1: data is not a DataFrame
    with pytest.raises(ValueError):
        task_func(123, "target_column")

    # Test case 2: data is empty
    with pytest.raises(ValueError):
        task_func(pd.DataFrame(), "target_column")

    # Test case 3: target_column not in data
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]}), "target_column")

    # Test case 4: data values are not numeric
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]}), "col2")

    # Test case 5: test_size is not between 0 and 1
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]}), "col2", test_size=2)

    # Test case 6: random_state is not an integer
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]}), "col2", random_state="abc")

    # Test case 7: valid input
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    assert task_func(data, "col2") == 1.0