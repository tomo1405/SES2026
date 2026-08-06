import pandas as pd
from itertools import combinations
from pytest import raises

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    if not 0 <= percentage <= 1:
        raise ValueError('Percentage must be between 0 and 1')
    df = pd.DataFrame(data, columns=cols)
    corr_matrix = df.corr().abs()
    columns = corr_matrix.columns
    corr_combinations = []

    for col1, col2 in combinations(columns, 2):
        if corr_matrix.loc[col1, col2] > percentage:
            corr_combinations.append((col1, col2))

    return corr_combinations

# Test cases
def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 0.5
    expected_corr_combinations = [('A', 'B'), ('A', 'C'), ('B', 'C')]
    actual_corr_combinations = task_func(data, cols, percentage)
    assert actual_corr_combinations == expected_corr_combinations

def test_task_func_invalid_percentage():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cols = ['A', 'B', 'C']
    percentage = 1.5
    with raises(ValueError) as excinfo:
        task_func(data, cols, percentage)
    assert str(excinfo.value) == 'Percentage must be between 0 and 1'