import numpy as np
import pandas as pd
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'
def task_func(file_path, output_dir=OUTPUT_DIR):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    matrix = pd.DataFrame(np.random.choice(LETTERS, (10, 10)))
    matrix.to_csv(file_path, sep='\t', header=False, index=False)

    return None