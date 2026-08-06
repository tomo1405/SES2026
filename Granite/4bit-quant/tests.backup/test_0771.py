import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(num_samples=500, noise_strength=1, random_seed=None, test_size=0.2):

    if num_samples * test_size < 2:
        raise ValueError("Test set should contain at least 2 samples. num_samples * testsize >=2")

    if random_seed is not None:
        np.random.seed(random_seed)

    X = np.random.rand(num_samples, 1)
    y = 2*X.squeeze() + 1 + np.random.randn(num_samples) * noise_strength

    X_train, X_test, y_train, y_test = train_test_split(
                                            X, y,
                                            test_size=test_size,
                                            random_state=random_seed
                                            )

    model = LinearRegression()
    model.fit(X_train, y_train)

    r_squared = model.score(X_test, y_test)

    return r_squared, model
import pytest
def test_task_func():
    num_samples = 500
    noise_strength = 1
    random_seed = None
    test_size = 0.2
    with pytest.raises(ValueError):
        task_func(num_samples=num_samples, noise_strength=noise_strength, random_seed=random_seed, test_size=test_size)
    num_samples = 500
    noise_strength = 1
    random_seed = None
    test_size = 0.5
    r_squared, model = task_func(num_samples=num_samples, noise_strength=noise_strength, random_seed=random_seed, test_size=test_size)
    assert r_squared > 0.5
    num_samples = 100
    noise_strength = 1
    random_seed = 42
    test_size = 0.2
    r_squared, model = task_func(num_samples=num_samples, noise_strength=noise_strength, random_seed=random_seed, test_size=test_size)
    assert r_squared > 0.5