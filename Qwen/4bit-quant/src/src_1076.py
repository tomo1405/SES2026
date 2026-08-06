import datetime
import numpy as np
import matplotlib.pyplot as plt
# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings):
    # Calculate time differences
    differences = (
        np.diff([datetime.datetime.strptime(t, TIME_FORMAT) for t in time_strings])
        .astype("timedelta64[s]")
        .astype(int)
    )

    # Plotting the bar chart
    _ = plt.bar(range(len(differences)), differences)
    plt.xlabel("Index")
    plt.ylabel("Time Difference (seconds)")
    plt.title("Time Differences Between Consecutive Timestamps")
    return plt.gca()