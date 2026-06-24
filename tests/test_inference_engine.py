from inference_engine import InferenceEngine, Detection
import pytest

def test_infer():
    engine = InferenceEngine()
    image = b"dummy_image_data"
    detections = engine.infer(image)
    assert len(detections) == 1
    assert detections[0].class_id == 1
    assert detections[0].confidence == 0.8
    assert detections[0].bounding_box == [10, 10, 50, 50]

def test_latency_log():
    engine = InferenceEngine()
    image = b"dummy_image_data"
    engine.infer(image)
    latency_log = engine.get_latency_log()
    assert len(latency_log) == 1
    assert latency_log[0] > 0

def test_infer_edge_case():
    engine = InferenceEngine()
    image = None
    with pytest.raises(AttributeError):
        engine.infer(image)
