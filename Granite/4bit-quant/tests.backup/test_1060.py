import pytest
import numpy as np
import random
import itertools
import pandas as pd
from src_1060 import task_func

def test_task_func():
    # Generate all possible pairs
    pairs = [
        f"{planet}:{element}"
        for planet, element in itertools.product(PLANETS, ELEMENTS)
    ]
    # Shuffle the pairs to ensure randomness
    random.shuffle(pairs)

    # Convert the list of pairs into a numpy array, then reshape it to fit the DataFrame dimensions
    data = np.array(pairs).reshape(len(PLANETS), len(ELEMENTS))
    # Create the DataFrame with ELEMENTS as column headers
    df = pd.DataFrame(data, columns=ELEMENTS)

    assert task_func().equals(df)

def test_task_func_shape():
    assert task_func().shape == (len(PLANETS), len(ELEMENTS))

def test_task_func_columns():
    assert task_func().columns.tolist() == ELEMENTS