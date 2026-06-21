import pytest
from vision_forge import VisionForge, Model

def test_load_model():
    vision_forge = VisionForge()
    model_data = '{"version": "1.0", "weights": "model_weights"}'
    with open("model.json", "w") as f:
        f.write(model_data)
    vision_forge.load_model("model.json")
    assert len(vision_forge.models) == 1
    assert vision_forge.default_model.version == "1.0"

def test_infer():
    vision_forge = VisionForge()
    model_data = '{"version": "1.0", "weights": "model_weights"}'
    with open("model.json", "w") as f:
        f.write(model_data)
    vision_forge.load_model("model.json")
    result = vision_forge.infer("image.jpg")
    assert result == "Inferred using 1.0"

def test_infer_no_model():
    vision_forge = VisionForge()
    with pytest.raises(ValueError):
        vision_forge.infer("image.jpg")

def test_load_model_versioning():
    vision_forge = VisionForge()
    model_data_v1 = '{"version": "1.0", "weights": "model_weights_v1"}'
    model_data_v2 = '{"version": "2.0", "weights": "model_weights_v2"}'
    with open("model_v1.json", "w") as f:
        f.write(model_data_v1)
    with open("model_v2.json", "w") as f:
        f.write(model_data_v2)
    vision_forge.load_model("model_v1.json")
    vision_forge.load_model("model_v2.json")
    assert len(vision_forge.models) == 2
    assert vision_forge.default_model.version == "1.0"
