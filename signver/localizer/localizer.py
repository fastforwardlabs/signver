import tensorflow as tf
import time


class Localizer():
    def __init__(self, detect_threshold=0.5) -> None:
        self.model_load_time = None
        self.detect_fn = None
        self.detect_threshold = detect_threshold
        pass

    def load(self, model_path: str) -> None:
        start_time = time.time()
        self.detect_fn = tf.saved_model.load(model_path)
        self.model_load_time = time.time() - start_time

    def detect(self, input_tensor):
        detections = self.detect_fn(input_tensor)
        return detections
