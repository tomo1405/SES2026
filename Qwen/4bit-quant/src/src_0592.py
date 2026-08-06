from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'
def task_func(hours, file_path=FILE_PATH):

    data = {'Time': [], 'Temperature': [], 'Category': []}
    for i in range(hours):
        temp = randint(-10, 40)  # random temperature between -10 and 40
        data['Time'].append(datetime.now().strftime('%H:%M:%S.%f'))
        data['Temperature'].append(temp)
        if temp < 0:
            data['Category'].append(TEMP_CATEGORIES[0])
        elif temp > 25:
            data['Category'].append(TEMP_CATEGORIES[2])
        else:
            data['Category'].append(TEMP_CATEGORIES[1])

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    
    ax = df.plot(x = 'Time', y = 'Temperature', kind = 'line', title="Temperature Data Over Time")
    plt.show()

    return file_path, ax