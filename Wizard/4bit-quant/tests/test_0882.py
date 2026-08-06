python
import pandas as pd
import random
import pytest

def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    df = pd.read_csv(csv_file)
    matches = df[df[column_name].str.contains(pattern, na=False)]

    if sample_size is not None:
        random.seed(seed)  # Set the seed for reproducibility
        sample_size = min(sample_size, len(matches))  # Ensure sample size is not greater than the number of matches
        sampled_indices = random.sample(range(len(matches)), sample_size)  # Randomly select indices
        matches = matches.iloc[sampled_indices]  # Select rows corresponding to sampled indices

    return matches

def test_task_func():
    # Test case 1: Test with sample_size = None
    df = pd.DataFrame({'data': ['123x', '456X', '789x', '1011x']})
    matches = task_func(df, sample_size=None)
    assert len(matches) == 4

    # Test case 2: Test with sample_size = 2
    matches = task_func(df, sample_size=2)
    assert len(matches) == 2

    # Test case 3: Test with sample_size = 10
    matches = task_func(df, sample_size=10)
    assert len(matches) == 4

    # Test case 4: Test with invalid input type for sample_size
    with pytest.raises(TypeError):
        task_func(df, sample_size='2')

    # Test case 5: Test with invalid input value for sample_size
    with pytest.raises(ValueError):
        task_func(df, sample_size=-1)

    # Test case 6: Test with invalid input type for seed
    with pytest.raises(TypeError):
        task_func(df, seed='42')

    # Test case 7: Test with invalid input value for seed
    with pytest.raises(ValueError):
        task_func(df, seed=-1)