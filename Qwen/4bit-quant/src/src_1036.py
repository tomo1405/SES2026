import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    # Create DataFrame from the series
    df = pd.DataFrame({"Feature": feature, "Target": target})

    # Split the data into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(
        df["Feature"], df["Target"], test_size=0.2, random_state=42
    )

    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train.values.reshape(-1, 1), y_train)

    # Make predictions
    y_pred = model.predict(X_test.values.reshape(-1, 1))

    # Compute the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot the confusion matrix
    _, ax = plt.subplots()
    cax = ax.matshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar(cax)

    # Setting tick locations
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    # Now set tick labels correctly
    ax.set_xticklabels(["No", "Yes"])
    ax.set_yticklabels(["No", "Yes"])

    return cm, ax