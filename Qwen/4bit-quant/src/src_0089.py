import numpy as np
import pandas as pd
from datetime import datetime, timedelta
def task_func(start_date, end_date, seed=42):
    np.random.seed(seed)
    data = []
    date = start_date

    while date <= end_date:
        sales = np.random.randint(0, 500)
        data.append([date, sales])
        date += timedelta(days=1)

    df = pd.DataFrame(data, columns=["Date", "Sales"])
    ax = df.plot(x='Date', y='Sales')
    ax.set_ylabel("Sales")

    return df, ax