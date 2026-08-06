import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
def task_func(
    feature_array,
    target_array,
    feature_names=["f1", "f2", "f3", "f4", "f5"],
    target_name="target",
    seed=None,
):
    if seed is not None:
        np.random.seed(seed)

    shuffled_array = feature_array.copy()
    np.random.shuffle(shuffled_array.T)

    df = pd.DataFrame(shuffled_array, columns=feature_names)
    df[target_name] = target_array

    clf = RandomForestClassifier()
    clf.fit(df[feature_names], df[target_name])

    return clf