from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Budgets:
    # Simple demo budgets; tune per benchmark
    max_latency_ms: float = 50.0


def within_latency_budget(latency_ms: float, budgets: Budgets) -> bool:
    return latency_ms <= budgets.max_latency_ms
