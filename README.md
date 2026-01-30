# AlphaEvolve Intelligence Optimization Sandbox

A public **mission-oriented optimization sandbox** inspired by AlphaEvolve-style workflows, demonstrating how AI systems can propose algorithmic changes **only when evaluator metrics improve**.

This project is designed as a safe, unclassified portfolio artifact for **Intelligence Community mission engineering**, focused on:

- Evaluator-driven optimization loops  
- Governance + latency budget enforcement  
- Benchmarks aligned to analytic workflows (clustering + watchlisting/entity resolution + rare-event detection)  
- Auditable run artifacts + one-page summaries  
- CI-backed reproducibility  

> **Note:** This is a simulation of evaluator-governed optimization principles — **not** Google/DeepMind source code.

---

## Architecture (Evaluator Loop)

```text
Candidate (params) ──► Propose ──► Evaluate ──► Governance Gates ──► Accept/Reject
        ▲                               │              │
        │                               ▼              ▼
        └────────────── Best so far ◄── Score      Latency/Bounds
                                       │
                                       ▼
                               Auditable Report (.json)
                               One-page Summary (.md)
Mermaid diagram (renders on GitHub)
flowchart LR
  A[Candidate params] --> B[Propose variation]
  B --> C[Evaluate benchmark]
  C --> D{Governance gates<br/>bounds + latency}
  D -- pass --> E[Accept update]
  D -- fail --> F[Reject]
  E --> G[Best candidate so far]
  F --> G
  C --> H[Report JSON]
  H --> I[One-page summary.md]
Why this matters (IC / MEMO relevance)
In mission environments, optimization is not just “higher accuracy.” Candidate changes must satisfy:

performance constraints (latency budgets)

governance bounds (safe parameter ranges)

repeatability + auditability

operational acceptance criteria

This sandbox demonstrates evaluator-governed optimization patterns in a transparent, mission-first framework.

Benchmarks included
✅ Toy clustering (toy_clustering)
Optimizes clustering configuration under governance constraints.

✅ Entity resolution / watchlisting (entity_resolution)
Simulates identity matching with synthetic alias/noise generation and F1 scoring under latency gating.

✅ Anomaly detection / rare event flagging (anomaly_detection)
Simulates rare-event detection (outliers/spikes) by evolving detection sensitivity and scoring F1 under mission constraints.

Quickstart (Windows)
1) Create environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
2) Run benchmarks
# Clustering
.\run.ps1 --benchmark toy_clustering --steps 25

# Watchlisting / entity resolution
.\run.ps1 --benchmark entity_resolution --steps 25

# Rare event / anomaly detection
.\run.ps1 --benchmark anomaly_detection --steps 25
Each run produces an auditable JSON artifact:

run_reports/<benchmark>_report.json

Auto-generated one-page run summary
After each run, the repo writes a recruiter-readable summary:

run_reports/latest_summary.md

This includes:

best candidate parameters

best quality score

governance + latency status

traceable optimization step

Continuous integration
GitHub Actions runs on every push:

Ruff lint checks

Pytest unit tests

Disclaimer
This repository is a public demonstration project intended for professional portfolio use.

It contains:

no classified data

no operational watchlists

no government system code

All benchmarks are synthetic and designed for safe, open experimentation.

Author
Mike McKeever
GitHub: https://github.com/MLM2
