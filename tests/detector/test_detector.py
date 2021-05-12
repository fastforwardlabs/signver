from signver.detector import Detector


def test_localizer_load():
    model_path = "models/localizer/ssd640fpnlite/saved_model"
    detector = Detector()
    detector.load(model_path)

    print(detector, detector.model_load_time)
    assert detector.model is not None
