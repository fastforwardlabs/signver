
import tensorflow as tf


class BaseExtractor():
    def __init__(self):
        self.extractor_type = ""

    def load(self, model_path: str):
        self.detect_fn = tf.saved_model.load(model_path)
