from unittest.mock import patch

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression


def task_func(df):
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns.")

    df['date'] = df['date'].apply(lambda x: x.toordinal())
    X = df[['date']]
    y = df['value']

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(X, y, color='red')
    ax.plot(X, y_pred, color='blue')
    ax.set_title('Value vs Date (Linear Regression Prediction)')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')

    return model, y_pred, ax

def test_task_func():
    # Test invalid input
    with patch('matplotlib.pyplot.show') as mock_show:
        with pytest.raises(ValueError) as exc_info:
            task_func('not a DataFrame')
        assert "Invalid 'df': must be a DataFrame with 'group', 'date', and 'value' columns." in str(exc_info.value)
        mock_show.assert_not_called()

    # Test valid input
    df = pd.DataFrame({
        'group': ['A', 'B', 'C'],
        'date': [pd.Timestamp('2022-01-01'), pd.Timestamp('2022-01-02'), pd.Timestamp('2022-01-03')],
        'value': [10, 20, 30]
    })
    model, y_pred, ax = task_func(df)
    assert isinstance(model, LinearRegression)
    assert isinstance(y_pred, pd.Series)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Value vs Date (Linear Regression Prediction)'
    assert ax.get_xlabel() == 'Date (ordinal)'
    assert ax.get_ylabel() == 'Value'