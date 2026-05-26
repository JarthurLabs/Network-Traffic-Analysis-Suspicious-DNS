# Splunk SPL Examples

These are example-style searches for a lab environment. Field names may need to be adjusted for a real SIEM.

## 1. DNS NXDOMAIN Burst by Host

```spl
index=dns sourcetype=dns_logs response="NXDOMAIN"
| bin _time span=5m
| stats count as nxdomain_count values(query) as queries by _time, src_ip
| where nxdomain_count >= 3
```

## 2. Random-Looking Subdomain Pattern

```spl
index=dns sourcetype=dns_logs
| eval subdomain=mvindex(split(query,"."),0)
| eval subdomain_length=len(subdomain)
| where subdomain_length >= 6 AND match(subdomain, "^[a-z0-9]+$")
| stats count values(query) as queries by src_ip
| where count >= 3
```

## 3. DNS Anomaly Followed by HTTP Check-In

```spl
(index=dns sourcetype=dns_logs response="NXDOMAIN") OR (index=proxy sourcetype=http_logs uri_path="/checkin")
| bin _time span=15m
| stats values(query) as dns_queries values(uri_path) as http_paths values(dest_ip) as destinations by _time, src_ip
| search http_paths="/checkin"
```
