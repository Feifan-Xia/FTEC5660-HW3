"""Offline tests for the Fisher agent software behaviour."""

from __future__ import annotations

import asyncio
import json
import unittest
from pathlib import Path

import hw3


class BrokenChain:
    """Simulate an unavailable model while keeping collected evidence intact."""

    async def ainvoke(self, values):
        raise RuntimeError("simulated API failure")


class FisherAgentTests(unittest.TestCase):
    def test_public_set_completes_with_semantic_fallback(self) -> None:
        root = Path(__file__).resolve().parents[1]
        data = root / "public_test"
        folders = hw3.company_folders(data)
        companies = {path.name: hw3.make_tools(path) for path in folders}

        analyses = asyncio.run(
            hw3.analyze_companies({"chain": BrokenChain()}, companies)
        )
        truth = hw3.read_ground_truth(data)
        names = [path.name for path in folders]

        self.assertEqual(set(analyses), set(companies))
        self.assertEqual(
            hw3.balanced_point_accuracy(analyses, truth, names, hw3.CHOSEN_POINTS),
            1.0,
        )
        for name, entry in analyses.items():
            self.assertEqual(set(entry["points"]), set(hw3.CHOSEN_POINTS))
            self.assertTrue(entry["summary"].strip(), name)

    def test_markdown_fenced_json_is_parsed(self) -> None:
        payload = {
            "points": {"4": "PASS", "7": "PASS", "11": "FAIL"},
            "summary": "Supported by the supplied interviews.",
        }
        parsed = hw3._parse_json_object(
            f"```json\n{json.dumps(payload)}\n```"
        )
        self.assertEqual(parsed, payload)

    def test_fallback_handles_opposite_competitive_signals(self) -> None:
        self.assertEqual(
            hw3._fallback_verdict(
                11, "Customers who switch to us usually go back to them."
            ),
            "PASS",
        )
        self.assertEqual(
            hw3._fallback_verdict(
                11, "Nothing they make is hard to copy; it is a price fight."
            ),
            "FAIL",
        )


if __name__ == "__main__":
    unittest.main()
