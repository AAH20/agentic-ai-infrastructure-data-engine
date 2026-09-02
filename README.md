# Agentic AI Infrastructure Operations Data Engine

**AI infrastructure · AIOps · platform engineering · NVIDIA NIM · Kubernetes · Terraform · OpenTofu · cloud cost optimization · FinOps · observability · network automation · Ansible · GraphRAG · compliance as code**

[![CI](https://github.com/AAH20/agentic-ai-infrastructure-data-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/AAH20/agentic-ai-infrastructure-data-engine/actions/workflows/ci.yml) [![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](pyproject.toml) [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An infrastructure intelligence and evaluation platform that converts cloud changes, Kubernetes incidents, network failures, configuration drift, human interventions and verified remediations into reusable training data, regression evaluations and evidence-gated automation.

> **Evidence boundary:** the temporal topology engine, KPI calculations, release gate and trajectory data flywheel are implemented and tested locally. The included incident and economic values are synthetic. NVIDIA NIM, agent frameworks, cloud providers and infrastructure tools are versioned integration contracts—not claimed live executions.

## Why this exists

AI can generate application changes faster than platform teams can safely absorb them. Generic agents lack current topology, operational ground truth, authorization boundaries, infrastructure-specific evaluations and verified business outcomes. This project makes those assets the system of record.

```text
OpenTelemetry + cloud + Kubernetes + network + IaC + incidents
                              ↓
           temporal topology and infrastructure GraphRAG
                              ↓
        authority-aware context + multi-model agent workflow
                              ↓
        simulate → evaluate → approve → canary → verify
                              ↓
      hashed trajectory + KPIs + regression + skill candidate
```

## Run the proof

```bash
PYTHONPATH=src python3 -m infra_data_engine.cli examples/synthetic-incident.json
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## Implemented

- Time-aware topology context with active/expired dependency relationships
- Operational trajectory normalization and SHA-256 evidence digest
- Reliability, agent-quality, platform and verified-economic KPIs
- Deterministic promotion/block release gate
- Failure-derived remediation and evaluation actions
- Synthetic Kubernetes/network/Terraform incident
- Framework, NVIDIA NIM, IaC, network automation and compliance contracts
- BI semantic model separating identified, approved and realized value

## Orchestration authority

| Component | Responsibility |
|---|---|
| Paperclip | Goals, budgets, assignments and outcomes |
| OpenClaw-compatible gateway | Persistent operator interface, schedules and reusable skills |
| LangGraph | Authoritative durable workflow state |
| CrewAI | Specialist collaboration inside bounded stages |
| LangChain | Model, retriever and tool adapters |
| NVIDIA NeMo Agent Toolkit | Profiling, evaluation and observability |
| Temporal GraphRAG | Dependency-aware operational context |
| Deterministic policy engine | Final authorization |

Framework names do not imply that all frameworks belong in one hot path. The contract deliberately prevents competing state owners.

## Infrastructure automation coverage

- **Infrastructure as Code:** Terraform, OpenTofu, Bicep, CloudFormation, Pulumi, Helm and Kustomize
- **Network automation:** Ansible, Nornir, Netmiko, NAPALM, Batfish, pyATS, containerlab, NETCONF and RESTCONF
- **Configuration management:** Chef, Puppet and Ansible
- **Compliance as Code:** OPA, Conftest, Checkov, InSpec, Azure Policy, AWS Config and Google Organization Policy
- **Observability:** OpenTelemetry, Prometheus, Grafana, Loki, Elastic, Splunk and Datadog

## KPI system

The engine calculates:

- Workflow success and change verification
- MTTD, MTTR and MTTR reduction
- Incident recurrence and rollback success
- Unauthorized actions
- Evaluation and policy pass rates
- Human interventions and automation containment
- Context precision, citation coverage and dependency coverage
- Drift-remediation rate
- Inference and execution cost
- Cost per verified outcome
- Realized cloud savings, revenue protected and labor value
- Verified net value and ROI

See the [KPI dictionary](docs/kpi-dictionary.md). Values that have not been verified after execution never become realized value.

## Search and role alignment

The documentation uses accurate, demand-aligned terminology: AI Platform Engineer, Principal Cloud Architect, Forward Deployed Engineer, Site Reliability Engineer, Platform Engineering, DevOps, MLOps, LLMOps, AIOps, Kubernetes, Terraform, OpenTofu, Infrastructure as Code, NVIDIA NIM, NeMo Agent Toolkit, LangGraph, LangChain, GraphRAG, OpenTelemetry, FinOps, cloud cost optimization, network automation, Ansible and compliance as code.

No search-volume figures are claimed without exportable keyword-planner evidence. See [search positioning](docs/search-positioning.md).

## Engage

[Request an AI infrastructure and AIOps architecture assessment](https://a2zsoc.com/contact?topic=agentic-ai-infrastructure-data-engine&utm_source=github&utm_medium=repository).
