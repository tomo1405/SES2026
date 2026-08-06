import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pytest

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    df = pd.read_csv(file_path)
    
    if target_column not in df.columns:
        raise ValueError(f"The specified target column '{target_column}' does not exist in the CSV file.")
    
    # Drop rows with any NaN values
    df_cleaned = df.dropna()

    X = df_cleaned.drop(target_column, axis=1)
    y = df_cleaned[target_column]
    
    # Option to scale features if needed
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)
    
    clf = RandomForestClassifier(random_state=seed)
    clf.fit(X, y)
    importances = clf.feature_importances_
    
    fig, ax = plt.subplots()
    sns.barplot(x=X.columns, y=importances, ax=ax)
    ax.set_title('Feature Importances')
    
    return ax, importances

def test_task_func():
    # Test if the function raises a FileNotFoundError when the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(file_path='nonexistent_file.csv')

    # Test if the function raises a ValueError when the target column does not exist
    with pytest.raises(ValueError):
        task_func(target_column='Nonexistent Column')

    # Test if the function returns the correct ax and importances objects
    ax, importances = task_func()
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, list)