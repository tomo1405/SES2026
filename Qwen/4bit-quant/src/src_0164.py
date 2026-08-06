import numpy as np
import pandas as pd
def task_func(rows=5, cols=5):
    np.random.seed(0)
    categories = ['A', 'B', 'C', 'D', 'E']
    if cols > len(categories):
        raise ValueError(f"Maximum number of columns allowed is {len(categories)}")

    data = pd.DataFrame(np.random.rand(rows, cols) * 100, columns=categories[:cols])

    ax = data.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_ylabel('Value')
    ax.set_title('Stacked Bar Chart')

    return ax