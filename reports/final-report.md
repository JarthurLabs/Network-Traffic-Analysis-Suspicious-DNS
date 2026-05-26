# Final Analyst Report

## Summary

A workstation generated suspicious DNS activity followed by repeated HTTP check-ins to a newly observed destination. The activity should be treated as High severity suspicious network activity pending endpoint validation.

## Evidence Reviewed

- DNS events with query length, subdomain length, TLD, response type, and analyst notes
- HTTP connection events
- DNS-to-HTTP timeline
- Suspicious DNS criteria
- False positive analysis
- IOC list
- Detection query examples
- Recommendation matrix

## Why This Is Suspicious

The activity combines several analyst signals:

1. Repeated random-looking subdomains.
2. Similar query lengths and structure.
3. Multiple NXDOMAIN responses.
4. Newly observed destination.
5. HTTP `/checkin` requests after DNS activity.
6. Repeated HTTP interval pattern.
7. User-reported browser pop-ups and slowness.

## Severity Rating

High.

The DNS behavior alone may be Medium. The severity increases to High because it correlates with repeated outbound HTTP check-ins.

## False Positives Considered

Possible benign explanations include software updates, browser prefetching, security tool telemetry, misconfigured internal applications, and ad/tracker traffic. These should be validated before confirming compromise.

## Recommended Actions

1. Isolate the workstation.
2. Block observed indicators pending validation.
3. Review endpoint telemetry.
4. Validate whether the destination is associated with approved software.
5. Add detection for NXDOMAIN bursts followed by HTTP check-ins.
6. Preserve evidence for follow-up investigation.
