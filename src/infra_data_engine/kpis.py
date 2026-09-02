from .models import WorkflowOutcome


def _rate(numerator: float, denominator: float) -> float:
    return round(numerator / denominator, 4) if denominator else 0.0


def calculate_kpis(outcome: WorkflowOutcome) -> dict:
    operating_cost = outcome.inference_cost_usd + outcome.execution_cost_usd
    labor_value = outcome.engineering_hours_saved * outcome.hourly_cost_usd
    verified_value = (
        outcome.realized_savings_usd + outcome.revenue_protected_usd + labor_value
        if outcome.verified else 0.0
    )
    return {
        "reliability": {
            "workflow_success": int(outcome.verified),
            "rollback_success_rate": _rate(outcome.successful_rollbacks, outcome.rollback_attempts),
            "mttr_reduction_rate": _rate(max(outcome.baseline_mttr_minutes - outcome.mttr_minutes, 0), outcome.baseline_mttr_minutes),
            "mttd_minutes": outcome.mttd_minutes,
            "recurrence_rate": int(outcome.recurrence_within_window),
            "unauthorized_actions": outcome.unauthorized_actions,
        },
        "agent_quality": {
            "evaluation_pass_rate": _rate(outcome.evaluations_passed, outcome.evaluations_total),
            "human_interventions_per_workflow": outcome.human_interventions,
            "context_precision": _rate(outcome.useful_context_tokens, outcome.total_context_tokens),
            "citation_coverage": _rate(outcome.citations_present, outcome.citations_required),
            "dependency_coverage": _rate(outcome.dependencies_known, outcome.dependencies_total),
            "tokens_per_verified_workflow": outcome.input_tokens if outcome.verified else None,
        },
        "platform": {
            "policy_pass_rate": _rate(outcome.policy_checks_passed, outcome.policy_checks_total),
            "drift_remediation_rate": _rate(outcome.remediated_drift_items, outcome.detected_drift_items),
            "automation_containment": int(outcome.verified and outcome.human_interventions == 0),
            "rollback_required": int(outcome.rolled_back),
        },
        "economics": {
            "operating_cost_usd": round(operating_cost, 2),
            "verified_value_usd": round(verified_value, 2),
            "cost_per_verified_outcome_usd": round(operating_cost, 2) if outcome.verified else None,
            "net_verified_value_usd": round(verified_value - operating_cost, 2),
            "roi": round((verified_value - operating_cost) / operating_cost, 4) if operating_cost else None,
            "realized_savings_usd": outcome.realized_savings_usd if outcome.verified else 0.0,
            "revenue_protected_usd": outcome.revenue_protected_usd if outcome.verified else 0.0,
            "labor_value_usd": round(labor_value, 2) if outcome.verified else 0.0,
        },
    }


def release_gate(kpis: dict) -> dict:
    checks = {
        "verified": kpis["reliability"]["workflow_success"] == 1,
        "zero_unauthorized_actions": kpis["reliability"]["unauthorized_actions"] == 0,
        "evaluations_complete": kpis["agent_quality"]["evaluation_pass_rate"] == 1,
        "citations_complete": kpis["agent_quality"]["citation_coverage"] == 1,
        "dependency_coverage": kpis["agent_quality"]["dependency_coverage"] >= .95,
        "policy_checks_complete": kpis["platform"]["policy_pass_rate"] == 1,
        "positive_net_value": kpis["economics"]["net_verified_value_usd"] > 0,
    }
    return {"decision": "promote" if all(checks.values()) else "block", "checks": checks}
