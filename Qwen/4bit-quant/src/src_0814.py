from itertools import combinations
import pandas as pd
def task_func(number_list, element):
    combinations_list = list(combinations(number_list, 3))
    valid_combinations = [comb for comb in combinations_list if sum(comb) == element]
    
    # Return only unique combinations
    return pd.DataFrame({'Combinations': list(set(valid_combinations))})