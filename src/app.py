from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

PROJECT = "water-network-pressure-anomaly-ai"
TITLE = "Water Network Pressure Anomaly AI"
DOMAIN = "iot"
TTE_DAYS = 5
EXPOSURE_SCORE = 7
WAVE = 2
PRIORITY_SCORE = 6.20
RISK_FOCUS = "device trust, telemetry integrity, and fleet resilience"


class ExposureRequest(BaseModel):
    channels: list[str] = Field(default_factory=lambda: ["github", "x", "linkedin"])
    objective: str = Field(default="maximize-qualified-exposure")
    constraints: list[str] = Field(default_factory=list)


class ExposureResponse(BaseModel):
    project: str
    launch_window: str
    risk_level: str
    priority_score: float
    channel_plan: list[str]
    actions: list[str]
    generated_at: str


def _risk_level(priority_score: float, tte_days: int) -> str:
    if priority_score >= 8.5 and tte_days <= 3:
        return "high-urgency"
    if priority_score >= 7.0:
        return "priority"
    return "standard"


def _actions(risk_level: str) -> list[str]:
    if risk_level == "high-urgency":
        return ["ship-demo-48h", "publish-thread", "collect-signal-review"]
    if risk_level == "priority":
        return ["ship-demo-7d", "post-technical-writeup", "track-conversion-signals"]
    return ["prepare-mvp", "document-roadmap"]


app = FastAPI(title=PROJECT, version="0.2.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "project": PROJECT, "domain": DOMAIN}


@app.get("/v1/meta")
def meta() -> dict[str, object]:
    return {
        "id": 151,
        "project": PROJECT,
        "title": TITLE,
        "domain": DOMAIN,
        "tte_days": TTE_DAYS,
        "exposure_score": EXPOSURE_SCORE,
        "wave": WAVE,
        "priority_score": PRIORITY_SCORE,
        "risk_focus": RISK_FOCUS,
    }


@app.post("/v1/exposure-plan", response_model=ExposureResponse)
def exposure_plan(payload: ExposureRequest) -> ExposureResponse:
    level = _risk_level(PRIORITY_SCORE, TTE_DAYS)
    window = "within-48h" if TTE_DAYS <= 3 else "within-7d"
    return ExposureResponse(
        project=PROJECT,
        launch_window=window,
        risk_level=level,
        priority_score=PRIORITY_SCORE,
        channel_plan=payload.channels,
        actions=_actions(level),
        generated_at=datetime.now(timezone.utc).isoformat(),
    )
