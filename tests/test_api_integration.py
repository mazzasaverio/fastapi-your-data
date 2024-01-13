# tests/test_api_integration.py
import pytest
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json
import os
from dotenv import load_dotenv
from loguru import logger

# Load environment variables from .env file for the test
load_dotenv()

# The base URL of the FastAPI server
BASE_URL = "http://127.0.0.1:8000"

# The endpoint to test
ENDPOINT = "/documents/"

# The API key for authentication
API_KEY = os.getenv("API_KEY")


def make_request_to_documents(api_key):
    """Make a request to the /documents/ endpoint."""
    request = Request(f"{BASE_URL}{ENDPOINT}")
    request.add_header("accept", "application/json")
    request.add_header("access_token", api_key)

    try:
        response = urlopen(request)
        data = response.read().decode("utf-8")
        return json.loads(data)
    except HTTPError as e:
        return e.code
    except URLError as e:
        return e.reason


@pytest.mark.parametrize("api_key", [API_KEY])
def test_documents_endpoint(api_key):
    """Test the /documents/ endpoint with the provided API key."""
    result = make_request_to_documents(api_key)

    print(result)

    # Assert the result is a list of documents, indicating a successful response
    assert isinstance(result, list), f"Expected a list of documents, got {type(result)}"

    # If we receive an HTTP error code, we assert that it's not a client or server error
    if isinstance(result, int):
        assert 400 > result, f"Client error occurred: HTTP status {result}"
        assert 500 > result, f"Server error occurred: HTTP status {result}"

    # If we receive a URLError, we fail the test with the reason
    if isinstance(result, str):
        pytest.fail(f"URLError occurred: {result}")


# If the script is run directly, we'll invoke pytest to run the tests contained in this file
if __name__ == "__main__":
    pytest.main()
