import pandas as pd
from sklearn.decomposition import PCA
def task_func(df):
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)
    
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    
    return df_pca