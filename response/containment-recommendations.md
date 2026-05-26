# Containment Recommendations

## Immediate Actions

1. Isolate workstation `10.10.20.17`.
2. Block observed suspicious domains and destination IP pending validation.
3. Preserve DNS, proxy, and endpoint logs.
4. Review browser extensions, startup items, and recently installed software.
5. Run endpoint security scan.
6. Validate whether the destination appears on any approved vendor list.

## Follow-Up Actions

- Add DNS anomaly detection.
- Add DNS-to-HTTP correlation rule.
- Improve asset ownership records.
- Review user awareness around browser pop-ups.
- Confirm whether sensitive files were accessed.
- Add safe packet capture lab in a future version.

## Severity

High, pending endpoint validation.
