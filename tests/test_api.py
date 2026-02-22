from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_meta_shape() -> None:
    response = client.get("/v1/meta")
    assert response.status_code == 200
    payload = response.json()
    assert "priority_score" in payload
    assert "risk_focus" in payload


def test_exposure_plan() -> None:
    response = client.post(
        "/v1/exposure-plan",
        json={"channels": ["github"], "objective": "ship-fast", "constraints": ["small-team"]},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["launch_window"] in {"within-48h", "within-7d"}
    assert len(payload["actions"]) >= 1
