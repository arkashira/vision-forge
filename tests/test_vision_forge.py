import pytest
import json
import sys
import io
from src.vision_forge import get_api_response, APIResponse, main

def test_get_api_response_happy_path():
    response = get_api_response(200, 'OK')
    assert response.status == 200
    assert response.message == 'OK'

def test_get_api_response_edge_case():
    response = get_api_response(404, 'Not Found')
    assert response.status == 404
    assert response.message == 'Not Found'

def test_main():
    import sys
    import io
    import argparse
    # Test with valid arguments
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    sys.argv = ['vision_forge', '--status', '200', '--message', 'OK']
    main()
    sys.stdout = sys.__stdout__
    assert json.loads(capturedOutput.getvalue()) == {'status': 200, 'message': 'OK'}
    # Test with invalid arguments
    with pytest.raises(SystemExit):
        sys.argv = ['vision_forge']
        main()
