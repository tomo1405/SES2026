import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src_1080 import task_func

def test_task_func():
    data = [
        {"Product": "A", "Price_String": "10,000"},
        {"Product": "B", "Price_String": "20,000"},
        {"Product": "C", "Price_String": "30,000"},
        {"Product": "D", "Price_String": "40,000"},
        {"Product": "E", "Price_String": "50,000"}
    ]
    expected_mean = 30000.0
    expected_median = 30000.0
    expected_std_dev = 10000.0
    expected_ax_settings = {
        "bins": "auto",
        "color": "blue",
        "alpha": 0.7,
        "rwidth": 0.85
    }
    expected_ax_labels = {
        "x": "Price",
        "y": "Frequency"
    }
    df = pd.DataFrame(data)
    df["Price_Float"] = df["Price_String"].apply(lambda x: float(x.replace(",", "")))
    mean_price = np.mean(df["Price_Float"])
    median_price = np.median(df["Price_Float"])
    std_dev_price = np.std(df["Price_Float"], ddof=1)
    ax = plt.hist(df["Price_Float"], bins="auto", color="blue", alpha=0.7, rwidth=0.85)
    plt.title("Histogram of Product Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    assert mean_price == expected_mean
    assert median_price == expected_median
    assert std_dev_price == expected_std_dev
    assert ax[1][0] == expected_ax_settings
    assert ax[1][1] == expected_ax_labels