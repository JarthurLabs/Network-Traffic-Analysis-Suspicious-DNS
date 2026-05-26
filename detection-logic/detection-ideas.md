# Detection Ideas

## Detection Goals

1. Identify DNS bursts with repeated NXDOMAIN responses.
2. Identify random-looking subdomains with similar length and structure.
3. Correlate suspicious DNS activity with outbound HTTP check-ins.
4. Reduce false positives by comparing against known vendors and normal endpoint behavior.

## Included Query Examples

- `splunk-spl-examples.md`
- `microsoft-sentinel-kql-examples.md`
- `chronicle-udm-examples.md`
- `sigma-style-rule.yml`
- `tcpdump-examples.md`
