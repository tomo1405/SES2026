import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import pytest

def task_func(directory: str, pattern: str) -> list:
    plots = []
    for file in os.listdir(directory):
        if re.match(pattern, file):
            df = pd.read_csv(os.path.join(directory, file))
            ax = df.plot(x='Month', y='Sales', title=file)
            plots.append(ax)
    plt.show()
    return plots