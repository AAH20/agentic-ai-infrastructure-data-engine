from .models import TopologyEdge, WorkflowOutcome


def load_case(document: dict) -> tuple[list[TopologyEdge], tuple[str, ...], str, WorkflowOutcome]:
    edges = [TopologyEdge(**edge) for edge in document["topology_edges"]]
    outcome = dict(document["outcome"])
    outcome["tags"] = tuple(outcome.get("tags", []))
    return edges, tuple(document["roots"]), document["as_of"], WorkflowOutcome(**outcome)
