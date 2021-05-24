from signver.extractor import MetricExtractor


def test_extractor_load():
    model_path = "models/extractor/metric"
    detector = MetricExtractor(model_path=model_path)

    assert detector.model is not None
