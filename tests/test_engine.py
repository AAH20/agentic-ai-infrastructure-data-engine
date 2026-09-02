import copy
import json
from pathlib import Path
import unittest

from infra_data_engine.engine import analyze
from infra_data_engine.graph import TemporalTopology
from infra_data_engine.io import load_case
from infra_data_engine.models import TopologyEdge


CASE = json.loads((Path(__file__).parents[1] / "examples" / "synthetic-incident.json").read_text())


class EngineTests(unittest.TestCase):
    def test_verified_case_produces_value_and_holdout_action(self):
        result = analyze(*load_case(CASE))
        self.assertEqual(result["release_gate"]["decision"], "promote")
        self.assertEqual(result["next_actions"], [
            "capture-human-correction-as-candidate-training-data",
            "eligible-for-independent-holdout-evaluation",
        ])
        self.assertGreater(result["kpis"]["economics"]["net_verified_value_usd"], 0)
        self.assertEqual(len(result["trajectory_digest"]), 64)

    def test_failed_evaluations_block_release_and_value(self):
        case = copy.deepcopy(CASE)
        case["outcome"]["verified"] = False
        case["outcome"]["evaluations_passed"] = 10
        result = analyze(*load_case(case))
        self.assertEqual(result["release_gate"]["decision"], "block")
        self.assertEqual(result["kpis"]["economics"]["verified_value_usd"], 0)
        self.assertIn("repair:evaluations_complete", result["next_actions"])

    def test_temporal_graph_excludes_expired_relationship(self):
        edges = [TopologyEdge("app", "old-db", "DEPENDS_ON", "2025", "2026")]
        result = TemporalTopology(edges).context(("app",), "2027")
        self.assertEqual(result["resources"], ["app"])

    def test_unauthorized_action_is_hard_block(self):
        case = copy.deepcopy(CASE)
        case["outcome"]["unauthorized_actions"] = 1
        result = analyze(*load_case(case))
        self.assertFalse(result["release_gate"]["checks"]["zero_unauthorized_actions"])


if __name__ == "__main__":
    unittest.main()
