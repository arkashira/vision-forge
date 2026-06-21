import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class Model:
    version: str
    weights: str

class VisionForge:
    def __init__(self):
        self.models = {}
        self.default_model = None

    def load_model(self, path):
        with open(path, 'r') as f:
            model_data = json.load(f)
            model = Model(version=model_data['version'], weights=model_data['weights'])
            self.models[model.version] = model
            if self.default_model is None:
                self.default_model = model

    def infer(self, image):
        if self.default_model is None:
            raise ValueError("No model loaded")
        # Simulate inference using the default model
        return f"Inferred using {self.default_model.version}"

def main():
    parser = ArgumentParser(description="Vision Forge CLI")
    parser.add_argument("--load-model", help="Load a model from a file")
    parser.add_argument("--infer", help="Run inference on an image")
    args = parser.parse_args()
    vision_forge = VisionForge()
    if args.load_model:
        vision_forge.load_model(args.load_model)
    if args.infer:
        print(vision_forge.infer(args.infer))

if __name__ == "__main__":
    main()
