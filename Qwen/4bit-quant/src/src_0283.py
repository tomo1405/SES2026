import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import cv2
import os
def task_func(file_path, onpick):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No file found at {file_path}")

    img = cv2.imread(file_path)
    color = ('b', 'g', 'r')
    fig = plt.figure()
    ax = Axes3D(fig)

    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        ax.plot(np.arange(256), hist, color=col)

    fig.canvas.mpl_connect('pick_event', onpick)

    # plt.show()

    return ax