import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    try:
        scaler = StandardScaler()

        df_grouped = df.groupby('id').apply(lambda x: pd.DataFrame(scaler.fit_transform(x[['age', 'income']]), columns=['age', 'income'], index=x.index))

        return df_grouped
    except:
        raise ValueError()
import pytest

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'id': [1, 1, 2, 2],
        'age': [25, 30, 28, 32],
        'income': [50000, 60000, 55000, 65000]
    })

    # Call the function with the sample DataFrame
    result = task_func(df)

    # Define the expected result
    expected_result = pd.DataFrame({
        'id': [1, 1, 2, 2],
        'age': [-1.3416407864998738, -0.22367000853308654, -1.0304033397641458, 0.22367000853308654],
        'income': [-1.3416407864998738, -0.22367000853308654, -1.0304033397641458, 0.22367000853308654]
    })

    # Assert that the result matches the expected result
    assert result.equals(expected_result)

if __name__ == '__main__':
    pytest.main()