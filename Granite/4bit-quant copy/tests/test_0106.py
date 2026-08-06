import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytest

def task_func(df):
    if df.empty or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")
    
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("'date' column must be in datetime format.")

    try:
        df['date'] = df['date'].apply(lambda x: x.toordinal())
        df_numeric = df.drop(columns=['group'])
        correlation_matrix = df_numeric.corr()

        heatmap_fig = plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title('Correlation Matrix')

        pairplot_grid = sns.pairplot(df)

        return heatmap_fig, pairplot_grid

    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

def test_task_func():
    # Test case 1: Test if the function raises a ValueError when the DataFrame is empty
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame must be non-empty"):
        task_func(df_empty)

    # Test case 2: Test if the function raises a ValueError when the DataFrame does not have the required columns
    df_missing_cols = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    with pytest.raises(ValueError, match="DataFrame must contain 'group', 'date', and 'value' columns"):
        task_func(df_missing_cols)

    # Test case 3: Test if the function raises a ValueError when the 'date' column is not in datetime format
    df_invalid_date_format = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'date': ['2022-01-01', '2022-02-01', '2022-03-01'],
        'value': [100, 200, 300]
    })
    with pytest.raises(ValueError, match="'date' column must be in datetime format"):
        task_func(df_invalid_date_format)

    # Test case 4: Test if the function returns the expected output when the input DataFrame is valid
    df_valid = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'date': ['2022-01-01', '2022-02-01', '2022-03-01'],
        'value': [100, 200, 300]
    })
    heatmap_fig, pairplot_grid = task_func(df_valid)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.PairGrid)