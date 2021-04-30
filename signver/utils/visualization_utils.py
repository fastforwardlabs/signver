import matplotlib
import matplotlib.pyplot as plt

import io
import scipy.misc
import numpy as np
from six import BytesIO
from PIL import Image, ImageDraw, ImageFont


from signver.utils import data_utils

viz_colors = {
    "green": np.array([0, 255, 0], dtype=np.uint8),
    "cyan": np.array([0, 255, 0], dtype=np.uint8)
}


def plot_np_array(np_img_array, plot_title: str="Image Plot", fig_size=(15, 20)):
    plt.figure(figsize=fig_size)
    plt.imshow(np_img_array, interpolation='nearest')
    plt.title(plot_title)
    plt.show()


def draw_rectangle_on_image(image_np_array, color, bounding_boxes):
    np_array = image_np_array.copy()
    for bbox in bounding_boxes:
        np_array[bbox[1], bbox[0]:bbox[0] + bbox[2]] = color
        np_array[bbox[1]:bbox[1] +
                 bbox[3], bbox[0]] = color

        np_array[bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]] = color
        np_array[bbox[1]:bbox[1] + bbox[3],
                 bbox[0] + bbox[2]] = color
    return np_array


def visualize_boxes(image_np_array, boxes, scores, threshold=0.5, color=viz_colors["green"]):
    bboxes = []
    for i in range(len(scores)):
        if scores[i] > 0.2:
            height, width, _ = image_np_array.shape
            ymin, xmin, ymax, xmax = boxes[i]
            bbox = (int(xmin*width), int(ymin*height),
                    int((xmax-xmin) * width), int((ymax-ymin)*height))
            bboxes.append(bbox)
    return draw_rectangle_on_image(image_np_array, color, bboxes)
