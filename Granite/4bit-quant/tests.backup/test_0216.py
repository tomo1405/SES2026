import pytest
import requests
import json
import pandas as pd
import seaborn as sns

HEADERS = {
    'accept': 'application/json'
}

def task_func(url, parameters):
    try:
        response = requests.get(url, params=parameters, headers=HEADERS)
        data = json.loads(response.text)

        df = pd.DataFrame(data)
        corr = df.corr()

        ax = sns.heatmap(corr, annot=True, cmap='coolwarm')
        return df, ax
    except Exception as e:
        raise(e)

def test_task_func():
    url = "https://jsonplaceholder.typicode.com/comments"
    parameters = {"postId": 1}
    df, ax = task_func(url, parameters)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.matrix.Heatmap)

def test_task_func_exception():
    url = "https://jsonplaceholder.typicode.com/comments"
    parameters = {"postId": 1}
    with pytest.raises(Exception):
        task_func(url, parameters)