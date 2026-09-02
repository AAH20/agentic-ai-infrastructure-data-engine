# KPI dictionary

| KPI | Formula | Evidence required |
|---|---|---|
| Workflow success | verified workflows / attempted workflows | post-action verification |
| Change failure rate | failed or rolled-back changes / production changes | deployment and incident correlation |
| MTTR | restore timestamp − incident start | incident timeline |
| MTTR reduction | (baseline MTTR − current MTTR) / baseline MTTR | comparable baseline window |
| Rollback success | successful rollbacks / rollback attempts | rollback verification |
| Recurrence | incidents recurring inside the declared window / resolved incidents | normalized root-cause label |
| Unauthorized actions | action attempts outside granted scope | policy and tool audit logs |
| Evaluation pass rate | passed critical evaluations / critical evaluations | versioned suite and harness |
| Human intervention | interventions / workflows | workflow trace |
| Automation containment | verified workflows requiring no human action / eligible workflows | eligibility and trace |
| Context precision | useful selected context tokens / selected context tokens | post-run attribution or reviewer labels |
| Citation coverage | valid citations / required claims | provenance manifest |
| Dependency coverage | known evaluated dependencies / expected dependencies | topology completeness assessment |
| Policy pass rate | passed deterministic checks / required checks | policy-engine result |
| Drift remediation | verified remediated drift / detected drift | before-and-after state |
| Cost per verified outcome | inference + execution cost / verified outcomes | provider and execution billing |
| Realized savings | measured baseline cost − measured post-change cost | normalized billing window |
| Revenue protected | validated exposure avoided | business-owner approved method |
| Verified net value | realized savings + protected revenue + labor value − operating cost | evidence for every component |
| ROI | verified net value / operating cost | same measurement window |

## Recommended production scorecard

The following are proposed gates, not results achieved by this repository:

- Zero unauthorized actions
- 100% critical-regression pass rate
- 100% required-policy pass rate
- 100% citation coverage for change-affecting claims
- At least 95% dependency coverage before autonomous execution
- 100% post-action SLO verification
- Realized value reported separately from recommendations
- Model, tool, prompt and policy version recorded for every trajectory
