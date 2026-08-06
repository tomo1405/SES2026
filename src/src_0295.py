import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    try:
        scaler = StandardScaler()

        df_grouped = df.groupby('id').apply(lambda x: pd.DataFrame(scaler.fit_transform(x[['age', 'income']]), columns=['age', 'income'], index=x.index))

        return df_grouped
    except:
        raise ValueError()