python
import pandas as pd
import numpy as np
import pytest

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):

    # Determine categories where both stores exceed the sales threshold
    high_sales_categories = s1.index[(s1 > 200) & (s2 > 200)]

    if high_sales_categories.empty:
        return None, 0.0

    # Prepare the data for plotting
    df = pd.DataFrame(
        {"Store 1": s1[high_sales_categories], "Store 2": s2[high_sales_categories]}
    )

    # compute the edit distance between the two series
    edit_distance = np.linalg.norm(df["Store 1"] - df["Store 2"])
    
    # Generate the bar plot
    ax = df.plot(kind="bar", title="Sales Comparison Above Threshold in Categories")
    return ax, edit_distance

def test_task_func():
    s1 = pd.Series([100, 200, 300, 400, 500], index=CATEGORIES)
    s2 = pd.Series([150, 250, 350, 450, 550], index=CATEGORIES)
    ax, edit_distance = task_func(s1, s2)
    assert ax is not None
    assert edit_distance == 50.0

test_task_func()