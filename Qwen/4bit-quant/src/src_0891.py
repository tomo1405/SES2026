import os
import random
import pandas as pd
def task_func(data_dir,
          csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
          seed=None):

    random.seed(seed)

    file = csv_files[random.randint(0, len(csv_files) - 1)]
    file_path = os.path.join(data_dir, file)

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return file, pd.DataFrame()

    selected_rows = df.sample(n=random.randint(1, len(df)), random_state=seed)

    return file, selected_rows