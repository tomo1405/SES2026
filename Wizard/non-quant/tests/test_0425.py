python
import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
import pytest

def task_func(image_path='image.jpg', n_clusters=3, random_seed=42):

    if not isinstance(n_clusters, int) or n_clusters <= 0:
        raise ValueError("n_clusters must be a positive integer.")

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")

    # Image processing
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Failed to read the image file.")
    if n_clusters == 1:
        # Return the original image without modification if n_clusters is 1
        return img, img.copy()
    
    pixels = img.reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_seed)
    kmeans.fit(pixels)
    segmented_image = kmeans.cluster_centers_[kmeans.labels_]
    segmented_image = segmented_image.reshape(img.shape).astype('uint8')

    # Save each cluster as a separate image, if more than one cluster
    if n_clusters > 1:
        for i in range(n_clusters):
            mask = kmeans.labels_.reshape(img.shape[:2]) == i
            cluster_img = np.where(np.stack([mask]*3, axis=-1), segmented_image, np.array([255, 255, 255], dtype=np.uint8))
            cv2.imwrite(f'cluster_{i+1}.jpg', cluster_img)

    return np.array(img), np.array(segmented_image)

def test_task_func():
    # Test case 1: n_clusters = 1
    img, segmented_image = task_func(n_clusters=1)
    assert np.array_equal(img, segmented_image)

    # Test case 2: n_clusters = 2
    img, segmented_image = task_func(n_clusters=2)
    assert segmented_image.shape == (256, 256, 3)
    assert len(os.listdir()) == 2

    # Test case 3: n_clusters = 3
    img, segmented_image = task_func(n_clusters=3)
    assert segmented_image.shape == (256, 256, 3)
    assert len(os.listdir()) == 3

    # Test case 4: n_clusters = 4 (invalid)
    with pytest.raises(ValueError):
        task_func(n_clusters=4)

    # Test case 5: image_path does not exist (invalid)
    with pytest.raises(FileNotFoundError):
        task_func(image_path='invalid_image.jpg')

    # Test case 6: image_path is None (invalid)
    with pytest.raises(ValueError):
        task_func(image_path=None)