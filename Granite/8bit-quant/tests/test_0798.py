import re
import pandas as pd
from src_0798 import task_func

def test_task_func():
    # Test case 1: df is a DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert task_func(df) == 0

    # Test case 2: df is not a DataFrame
    with pytest.raises(TypeError) as excinfo:
        task_func([1, 2, 3])
    assert "df should be a DataFrame." in str(excinfo.value)

    # Test case 3: df has nested brackets
    df = pd.DataFrame({'A': ['{{}', '[]', '()']})
    assert task_func(df) == 6

    # Test case 4: df has no brackets
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    assert task_func(df) == 0