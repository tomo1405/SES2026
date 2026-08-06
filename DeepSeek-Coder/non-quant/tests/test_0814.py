import pytest
from itertools import combinations
import pandas as pd

def task_func(number_list, element):
    combinations_list = list(combinations(number_list, 3))
    valid_combinations = [comb for comb in combinations_list if sum(comb) == element]
    
    # Return only unique combinations
    return pd.DataFrame({'Combinations': list(set(valid_combinations))})

# Test cases
def test_task_func():
    # Test case 1
    result = task_func([1, 2, 3, 4], 7)
    assert result.iloc[0]['Combinations'] == (1, 2, 4)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()