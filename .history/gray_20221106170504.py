import numpy as np
from PIL import Image

# l = np.array([[0, 128, 255], [0, 128, 255], [0, 128, 255]])
row_data = np.arange(256)
im_data = np.tile(row_data)
# print(row_data)



im = Image.fromarray(np.unit8(l), "L")
im.show()
