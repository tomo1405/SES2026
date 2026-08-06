import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    df = pd.DataFrame(array)

    pca = PCA(n_components=2, random_state=random_seed)
    transformed_data = pca.fit_transform(df)

    return df, transformed_data