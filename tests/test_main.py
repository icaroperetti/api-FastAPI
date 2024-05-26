from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    respose = client.get("/health-check")
    assert respose.status_code == 200
    assert respose.json() == {"status": "ok"}
