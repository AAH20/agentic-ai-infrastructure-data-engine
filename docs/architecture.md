# Architecture

## Control and data planes

1. **Ingestion:** OpenTelemetry, cloud inventory, Kubernetes events, network state, Git, IaC plans, tickets and billing exports.
2. **Normalization:** canonical resources, changes, incidents, evaluations, interventions and outcomes.
3. **Temporal topology:** dependencies are queried as they existed when an event occurred.
4. **Context compilation:** policy, desired state and observed state outrank retrieved documents.
5. **Inference:** health- and constraint-aware routing across NIM, local models and frontier APIs.
6. **Orchestration:** LangGraph owns durable state; specialist collaboration remains stage-bounded.
7. **Execution:** static analysis, isolated simulation, approval, canary, verification and rollback.
8. **Data flywheel:** each verified or failed trajectory becomes evaluation and training-data input.
9. **Analytics:** reliability, quality, operations and verified economics share one semantic model.

## Production target—not current proof

```text
event bus → lakehouse/trajectory store → temporal graph → feature/evaluation store
    ↓                 ↓                       ↓                 ↓
OpenTelemetry     immutable lineage      GraphRAG          holdout suites
    ↓                 ↓                       ↓                 ↓
NeMo profiling → LangGraph workflow → sandbox/tool adapters → KPI warehouse
```

Production implementation must add tenant isolation, workload identity, secrets management, immutable evidence storage, data residency, signed journal events, high availability and disaster recovery.
