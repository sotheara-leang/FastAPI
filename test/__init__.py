from fastapi.testclient import TestClient

from main.application import app

client = TestClient(app)
