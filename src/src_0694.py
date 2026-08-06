import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(tuples_list, columns):
    df = pd.DataFrame(tuples_list, columns=columns)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    return df_scaled