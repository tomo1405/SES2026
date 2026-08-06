import pytest
from src_0127 import task_func
import pandas as pd
import numpy as np
import statistics
from random import randint, seed as random_seed

def test_task_func():
    # Test with default seed
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) > 0, "The DataFrame should not be empty"
    assert set(result.columns) == {'Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'}, "Columns are not as expected"

    # Test with custom seed
    result_custom_seed = task_func(seed=123)
    assert result != result_custom_seed, "The function should produce different results with different seeds"

    # Test with custom animals
    custom_animals = ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    result_custom_animals = task_func(animals=custom_animals)
    assert len(result_custom_animals) > 0, "The DataFrame should not be empty"

    # Test with empty animals
    empty_result = task_func(animals=[])
    assert len(empty_result) == 0, "The DataFrame should be empty for an empty list of animals"

    # Test with invalid input
    with pytest.raises(TypeError):
        task_func(seed="invalid_seed")