# DNS Analysis Notes

## Observed Pattern

One internal workstation generated repeated random-looking subdomain queries under a similar pattern. Several responses returned NXDOMAIN, followed by a successful resolution to a newly observed destination.

## Why This Matters

High-volume or repeated random-looking DNS queries can indicate unwanted software, beaconing, or domain generation behavior. DNS alone does not prove compromise, so it should be correlated with endpoint and HTTP evidence.
