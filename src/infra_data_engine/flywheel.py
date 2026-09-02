from dataclasses import asdict
from hashlib import sha256
import json

from .models import WorkflowOutcome


def trajectory_record(outcome: WorkflowOutcome, context: dict, kpis: dict, gate: dict) -> dict:
    payload = {
        "outcome": asdict(outcome),
        "context_manifest": {
            "as_of": context["as_of"],
            "resources": context["resources"],
            "relationship_count": len(context["relationships"]),
        },
        "kpis": kpis,
        "release_gate": gate,
        "labels": {
            "verified_success": outcome.verified,
            "required_rollback": outcome.rolled_back,
            "human_intervention": outcome.human_interventions > 0,
            "recurrence": outcome.recurrence_within_window,
        },
        "evidence_tier": "simulated" if "synthetic" in outcome.tags else "measured",
    }
    payload["trajectory_digest"] = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    payload["next_actions"] = _next_actions(kpis, gate)
    return payload


def _next_actions(kpis: dict, gate: dict) -> list[str]:
    actions = []
    for name, passed in gate["checks"].items():
        if not passed:
            actions.append(f"repair:{name}")
    if kpis["reliability"]["recurrence_rate"]:
        actions.append("create-incident-derived-regression")
    if kpis["agent_quality"]["human_interventions_per_workflow"]:
        actions.append("capture-human-correction-as-candidate-training-data")
    if gate["decision"] == "promote":
        actions.append("eligible-for-independent-holdout-evaluation")
    return actions
