python
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
    # Test case 1: Valid input
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [1, 2, 3]})
    heatmap_fig, pairplot_grid = task_func(df)
    assert isinstance(heatmap_fig, plt.Figure)
    assert isinstance(pairplot_grid, sns.axisgrid.PairGrid)

    # Test case 2: Empty DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."

    # Test case 3: DataFrame with missing columns
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03']})
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."

    # Test case 4: DataFrame with non-datetime column
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [1, 2, 3], 'non-datetime': ['a', 'b', 'c']})
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "'date' column must be in datetime format."

    # Test case 5: Error in correlation matrix calculation
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [1, 2, '3']})
    with pytest.raises(ValueError) as e:
        task_func(df)
    assert str(e.value) == "An error occurred: could not convert string to float: '3'"