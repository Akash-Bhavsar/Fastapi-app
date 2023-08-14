import unittest
from fastapi.testclient import TestClient
from main import app 
from unittest.mock import MagicMock, patch

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch('git.Repo')
    def test_sha_comparison(self, mock_repo):
        mock_instance = MagicMock()
        mock_instance.head.object.hexsha = "mock_sha"
        mock_repo.return_value = mock_instance

        response = self.client.get("/")
        data = response.json()

        expected_data = {
            "FastAPI": {
                "version": "1.0.0",
                "description": "This App demonstrate a Fast API example and some github actions",
                "sha": "mock_sha"
            }
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, expected_data)

if __name__ == "__main__":
    unittest.main()
