from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.domain_logic import get_profile

PROJECT = "water-network-pressure-anomaly-ai"
TITLE = "Water Network Pressure Anomaly AI"
DOMAIN = "iot"
TTE_DAYS = 5
EXPOSURE_SCORE = 7
WAVE = 2
PRIORITY_SCORE = 6.20

profile = get_profile(DOMAIN)


class ExposureRequest(BaseModel):
    channels: list[str] = Field(default_factory=lambda: ["github", "x", "linkedin"])
    objective: str = Field(default="maximize-qualified-exposure")
    constraints: list[str] = Field(default_factory=list)


class VerticalSignalRequest(BaseModel):
    incident_severity: str = Field(default="medium")
    observed_signals: list[str] = Field(default_factory=list)


def _risk_level(priority_score: float, tte_days: int) -> str:
    if priority_score >= 8.5 and tte_days <= 3:
        return "high-urgency"
    if priority_score >= 7.0:
        return "priority"
    return "standard"


def _launch_window(tte_days: int) -> str:
    if tte_days <= 2:
        return "within-24h"
    if tte_days <= 3:
        return "within-48h"
    return "within-7d"


app = FastAPI(title=PROJECT, version="0.3.0")


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
        "key_metric": profile.key_metric,
        "controls": profile.controls,
    }


@app.post("/v1/exposure-plan")
def exposure_plan(payload: ExposureRequest) -> dict[str, object]:
    level = _risk_level(PRIORITY_SCORE, TTE_DAYS)
    return {
        "project": PROJECT,
        "risk_level": level,
        "launch_window": _launch_window(TTE_DAYS),
        "channels": payload.channels,
        "objective": payload.objective,
        "actions": profile.default_actions,
        "demo_assets": profile.demo_assets,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/v1/vertical-signal")
def vertical_signal(payload: VerticalSignalRequest) -> dict[str, object]:
    confidence = min(0.95, 0.45 + (len(payload.observed_signals) * 0.08))
    return {
        "project": PROJECT,
        "domain": DOMAIN,
        "incident_severity": payload.incident_severity,
        "signal_count": len(payload.observed_signals),
        "confidence": round(confidence, 2),
        "key_metric": profile.key_metric,
        "recommended_controls": profile.controls,
        "next_actions": profile.default_actions,
    }
