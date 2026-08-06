import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def task_func(num_samples, countries=['Russia', 'China', 'USA', 'India', 'Brazil'], 
           ages=np.arange(18, 60), genders=['Male', 'Female'], rng_seed=None):

    if not isinstance(num_samples, int):
        raise ValueError("num_samples should be an integer.")

    rng = np.random.default_rng(seed=rng_seed)
    countries = rng.choice(countries, num_samples)
    ages = rng.choice(ages, num_samples)
    genders = rng.choice(genders, num_samples)

    le = LabelEncoder()
    encoded_genders = le.fit_transform(genders)

    demographics = pd.DataFrame({
        'Country': countries,
        'Age': ages,
        'Gender': encoded_genders
    })

    return demographics