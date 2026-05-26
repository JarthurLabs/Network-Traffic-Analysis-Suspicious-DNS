# Finding Severity Rating

## Rating: High

## Reasoning

The finding is rated **High** because:

1. The source host generated a burst of random-looking DNS queries.
2. Multiple queries returned NXDOMAIN.
3. A newly observed destination resolved after the DNS burst.
4. The same host made repeated HTTP `/checkin` requests.
5. The pattern repeated at consistent intervals.
6. The user reported browser pop-ups and slowness.

## Why Not Critical?

This is not rated Critical because there is no confirmed data exfiltration, ransomware activity, privilege escalation, or confirmed malware binary in this lab evidence.

## Why Not Medium?

The DNS pattern alone could be Medium. The rating becomes High because DNS activity correlates with repeated outbound HTTP check-ins.
