import pandas as pd
from random import shuffle
# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def task_func(list_of_lists):
    dataframes = []

    for list_ in list_of_lists:
        df_dict = {col: POSSIBLE_VALUES.copy() for col in list_}
        for col in df_dict:
            shuffle(df_dict[col])
        df = pd.DataFrame(df_dict)
        dataframes.append(df)

    return dataframes