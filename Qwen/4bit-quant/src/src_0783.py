import random
import pandas as pd
import numpy as np
def task_func(n,
          domain="samplewebsite.com",
          categories=['Sports', 'Technology', 'Health', 'Science', 'Business'],
          random_seed=None):
    random.seed(random_seed)
    np.random.seed(random_seed)

    data = []
    for _ in range(n):
        title = f"Article {_}"
        title_url = f"{domain}/Article_{_}"
        id = _
        category = random.choice(categories)
        views = np.random.poisson(1000)
        data.append({'title': title, 'title_url': title_url, 'id': id, 'category': category, 'views': views})

    df = pd.DataFrame(data)
    return df