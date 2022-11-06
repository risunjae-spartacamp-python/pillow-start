from PIL import Image
import numpy as np

row_data = np.arange(256)

hue_data = np.tile(row_data, (256, 1))

sat_data = np.transpose(hue_data)

