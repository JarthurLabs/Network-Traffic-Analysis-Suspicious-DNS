# Microsoft Sentinel KQL Examples

These are example-style KQL searches. Table and field names may vary by environment.

## 1. DNS NXDOMAIN Burst

```kql
DnsEvents
| where ResponseCodeName == "NXDOMAIN"
| summarize NXDomainCount=count(), Queries=make_set(Name) by SrcIpAddr, bin(TimeGenerated, 5m)
| where NXDomainCount >= 3
```

## 2. Random-Looking Subdomain Pattern

```kql
DnsEvents
| extend Subdomain = tostring(split(Name, ".")[0])
| extend SubdomainLength = strlen(Subdomain)
| where SubdomainLength >= 6
| where Subdomain matches regex @"^[a-z0-9]+$"
| summarize QueryCount=count(), Queries=make_set(Name) by SrcIpAddr, bin(TimeGenerated, 5m)
| where QueryCount >= 3
```

## 3. DNS Burst Followed by HTTP Check-In

```kql
let suspicious_dns =
DnsEvents
| where ResponseCodeName == "NXDOMAIN"
| summarize NXDomainCount=count() by SrcIpAddr, bin(TimeGenerated, 15m)
| where NXDomainCount >= 3;
let checkins =
CommonSecurityLog
| where RequestURL has "/checkin"
| summarize CheckinCount=count(), Destinations=make_set(DestinationIP) by SourceIP, bin(TimeGenerated, 15m);
suspicious_dns
| join kind=inner checkins on $left.SrcIpAddr == $right.SourceIP
```
