# Detection Ideas

## High NXDOMAIN Volume

```text
dns.response=NXDOMAIN
| stats count by source_host
| where count > 20
```

## New Domain Followed by HTTP Check-In

```text
dns.query_status=resolved
| join source_host destination_ip
| search http.path="/checkin"
```

## Tuning Notes

- Exclude known software update domains.
- Baseline normal DNS volume by host.
- Review repeated intervals.
- Correlate DNS with proxy, firewall, and endpoint logs.
