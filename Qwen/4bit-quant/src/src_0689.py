import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    # Standardize data
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized