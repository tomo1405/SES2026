import pytest
from src_0216 import task_func
import pandas as pd
import seaborn as sns
import io
import matplotlib.pyplot as plt

# Mocking the requests.get method
class MockResponse:
    def __init__(self, text):
        self.text = text

def mock_requests_get(url, params, headers):
    # Example JSON data
    json_data = '{"col1": [1, 2, 3], "col2": [4, 5, 6]}'
    return MockResponse(json_data)

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    monkeypatch.setattr('requests.get', mock_requests_get)

def test_task_func():
    url = "http://example.com"
    parameters = {"param1": "value1", "param2": "value2"}
    
    df, ax = task_func(url, parameters)
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [4, 5, 6]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the heatmap is created
    assert isinstance(ax, sns.axisgrid.heatmap)
    
    # Save the plot to a BytesIO object and check its content
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue() != b''

if __name__ == "__main__":
    pytest.main()