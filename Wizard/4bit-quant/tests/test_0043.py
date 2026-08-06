python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

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
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data_matrix)
    assert df.shape == (3, 3)
    assert df.columns.tolist() == ["Component 1", "Component 2", "Mean"]
    assert df.loc[0, "Component 1"] == 0.7071067811865476
    assert df.loc[1, "Component 2"] == 0.7071067811865476
    assert df.loc[2, "Mean"] == 5.0
    assert ax.get_xlabel() == "Number of Components"
    assert ax.get_ylabel() == "Cumulative Explained Variance"