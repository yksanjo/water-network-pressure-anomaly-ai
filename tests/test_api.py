from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_meta_includes_controls() -> None:
    response = client.get("/v1/meta")
    assert response.status_code == 200
    payload = response.json()
    assert "controls" in payload
    assert len(payload["controls"]) >= 1


def test_vertical_signal() -> None:
    response = client.post(
        "/v1/vertical-signal",
        json={"incident_severity": "high", "observed_signals": ["drift", "outage"]},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["confidence"] >= 0.45
    assert len(payload["next_actions"]) >= 1
