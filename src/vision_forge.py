import json
import argparse
from dataclasses import dataclass

@dataclass
class APIResponse:
    status: int
    message: str

def get_api_response(status: int, message: str) -> APIResponse:
    return APIResponse(status, message)

def main():
    parser = argparse.ArgumentParser(description='Vision Forge API')
    parser.add_argument('--status', type=int, help='Status code', required=True)
    parser.add_argument('--message', type=str, help='Message', required=True)
    args = parser.parse_args()
    response = get_api_response(args.status, args.message)
    print(json.dumps(response.__dict__))

if __name__ == '__main__':
    main()
