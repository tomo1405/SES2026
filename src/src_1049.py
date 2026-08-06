from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
def task_func(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    x = np.linspace(0, 2 * np.pi, 1000)
    frequency = date.day
    y = np.sin(frequency * x)
    _, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Sine Wave for {date_str} (Frequency: {frequency})")
    return ax