import time
from dataclasses import dataclass
from typing import List

@dataclass
class Detection:
    class_id: int
    confidence: float
    bounding_box: List[float]

class InferenceEngine:
    def __init__(self):
        self.model = None  # placeholder for a real model
        self.latency_log = []

    def infer(self, image):
        if image is None:
            raise AttributeError("Image cannot be None")
        start_time = time.time()
        # simulate inference
        detections = [Detection(1, 0.8, [10, 10, 50, 50])]
        end_time = time.time()
        latency = end_time - start_time
        self.latency_log.append(latency)
        return detections

    def get_latency_log(self):
        return self.latency_log
