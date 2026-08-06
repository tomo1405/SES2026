import pandas as pd
import itertools
from random import shuffle
def task_func(letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], categories=['Category 1', 'Category 2', 'Category 3']):
    
    flattened_list = list(itertools.chain(*[letters for _ in range(len(categories))]))
    expanded_categories = list(itertools.chain(*[[category] * len(letters) for category in categories]))
    shuffle(expanded_categories)

    df = pd.DataFrame({'Letter': flattened_list, 'Category': expanded_categories})

    return df