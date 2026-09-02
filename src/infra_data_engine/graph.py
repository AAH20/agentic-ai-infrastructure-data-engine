from collections import defaultdict, deque

from .models import TopologyEdge


class TemporalTopology:
    def __init__(self, edges: list[TopologyEdge]):
        self.edges = edges

    def context(self, roots: tuple[str, ...], at: str, max_hops: int = 3) -> dict:
        adjacency: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for edge in self.edges:
            active = edge.valid_from <= at and (edge.valid_to is None or at < edge.valid_to)
            if active:
                adjacency[edge.source].append((edge.target, edge.relation))
                adjacency[edge.target].append((edge.source, f"inverse:{edge.relation}"))
        queue = deque((root, 0) for root in roots)
        visited: set[str] = set()
        relationships = []
        while queue:
            node, depth = queue.popleft()
            if node in visited or depth > max_hops:
                continue
            visited.add(node)
            for neighbor, relation in sorted(adjacency[node]):
                relationships.append({"source": node, "target": neighbor, "relation": relation, "depth": depth + 1})
                if neighbor not in visited:
                    queue.append((neighbor, depth + 1))
        return {
            "as_of": at,
            "roots": list(roots),
            "max_hops": max_hops,
            "resources": sorted(visited),
            "relationships": relationships,
        }
