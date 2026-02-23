from dataclasses import dataclass


@dataclass(frozen=True)
class DomainProfile:
    name: str
    key_metric: str
    controls: list[str]
    demo_assets: list[str]
    default_actions: list[str]


PROFILES = {
    "security-agent": DomainProfile(
        name="security-agent",
        key_metric="mean-time-to-contain",
        controls=["identity-hardening", "runtime-guardrails", "audit-trails"],
        demo_assets=["incident-brief", "risk-heatmap", "playbook-timeline"],
        default_actions=["escalate-soc", "open-incident", "contain-scope"],
    ),
    "infrastructure": DomainProfile(
        name="infrastructure",
        key_metric="slo-burn-rate",
        controls=["change-risk-check", "rollback-safety", "dependency-health"],
        demo_assets=["service-map", "latency-trend", "capacity-forecast"],
        default_actions=["freeze-risky-change", "trigger-failover-drill", "rebalance-capacity"],
    ),
    "iot": DomainProfile(
        name="iot",
        key_metric="fleet-anomaly-density",
        controls=["device-attestation", "firmware-safety", "sensor-integrity"],
        demo_assets=["fleet-map", "device-risk-table", "telemetry-sparkline"],
        default_actions=["quarantine-device", "rollback-firmware", "dispatch-maintenance"],
    ),
    "internet": DomainProfile(
        name="internet",
        key_metric="signal-propagation-velocity",
        controls=["source-validation", "abuse-throttling", "crawler-safety"],
        demo_assets=["signal-graph", "campaign-velocity-chart", "source-confidence-grid"],
        default_actions=["flag-high-velocity-signal", "publish-advisory", "increase-monitoring"],
    ),
    "spatial-3d": DomainProfile(
        name="spatial-3d",
        key_metric="operator-decision-latency",
        controls=["scene-integrity", "event-time-sync", "view-state-audit"],
        demo_assets=["3d-scene", "timeline-playback", "threat-cluster-view"],
        default_actions=["focus-hotspot-cluster", "replay-last-incident", "export-scene-state"],
    ),
    "ai-growth": DomainProfile(
        name="ai-growth",
        key_metric="exposure-conversion-rate",
        controls=["launch-window-validation", "channel-attribution", "experiment-tracking"],
        demo_assets=["launch-calendar", "conversion-funnel", "channel-performance-board"],
        default_actions=["ship-demo-now", "publish-launch-thread", "schedule-48h-retrospective"],
    ),
}


def get_profile(domain: str) -> DomainProfile:
    return PROFILES.get(
        domain,
        DomainProfile(
            name=domain,
            key_metric="execution-readiness",
            controls=["baseline-validation"],
            demo_assets=["project-summary"],
            default_actions=["review-scope"],
        ),
    )
