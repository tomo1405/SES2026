import os
import pandas as pd
from dateutil.parser import parse
OUTPUT_DIR = './output'
def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):

    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")

    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))

    return df[date_column].dt.year.hist()