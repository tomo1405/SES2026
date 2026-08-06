import numpy as np
import pandas as pd
from dateutil.parser import parse
def task_func(dates_str_list):
    DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays = [parse(date_str).weekday() for date_str in dates_str_list]
    weekday_counts = np.bincount(weekdays, minlength=7)
    
    distribution = pd.Series(weekday_counts, index=DAYS_OF_WEEK)

    return distribution