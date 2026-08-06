import pandas as pd
import os
def task_func(data_dir: str, csv_files: list) -> pd.DataFrame:
    merged_df = pd.DataFrame()

    for file in csv_files:
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    return merged_df