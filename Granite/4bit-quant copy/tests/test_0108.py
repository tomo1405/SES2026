import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from unittest.mock import patch

def task_func(df, n_clusters=3, random_state=0):
    if df.empty or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")

    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("'date' column must be in datetime format.")

    df['date'] = df['date'].apply(lambda x: x.toordinal())
    X = df[['date', 'value']]

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(X['date'], X['value'], c=y_kmeans, cmap='viridis')
    ax.set_title('KMeans Clustering of Value vs Date')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')

    return ax

def test_task_func():
    df = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'value': [10, 20, 30]
    })
    with patch('matplotlib.pyplot.show') as mock_show:
        ax = task_func(df)
        mock_show.assert_called_once()
    assert ax.get_title() == 'KMeans Clustering of Value vs Date'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'

def test_task_func_empty_df():
    df = pd.DataFrame()
    with patch('src_0108.task_func') as mock_task_func:
        with pytest.raises(ValueError) as exc_info:
            task_func(df)
        assert str(exc_info.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."
        mock_task_func.assert_not_called()

def test_task_func_missing_columns():
    df = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'value': [10, 20, 30]
    })
    with patch('src_0108.task_func') as mock_task_func:
        with pytest.raises(ValueError) as exc_info:
            task_func(df.drop(columns=['group']))
        assert str(exc_info.value) == "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns."
        mock_task_func.assert_not_called()

def test_task_func_invalid_date_format():
    df = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'value': [10, 20, 30]
    })
    with patch('src_0108.task_func') as mock_task_func:
        with pytest.raises(ValueError) as exc_info:
            task_func(df.assign(date=['2022-01-01', '2022-01-02', '2022-01-03']))
        assert str(exc_info.value) == "'date' column must be in datetime format."
        mock_task_func.assert_not_called()