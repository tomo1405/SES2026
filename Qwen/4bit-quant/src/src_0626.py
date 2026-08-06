import math
from random import randint
import pandas as pd
def task_func(cities_list):
    population_data = []

    for city in cities_list:
        population = math.ceil(randint(1000000, 20000000) / 1000.0) * 1000
        population_data.append([city, population])

    population_df = pd.DataFrame(population_data, columns=['City', 'Population'])

    return population_df