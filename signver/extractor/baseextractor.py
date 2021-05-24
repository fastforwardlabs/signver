
import tensorflow as tf

model_path_dict = {"pretrained": "models/extractor/pretrained",
                   "metric": "models/extractor/metric"}


class BaseExtractor():
    def __init__(self, model_path=None, model_type="metric", batch_size=64):
        self.model_type = model_type
        self.batch_size = batch_size
        self.model_path = model_path if model_path else model_path_dict[model_type]
        self.load(self.model_path)

    def load(self, model_path: str):
        self.model = tf.saved_model.load(model_path)

    def extract(self, image_np):
        return self.model.predict(image_np, batch_size=self.batch_size)
