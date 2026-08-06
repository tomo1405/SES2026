import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(data):
    le = LabelEncoder()
    encoded = le.fit_transform(data)
    df = pd.DataFrame({'Category': data, 'Encoded': encoded})

    return df