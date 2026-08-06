import re
import pandas as pd
def task_func(df: pd.DataFrame) -> int:

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df should be a DataFrame.")

    # Constants
    BRACKETS_PATTERN = '[(){}[\]]'

    return df.applymap(
        lambda x: len(re.findall(BRACKETS_PATTERN, str(x)))
        ).sum().sum()