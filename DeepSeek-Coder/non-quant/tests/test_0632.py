import pytest
from src_0632 import task_func
import os

@pytest.fixture
def sample_dataframe():
    import pandas as pd
    data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']}
    return pd.DataFrame(data)

def test_task_func(sample_dataframe):
    filename = 'test_output.csv'
    result = task_func(sample_dataframe, filename=filename)
    assert os.path.exists(result)
    os.remove(result)  # Clean up

if __name__ == "__main__":
    pytest.main()