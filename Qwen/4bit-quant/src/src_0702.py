import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(df, target):
    X = pd.DataFrame.drop(df, target, axis=1)  
    y = pd.Series(df[target])  
    
    model = LinearRegression()
    model.fit(X, y)

    return model.score(X, y)