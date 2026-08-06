import pandas as pd
from sklearn.model_selection import train_test_split
def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    df = pd.DataFrame(df)
    # Drop the specified column if it exists in the dataframe
    if column_to_remove in df.columns:
        df = df.drop(columns=column_to_remove)

    # Split the dataframe into training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(columns=target_column), df[target_column], test_size=test_size
    )

    return X_train, X_test, y_train, y_test