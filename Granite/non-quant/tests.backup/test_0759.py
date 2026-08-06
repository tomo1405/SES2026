import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pytest

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):

    if not isinstance(num_samples, int):
        raise ValueError("num_samples should be an integer.")

    rng = np.random.default_rng(seed=rng_seed)
    countries = rng.choice(countries, num_samples)
    ages = rng.choice(ages, num_samples)
    genders = rng.choice(genders, num_samples)

    le = LabelEncoder()
    encoded_genders = le.fit_transform(genders)

    demographics = pd.DataFrame({
        'Country': countries,
        'Age': ages,
        'Gender': encoded_genders
    })

    return demographics

def test_task_func():
    # Test case 1: num_samples is an integer
    demographics = task_func(num_samples=10)
    assert isinstance(demographics, pd.DataFrame)
    assert demographics.shape == (10, 3)

    # Test case 2: num_samples is not an integer
    with pytest.raises(ValueError):
        task_func(num_samples=10.5)

    # Test case 3: num_samples is negative
    with pytest.raises(ValueError):
        task_func(num_samples=-10)

    # Test case 4: num_samples is zero
    demographics = task_func(num_samples=0)
    assert isinstance(demographics, pd.DataFrame)
    assert demographics.shape == (0, 3)