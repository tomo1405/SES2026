import random
from collections import Counter
def task_func(values, weights, n_samples):
    import random
    samples = random.choices(values, weights=weights, k=n_samples)
    histogram = dict(Counter(samples))

    return histogram