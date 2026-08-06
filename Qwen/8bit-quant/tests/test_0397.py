import pytest
from src_0397 import task_func
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_invalid_sample_size():
    with pytest.raises(ValueError, match='sample_size must be a positive integer.'):
        task_func(mu=0, sigma=1, sample_size=-1)

def test_task_func_zero_sample_size():
    with pytest.raises(ValueError, match='sample_size must be a positive integer.'):
        task_func(mu=0, sigma=1, sample_size=0)

def test_task_func_positive_sample_size():
    ax = task_func(mu=0, sigma=1, sample_size=100)
    assert isinstance(ax, plt.Axes)

def test_task_func_seed_consistency():
    ax1 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    ax2 = task_func(mu=0, sigma=1, sample_size=100, seed=42)
    
    # Convert axes to images and compare
    img1 = BytesIO()
    ax1.figure.savefig(img1, format='png')
    img1.seek(0)
    
    img2 = BytesIO()
    ax2.figure.savefig(img2, format='png')
    img2.seek(0)
    
    assert base64.b64encode(img1.read()) == base64.b64encode(img2.read())

def test_task_func_different_means():
    ax1 = task_func(mu=0, sigma=1, sample_size=100)
    ax2 = task_func(mu=2, sigma=1, sample_size=100)
    
    # Convert axes to images and compare
    img1 = BytesIO()
    ax1.figure.savefig(img1, format='png')
    img1.seek(0)
    
    img2 = BytesIO()
    ax2.figure.savefig(img2, format='png')
    img2.seek(0)
    
    assert base64.b64encode(img1.read()) != base64.b64encode(img2.read())

def test_task_func_different_std_devs():
    ax1 = task_func(mu=0, sigma=1, sample_size=100)
    ax2 = task_func(mu=0, sigma=2, sample_size=100)
    
    # Convert axes to images and compare
    img1 = BytesIO()
    ax1.figure.savefig(img1, format='png')
    img1.seek(0)
    
    img2 = BytesIO()
    ax2.figure.savefig(img2, format='png')
    img2.seek(0)
    
    assert base64.b64encode(img1.read()) != base64.b64encode(img2.read())