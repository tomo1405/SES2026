import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(df):

    scaler = MinMaxScaler(feature_range=(0, 1))
    #Scaling the 'age' and 'income' columns
    df_grouped = df.groupby('id').apply(
        lambda x: pd.DataFrame(
            scaler.fit_transform(x[['age', 'income']]), 
            columns=['age', 'income'], 
            index=x.index
        )
    )

    # Creating a histogram of the 'income' column
    hist, bins = np.histogram(df_grouped['income'], bins=10)

    return df_grouped, (hist, bins)
import pytest
def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({
        'id': [1, 1, 2, 2, 3],
        'age': [25, 30, 28, 32, 27],
        'income': [50000, 60000, 55000, 70000, 65000]
    })

    # Call the function
    df_grouped, (hist, bins) = task_func(df)

    # Test the output
    assert isinstance(df_grouped, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert isinstance(bins, np.ndarray)
    assert df_grouped.shape == (3, 2)
    assert len(hist) == 10
    assert len(bins) == 11
    assert df_grouped.columns.tolist() == ['age', 'income']
    assert df_grouped.index.tolist() == [1, 2, 3]
    assert df_grouped.loc[1].tolist() == [0.0, 0.0]
    assert df_grouped.loc[2].tolist() == [0.25, 0.25]
    assert df_grouped.loc[3].tolist() == [0.5, 0.5]

if __name__ == "__main__":
    pytest.main()