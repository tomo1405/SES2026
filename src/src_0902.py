import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# Updated function to handle empty input list
def task_func(d):
    if not d:  # Check if the input list is empty
        return pd.DataFrame(columns=['x', 'y', 'z'])  # Return an empty DataFrame with specified columns
    
    df = pd.DataFrame(d)
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df[['x', 'y', 'z']]), columns=['x', 'y', 'z'])

    return scaled_df