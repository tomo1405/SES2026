import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import pytest

def task_func(data_matrix, n_components=2):
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_matrix)

    df = pd.DataFrame(
        transformed_data,
        columns=[f"Component {i+1}" for i in range(transformed_data.shape[1])],
    )
    df["Mean"] = df.mean(axis=1)

    fig, ax = plt.subplots()
    ax.plot(np.cumsum(pca.explained_variance_ratio_))
    ax.set_xlabel("Number of Components")
    ax.set_ylabel("Cumulative Explained Variance")
    return df, ax

def test_task_func():
    data_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n_components = 2
    df, ax = task_func(data_matrix, n_components)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, n_components + 1)
    assert df["Mean"].tolist() == [1.5, 4.5, 7.5]
    assert ax.get_xlabel() == "Number of Components"
    assert ax.get_ylabel() == "Cumulative Explained Variance"

if __name__ == "__main__":
    pytest.main()