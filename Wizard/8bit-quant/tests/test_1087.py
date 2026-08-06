python
import string
import random
import pandas as pd
import numpy as np
import pytest

# Constants
NUM_SAMPLES = 1000  # Number of samples

def task_func():
    data = {
        "String Field": [
            "".join(random.choices(string.ascii_letters, k=10))
            for _ in range(NUM_SAMPLES)
        ],
        "Float Field": [f"{x:,.2f}" for x in np.random.uniform(0, 10000, NUM_SAMPLES)],
    }

    df = pd.DataFrame(data)

    return df

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == NUM_SAMPLES
    assert df.shape[1] == 2
    assert df.dtypes["String Field"] == object
    assert df.dtypes["Float Field"] == object