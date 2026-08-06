import pandas as pd
from src_0299 import task_func


def test_task_func():
    # Test with plot=False
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Value': [10, 20, 30]})
    df_expected = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                               'Value': [10, 20, 30]})
    df_expected['Date'] = pd.to_datetime(df_expected['Date'])
    df_expected = pd.concat([df_expected['Date'], df_expected['Value'].apply(pd.Series)], axis=1)
    scaler = StandardScaler()
    df_expected.iloc[:,1:] = scaler.fit_transform(df_expected.iloc[:,1:])
    df_result, ax = task_func(df, plot=False)
    assert df_result.equals(df_expected)

    # Test with plot=True
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Value': [10, 20, 30]})
    df_expected = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                               'Value': [10, 20, 30]})
    df_expected['Date'] = pd.to_datetime(df_expected['Date'])
    df_expected = pd.concat([df_expected['Date'], df_expected['Value'].apply(pd.Series)], axis=1)
    scaler = StandardScaler()
    df_expected.iloc[:,1:] = scaler.fit_transform(df_expected.iloc[:,1:])
    df_result, ax = task_func(df, plot=True)
    assert df_result.equals(df_expected)
    assert ax.title.get_text() == 'Scaled Values Over Time'
    assert ax.xlabel.get_text() == 'Date'
    assert ax.ylabel.get_text() == 'Scaled Value'