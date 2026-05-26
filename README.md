# Network Traffic Analysis: Suspicious DNS Activity

## Overview

This repository contains a network traffic analysis investigation using synthetic DNS and HTTP event data. It demonstrates how to identify suspicious DNS patterns, correlate them with outbound HTTP connections, document indicators, and recommend defensive actions.

The focus is practical analyst work: review network events, identify patterns, separate normal vendor traffic from suspicious behavior, document indicators, and explain containment recommendations.

> All hosts, domains, IP addresses, timestamps, and traffic records are synthetic and safe for public use.

---

## Scenario

A billing workstation generated a burst of random-looking DNS queries followed by repeated HTTP connections to a newly observed destination. The user also reported browser pop-ups and system slowness. The analyst needs to determine whether the activity is benign, suspicious, or requires containment.

The investigation answers five questions:

1. Which host generated the suspicious traffic?
2. What DNS pattern was observed?
3. Did the DNS activity correlate with outbound HTTP traffic?
4. What indicators should be documented?
5. What defensive actions should be recommended?

---

## Target Roles

| Role | Why This Repository Fits |
|---|---|
| SOC Analyst | Shows network event review, IOC documentation, and triage logic |
| Cybersecurity Analyst | Demonstrates DNS/HTTP analysis and defensive recommendations |
| Incident Response Analyst, beginner | Connects suspicious traffic to containment steps |
| Security Implementation Specialist | Connects findings to DNS filtering, logging, and endpoint hardening improvements |

---

## Core Deliverables

| Area | Deliverables |
|---|---|
| DNS Analysis | Synthetic DNS event review and suspicious pattern notes |
| HTTP Correlation | Outbound connection review after DNS anomalies |
| IOC Documentation | Domain, IP, and host indicators |
| Detection Logic | DNS anomaly and HTTP check-in detection examples |
| Response | Containment and remediation recommendations |
| Reporting | Executive summary and analyst report |

---

## Analysis Workflow

![Analysis Workflow](./screenshots/analysis-workflow.svg)

---

## DNS Activity Dashboard

The DNS dashboard shows repeated random-looking queries from one internal workstation.

![DNS Activity Dashboard](./screenshots/dns-activity-dashboard.svg)

---

## HTTP Flow Summary

The HTTP flow summary shows repeated outbound check-ins after the suspicious DNS activity.

![HTTP Flow Summary](./screenshots/http-flow-summary.svg)

---

## IOC Table

Indicators are documented with reason and recommended defensive action.

![IOC Table](./screenshots/ioc-table.svg)

---

## Recommendation Matrix

Recommendations are prioritized by security value and business reason.

![Recommendation Matrix](./screenshots/recommendation-matrix.svg)

---

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── COMMIT_GUIDE.md
├── traffic-analysis/
├── data/
├── evidence/
├── detection-logic/
├── response/
├── reports/
├── screenshots/
└── templates/
```

---

## Key Evidence Files

| File | Purpose |
|---|---|
| `data/dns-events.csv` | Synthetic DNS query evidence |
| `data/http-connections.csv` | Synthetic outbound HTTP flow evidence |
| `data/ioc-list.csv` | Indicator list with action recommendations |
| `data/recommendations.csv` | Defensive recommendation matrix |
| `traffic-analysis/dns-analysis-notes.md` | Analyst review of DNS behavior |
| `traffic-analysis/http-correlation-notes.md` | DNS-to-HTTP correlation notes |
| `detection-logic/detection-ideas.md` | Defensive detection concepts |

---

## Analyst Conclusion

The activity should be treated as suspicious because one workstation generated repeated random-looking DNS queries and then made repeated outbound HTTP requests to a newly observed destination. The recommended response is to isolate the host, block observed indicators pending validation, review endpoint telemetry, and improve DNS anomaly detection.

---

## Limitations

This is a synthetic network traffic analysis project. It does not contain real packet captures, malware, production logs, or customer data.
