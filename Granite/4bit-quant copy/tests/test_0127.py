import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
def task_func(animals=None, seed=42):
    random_seed(seed)
    animals = animals or ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    report_data = []

    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        mode = statistics.mode(counts)
        std_dev = np.std(counts)
        report_data.append([animal, mean, median, mode, std_dev])
    
    report_df = pd.DataFrame(report_data, columns=['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation'])

    return report_df
import pytest

def test_task_func():
    # Test case 1: Default arguments
    report_df = task_func()
    assert report_df.shape == (5, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda']
    
    # Test case 2: Custom arguments
    animals = ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda', 'Monkey']
    seed = 123
    report_df = task_func(animals=animals, seed=seed)
    assert report_df.shape == (6, 5)
    assert report_df.columns.tolist() == ['Animal', 'Mean', 'Median', 'Mode', 'Standard Deviation']
    assert report_df['Animal'].tolist() == ['Lion', 'Elephant', 'Tiger', 'Giraffe', 'Panda', 'Monkey']

if __name__ == '__main__':
    pytest.main()