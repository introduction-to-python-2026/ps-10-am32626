
 
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import median
from skimage.morphology import ball
from image_utils import load_image, edge_detection
image = load_image(img.jpg)
clean_image = median(image, ball(3))
edge_image = edge_detection(clean_image)


