from .flywheel import trajectory_record
from .graph import TemporalTopology
from .kpis import calculate_kpis, release_gate
from .models import TopologyEdge, WorkflowOutcome


def analyze(edges: list[TopologyEdge], roots: tuple[str, ...], at: str, outcome: WorkflowOutcome) -> dict:
    context = TemporalTopology(edges).context(roots, at)
    kpis = calculate_kpis(outcome)
    gate = release_gate(kpis)
    return trajectory_record(outcome, context, kpis, gate)
