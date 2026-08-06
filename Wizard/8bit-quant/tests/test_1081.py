python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def task_func(area_string, data=DATA):
    # Convert area strings to float and prepare data for the model
    df = pd.DataFrame(data)
    df["Area_Float"] = df["Area_String"].str.replace(",", "").astype(float)

    # Train the linear regression model
    X = df[["Area_Float"]]
    Y = df["Price"]
    model = LinearRegression()
    model.fit(X, Y)

    # Predict the price for the given area string
    area_float = float(area_string.replace(",", ""))
    prediction_data = pd.DataFrame([area_float], columns=["Area_Float"])
    price_predicted = model.predict(prediction_data)

    return price_predicted[0]

def test_task_func():
    assert task_func("1,000") == 100
    assert task_func("2,000") == 200
    assert task_func("3,000") == 300
    assert task_func("4,000") == 400
    assert task_func("5,000") == 500
    assert task_func("6,000") == pytest.approx(500.0000000000001)