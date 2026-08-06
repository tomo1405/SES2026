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
    df.to_csv('test.csv', index=False)
    matches = task_func('test.csv')
    assert len(matches) == 3
    assert matches.iloc[0]['data'] == '123'
    assert matches.iloc[1]['data'] == '456'
    assert matches.iloc[2]['data'] == '789x'

    # Test case 2: Test with sample_size = 2
    df = pd.DataFrame({'data': ['123', '456', '789x', 'abc']})
    df.to_csv('test.csv', index=False)
    matches = task_func('test.csv', sample_size=2)
    assert len(matches) == 2
    assert matches.iloc[0]['data'] in ['123', '456', '789x', 'abc']
    assert matches.iloc[1]['data'] in ['123', '456', '789x', 'abc']
    assert matches.iloc[0]['data'] != matches.iloc[1]['data']

    # Test case 3: Test with sample_size = 10
    df = pd.DataFrame({'data': ['123', '456', '789x', 'abc']})
    df.to_csv('test.csv', index=False)
    matches = task_func('test.csv', sample_size=10)
    assert len(matches) == 3
    assert matches.iloc[0]['data'] in ['123', '456', '789x', 'abc']
    assert matches.iloc[1]['data'] in ['123', '456', '789x', 'abc']
    assert matches.iloc[2]['data'] in ['123', '456', '789x', 'abc']
    assert matches.iloc[0]['data'] != matches.iloc[1]['data']
    assert matches.iloc[0]['data'] != matches.iloc[2]['data']
    assert matches.iloc[1]['data'] != matches.iloc[2]['data']

    # Test case 4: Test with invalid input file
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.csv')

    # Test case 5: Test with invalid column name
    df = pd.DataFrame({'invalid_column': ['123', '456', '789x', 'abc']})
    df.to_csv('test.csv', index=False)
    with pytest.raises(KeyError):
        task_func('test.csv', column_name='invalid_column')

    # Test case 6: Test with invalid pattern
    df = pd.DataFrame({'data': ['123', '456', '789x', 'abc']})
    df.to_csv('test.csv', index=False)
    with pytest.raises(ValueError):
        task_func('test.csv', pattern='[a-z]+')

    # Test case 7: Test with invalid sample size
    df = pd.DataFrame({'data': ['123', '456', '789x', 'abc']})
    df.to_csv('test.csv', index=False)
    with pytest.raises(ValueError):
        task_func('test.csv', sample_size=-1)

    # Test case 8: Test with invalid seed
    df = pd.DataFrame({'data': ['123', '456', '789x', 'abc']})
    df.to_csv('test.csv', index=False)
    with pytest.raises(ValueError):
        task_func('test.csv', seed='invalid_seed')