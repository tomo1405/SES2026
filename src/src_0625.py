from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
# Constants
N_COMPONENTS = 2
def task_func(L):
    data = np.array(L)

    pca = PCA(n_components=N_COMPONENTS)
    pca_result = pca.fit_transform(data)

    fig, ax = plt.subplots()
    ax.scatter(pca_result[:,0], pca_result[:,1])

    return pca_result, ax