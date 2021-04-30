import tensorflow as tf
import logging
import urllib.request
import os

import io
import numpy as np
from six import BytesIO
from PIL import Image


logger = logging.getLogger(__name__)


def mkdir(dir_path: str, exist_ok: bool=True) -> None:
    os.makedirs(dir_path, exist_ok=exist_ok)


def download_file(file_url: str, file_name: str,  destination_dir: str) -> str:
    mkdir(destination_dir)

    # add header agent as needed
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    logger.info(">> Downloading data file for " + file_url)
    file_path = os.path.join(destination_dir, file_name)
    urllib.request.urlretrieve(file_url, file_path)
    return file_path


def read_file(file_path: str):
    return tf.io.gfile.GFile(file_path, "rb").read()


def img_to_np_array(img_path: str) -> None:
    img = read_file(img_path)
    image = Image.open(BytesIO(img))
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)


def invert_img(img):
    return np.invert(img)
