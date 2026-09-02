from dataclasses import dataclass, field


@dataclass(frozen=True)
class InfraEvent:
    event_id: str
    timestamp: str
    source: str
    environment: str
    resource_id: str
    event_type: str
    severity: str
    change_id: str | None = None
    incident_id: str | None = None
    evidence_digest: str = ""


@dataclass(frozen=True)
class TopologyEdge:
    source: str
    target: str
    relation: str
    valid_from: str
    valid_to: str | None = None


@dataclass(frozen=True)
class WorkflowOutcome:
    workflow_id: str
    status: str
    applied: bool
    verified: bool
    rolled_back: bool
    human_interventions: int
    unauthorized_actions: int
    inference_cost_usd: float
    execution_cost_usd: float
    realized_savings_usd: float
    revenue_protected_usd: float
    engineering_hours_saved: float
    hourly_cost_usd: float
    input_tokens: int
    useful_context_tokens: int
    total_context_tokens: int
    citations_required: int
    citations_present: int
    dependencies_known: int
    dependencies_total: int
    evaluations_passed: int
    evaluations_total: int
    policy_checks_passed: int
    policy_checks_total: int
    remediated_drift_items: int
    detected_drift_items: int
    mttr_minutes: float
    baseline_mttr_minutes: float
    mttd_minutes: float
    rollback_attempts: int
    successful_rollbacks: int
    recurrence_within_window: bool
    tags: tuple[str, ...] = field(default_factory=tuple)
