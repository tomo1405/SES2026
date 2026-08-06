import pytest
from src_1087 import task_func
import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples

def test_task_func():
    data = {
        "String Field": [
            "".join(random.choices(string.ascii_letters, k=10))
            for _ in range(NUM_SAMPLES)
        ],
        "Float Field": [f"{x:,.2f}" for x in np.random.uniform(0, 10000, NUM_SAMPLES)],
    }

    df = pd.DataFrame(data)

    result = task_func()

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (NUM_SAMPLES, 2)
    assert result.columns.tolist() == ["String Field", "Float Field"]