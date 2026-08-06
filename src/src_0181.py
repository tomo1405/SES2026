from PIL import Image
import numpy as np
from skimage.transform import resize
import matplotlib.pyplot as plt
import os
def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    im = Image.open(img_path)
    img_arr = np.array(im)
    results = []

    for scale_factor in scale_factors:
        scaled_img_arr = resize(img_arr, (int(im.height * scale_factor), int(im.width * scale_factor)),
                                mode='reflect', anti_aliasing=True)
        fig, ax = plt.subplots()
        ax.imshow(scaled_img_arr)
        ax.set_title(f'Scale factor: {scale_factor}')
        results.append((ax, scaled_img_arr))
    # plt.show()
    return results