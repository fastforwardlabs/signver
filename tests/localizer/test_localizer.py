from signver.localizer import Localizer


def test_localizer_load():
    model_path = "models/localizer/ssd640fpnlite/saved_model"
    localizer = Localizer()
    localizer.load(model_path)

    print(localizer, localizer.model_load_time)
    assert localizer.detect_fn is not None
