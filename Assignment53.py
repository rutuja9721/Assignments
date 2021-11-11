#Read one image and convert it in to numpy array

from PIL import Image
import numpy as np

im = np.array(Image.open('D:/PythonWork/PythonWork/download.jpg'))

print(im)