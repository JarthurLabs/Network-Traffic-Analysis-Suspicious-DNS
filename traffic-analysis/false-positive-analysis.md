# False Positive Analysis

## Purpose

Good analysts consider benign explanations before escalating. This section documents what else could look similar.

| Possible Benign Cause | Why It Can Look Similar | Validation Step |
|---|---|---|
| Software update service | Update clients may query CDNs frequently | Check vendor documentation and process name |
| Browser prefetching | Browsers may pre-resolve domains | Compare with browser history and user activity |
| Security tool telemetry | EDR/DNS tools may beacon normally | Validate installed agent and known destinations |
| Misconfigured internal app | Broken apps may create repeated DNS failures | Ask asset owner and review application logs |
| Ad/tracker traffic | Websites can trigger unusual domains | Correlate with browsing session and known ad domains |

## Analyst Decision

The traffic remains suspicious because of the combination of random-looking DNS, NXDOMAIN responses, newly observed destination, and repeated HTTP check-ins. However, endpoint telemetry is required before confirming compromise.
