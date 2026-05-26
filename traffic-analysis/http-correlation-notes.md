# HTTP Correlation Notes

## Observed Pattern

After the DNS burst, the same workstation made repeated outbound HTTP requests to `203.0.113.90` using the `/checkin` path.

## Why This Matters

The HTTP activity increases the severity because it appears after the DNS anomaly and repeats at a consistent interval. Repeated check-ins can be associated with command-and-control behavior, unwanted software, or automated telemetry.

## Cautious Conclusion

This should be treated as suspicious pending endpoint validation. The analyst should not claim malware is confirmed from DNS and HTTP metadata alone.
