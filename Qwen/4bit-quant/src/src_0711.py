import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(data_path):
    df = pd.read_csv(data_path)
    data = df.to_numpy()
    
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    df = pd.DataFrame(data, columns=df.columns)

    return df