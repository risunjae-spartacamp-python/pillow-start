import numpy as np
from PIL import Image

# l = np.array([[0, 128, 255], [0, 128, 255], [0, 128, 255]])
l = np.

im = Image.fromarray(np.unit8(l), "L")
im.show()
