import numpy as np
from sklearn.decomposition import PCA
def task_func(tuples_list, n_components):
    data = np.array(tuples_list)
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data)

    return transformed_data