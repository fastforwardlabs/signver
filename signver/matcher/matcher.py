
import tensorflow as tf


class Matcher():
    def __init__(self):
        self.extractor_type = ""

    def verify(query, query2) -> bool:
        return True

    def match(query, ):
        return True

    def load(self, model_path: str):
        self.detect_fn = tf.saved_model.load(model_path)
