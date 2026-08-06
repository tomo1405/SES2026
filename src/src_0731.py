import pickle
import os
# Constants
FILE_NAME = 'save.pkl'
def task_func(dt):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(dt, file)
    
    with open(FILE_NAME, 'rb') as file:
        loaded_dt = pickle.load(file)

    os.remove(FILE_NAME)

    return loaded_dt