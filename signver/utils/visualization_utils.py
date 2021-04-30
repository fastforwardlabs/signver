import matplotlib
import matplotlib.pyplot as plt

import io
import scipy.misc
import numpy as np
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont


from signver.utils import data_utils


def plot_np_array(np_img_array, plot_title: str="Image Plot", fig_size=(15, 20)):
    plt.figure(figsize=fig_size)
    plt.imshow(np_img_array, interpolation='nearest')
    plt.title(plot_title)
    plt.show()


def draw_rectangle(np_array, color, bounding_boxes):
    np_array = np_array.copy()
    for bbox in bounding_boxes:
        np_array[bbox[1], bbox[0]:bbox[0] + bbox[2]] = color
        np_array[bbox[1]:bbox[1] +
                 bbox[3], bbox[0]] = color

        np_array[bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]] = color
        np_array[bbox[1]:bbox[1] + bbox[3],
                 bbox[0] + bbox[2]] = color
    return np_array
