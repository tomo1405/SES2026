import time
import matplotlib.pyplot as plt
def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    try:
        seconds = [time.strptime(ts, time_format).tm_sec for ts in time_strings]
        _, ax = plt.subplots()
        ax.hist(seconds, bins=60, rwidth=0.8)
        return ax
    except ValueError as e:
        print(f"Error parsing time strings: {e}")
        return None