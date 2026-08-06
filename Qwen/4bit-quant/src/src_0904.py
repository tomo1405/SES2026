import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(d, target='z'):
    df = pd.DataFrame(d)
    predictors = [k for k in df.columns if k != target]

    X = df[predictors]
    y = df[target]

    model = LinearRegression().fit(X, y)

    return model