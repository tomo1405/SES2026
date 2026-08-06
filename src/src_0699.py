import pandas as pd
from sklearn.model_selection import train_test_split
def task_func(df):
    X = pd.DataFrame.drop(df, 'target', axis=1)
    y = pd.DataFrame(df['target'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test