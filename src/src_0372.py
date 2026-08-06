from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(l):

    scaler = MinMaxScaler()
    l_scaled = scaler.fit_transform(l.reshape(-1, 1))
    df = pd.DataFrame(l_scaled, columns=['Scaled Values'])
    return df