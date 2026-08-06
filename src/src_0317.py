import pandas as pd
import random
# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
def task_func(value_range=(0, 100)):

    distribution = {category: random.randint(*value_range) for category in CATEGORIES}
    df = pd.DataFrame(list(distribution.items()), columns=['Category', 'Count'])

    return df