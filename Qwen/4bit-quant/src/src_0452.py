import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(n_components=2, N_SAMPLES=500, N_FEATURES=50, random_seed=None):
    np.random.seed(random_seed)  # Ensuring reproducibility
    X = np.random.rand(N_SAMPLES, N_FEATURES)

    pca = PCA(n_components=n_components, random_state=random_seed)
    X_transformed = pca.fit_transform(X)

    if n_components == 1:
        return X_transformed, None

    fig, ax = plt.subplots(figsize=(10, 7))
    sns.heatmap(np.cov(X_transformed.T), annot=True, fmt=".2f", ax=ax)

    return X_transformed, ax