from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    img = Image.open(path)
    image_np = np.array(img)
    image_np = 255 - image_np
    return image_np


def edge_detection(image):
   
    if len(image.shape) == 3:
        gray = np.mean(image, axis=2)
    else:
        gray = image
    Gx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])
    Gy = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ])
    edgeX = convolve2d(gray, Gx, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(gray, Gy, mode='same', boundary='fill', fillvalue=0)
    edgeMAG = ((edgeX**2 + edgeY**2) ** 0.5)
    return edgeMAG
    
