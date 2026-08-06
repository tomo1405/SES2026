import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
def task_func(df, x_column, y_column):
    X = df[x_column].values.reshape(-1, 1)
    Y = df[y_column].values
    reg = LinearRegression().fit(X, Y)
    Y_pred = reg.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, Y_pred, color="red")

    return ax