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
    df = pd.DataFrame({'data': ['123', '456', '789x', 'abc']})
    matches = task_func(df, sample_size=None)
    assert len(matches) == 4

    # Test case 2: Test with sample_size = 2
    matches = task_func(df, sample_size=2)
    assert len(matches) == 2

    # Test case 3: Test with sample_size = 5
    matches = task_func(df, sample_size=5)
    assert len(matches) == 4

    # Test case 4: Test with sample_size = 10
    matches = task_func(df, sample_size=10)
    assert len(matches) == 4

    # Test case 5: Test with invalid input type for sample_size
    with pytest.raises(TypeError):
        task_func(df, sample_size='a')

    # Test case 6: Test with invalid input type for csv_file
    with pytest.raises(TypeError):
        task_func(123, sample_size=None)

    # Test case 7: Test with invalid input type for column_name
    with pytest.raises(TypeError):
        task_func(df, column_name=123, sample_size=None)

    # Test case 8: Test with invalid input type for pattern
    with pytest.raises(TypeError):
        task_func(df, pattern=123, sample_size=None)

    # Test case 9: Test with invalid input type for seed
    with pytest.raises(TypeError):
        task_func(df, seed='a', sample_size=None)