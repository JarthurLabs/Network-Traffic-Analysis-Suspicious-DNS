# DNS Analysis Notes

## Observed Pattern

One internal workstation, `10.10.20.17`, generated multiple DNS queries with similar random-looking subdomains under the same base domain pattern.

## Analyst Criteria

| Criteria | Observation | Why It Matters |
|---|---|---|
| Query length | Queries were similar length, around 18-21 characters | Automation often produces consistent patterns |
| Subdomain shape | Short alphanumeric labels like `a8d3k2` | Random-looking labels can indicate generated domains |
| Frequency | Multiple queries occurred within roughly one minute | Bursts can indicate automated behavior |
| Response type | Multiple NXDOMAIN responses | Generated or invalid domains often fail resolution |
| Suspicious TLD | `.test` and `.invalid` are not normal business destinations in this lab | Unusual TLDs require validation |
| Newly observed destination | `203.0.113.90` appeared after failed DNS queries | New destination after suspicious DNS raises concern |

## Analyst Interpretation

The DNS activity is suspicious because it combines multiple weak signals: repeated pattern, random-looking subdomains, short timing interval, NXDOMAIN responses, and a newly observed destination. No single item proves compromise by itself. The combination makes it worth investigating.
