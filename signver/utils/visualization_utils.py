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


def visualize_boxes(image_np_array, bounding_boxes, scores, threshold=0.5, color="green", thickness=1):

    # Code snippets inspired by https://github.com/tensorflow/models/blob/cda3bca5d53b6a09d8c0a3e2952feba297cbc096/research/object_detection/utils/visualization_utils.py#L166

    image = Image.fromarray(np.uint8(image_np_array)).convert('RGB')
    draw = ImageDraw.Draw(image)
    im_width, im_height = image.size

    for i in range(len(bounding_boxes)):
        if scores[i] > threshold:
            bbox = bounding_boxes[0]
            ymin, xmin, ymax, xmax = bbox[0], bbox[1], bbox[2], bbox[3]
            (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
                                          ymin * im_height, ymax * im_height)
            draw.line([(left, top), (left, bottom), (right, bottom), (right, top),
                       (left, top)],
                      width=thickness,
                      fill=color)

            try:
                font = ImageFont.truetype('arial.ttf', 24)
            except IOError:
                font = ImageFont.load_default()

            display_str_list = [" signature " +
                                str(i) + " | " + str(round(scores[i], 2)) + " "]
            # If the total height of the display strings added to the top of the bounding
            # box exceeds the top of the image, stack the strings below the bounding box
            # instead of above.
            display_str_heights = [font.getsize(
                ds)[1] for ds in display_str_list]
            # Each display_str has a top and bottom margin of 0.05x.
            total_display_str_height = (
                1 + 2 * 0.05) * sum(display_str_heights)

            if top > total_display_str_height:
                text_bottom = top
            else:
                text_bottom = bottom + total_display_str_height
            # Reverse list and print from bottom to top.
            for display_str in display_str_list[::-1]:
                text_width, text_height = font.getsize(display_str)
                margin = np.ceil(0.05 * text_height)
                draw.rectangle(
                    [(left, text_bottom - text_height - 2 * margin), (left + text_width,
                                                                      text_bottom)],
                    fill=color)
                draw.text(
                    (left + margin, text_bottom - text_height - margin),
                    display_str,
                    fill='black',
                    font=font)
                text_bottom -= text_height - 2 * margin

    return np.array(image)
