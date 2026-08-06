import pandas as pd
import os
OUTPUT_DIR = './output'
def task_func(df, filename, output_dir=OUTPUT_DIR):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, filename)
    df_clean = df.where(pd.notnull(df), None)
    with open(file_path, 'w') as f:
        df_clean.to_json(f, orient='records')
    return file_path