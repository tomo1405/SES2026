import collections
import pandas as pd
def task_func(my_tuple, path_csv_files):

    counter = {column: collections.Counter() for column in my_tuple}

    for csv_file in path_csv_files:
        df = pd.read_csv(csv_file)

        for column in my_tuple:
            if column in df:
                counter[column].update(df[column])

    return counter