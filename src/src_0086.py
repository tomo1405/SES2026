import numpy as np
import pandas as pd
from datetime import timedelta
def task_func(start_date, end_date, random_seed=42):
    if end_date < start_date:
        raise ValueError("End date must be after start date")

    np.random.seed(random_seed)

    COLUMNS = ["Date", "Temperature", "Humidity", "Wind Speed"]
    data = []
    date = start_date

    while date <= end_date:
        temp = np.random.uniform(-10, 40)
        humidity = np.random.uniform(20, 100)
        wind_speed = np.random.uniform(0, 20)
        data.append([date, temp, humidity, wind_speed])
        date += timedelta(days=1)

    df = pd.DataFrame(data, columns=COLUMNS)
    ax = df.plot(x='Date', y=['Temperature', 'Humidity', 'Wind Speed'], title="Generated Weather Data")

    return df, ax