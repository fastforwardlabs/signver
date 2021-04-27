import tensorflow as tf


class Localizer():
    def __init__(self) -> None:

        pass

    def load(self, model_path: str) -> None:
        self.model_fn = tf.saved_model.load(model_path)

    def detect(self, input_tensor):
        return self.model_fn.detect(input_tensor)
