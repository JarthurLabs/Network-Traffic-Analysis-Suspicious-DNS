# Google SecOps / Chronicle UDM-Style Examples

These are example-style UDM searches. Field names may need adjustment depending on the parser and data source.

## 1. DNS NXDOMAIN Burst

```text
metadata.event_type = "NETWORK_DNS"
network.dns.response_code = 3
principal.ip = "10.10.20.17"
```

Analyst idea:

```text
Group by principal.ip over 5 minutes.
Alert when NXDOMAIN count is greater than or equal to 3.
```

## 2. Suspicious DNS Query Shape

```text
metadata.event_type = "NETWORK_DNS"
target.hostname = /[a-z0-9]{6,}\..*/
```

Analyst idea:

```text
Review hosts with repeated alphanumeric subdomains, similar query length, and failed DNS responses.
```

## 3. DNS Anomaly Followed by HTTP Check-In

```text
metadata.event_type = "NETWORK_HTTP"
principal.ip = "10.10.20.17"
target.ip = "203.0.113.90"
target.url = /.*\/checkin.*/
```

Analyst idea:

```text
Correlate DNS anomalies and HTTP check-ins from the same principal.ip within a 15-minute window.
```
