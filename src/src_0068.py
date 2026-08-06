import pandas as pd
import re
import os
def task_func(dir_path: str, pattern: str = '^EMP'):
    file_sizes = []
    for file in sorted(os.listdir(dir_path)):
        if re.match(pattern, file):
            file_sizes.append((file, os.path.getsize(os.path.join(dir_path, file))))

    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])
    return df