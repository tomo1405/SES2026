import math
import pandas as pd
def task_func(tuples_list):
    df = pd.DataFrame([(math.sin(n) for n in t) for t in tuples_list])
    return df