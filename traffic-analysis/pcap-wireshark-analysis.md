# PCAP and Wireshark Analysis

## Purpose

This file documents the hands-on packet review layer added to the lab. The included `.pcap` is a benign, self-generated lab capture that contains synthetic DNS queries and HTTP requests.

## Included capture

```text
captures/benign-dns-http-lab.pcap
SHA-256 037aa23ccfbe3430fe1b59fc78d475601d38c47c969db6fd6e7a44fe9e41fe75
27 packets, Ethernet link type
```

The provenance record is in `captures/PROVENANCE.md`. The original generation command was not retained; the capture is integrity-verifiable and analysis-reproducible, but not independently regenerable.

## Wireshark Filters Used

```text
dns
```

```text
http || tcp.port == 80
```

```text
ip.addr == 10.10.20.17
```

## Packet Observations

| Observation | Evidence | What It Proves |
|---|---|---|
| Repeated DNS queries | Multiple A record queries from `10.10.20.17` | One host is the source of the suspicious pattern |
| NXDOMAIN responses | Several random-looking subdomains return NXDOMAIN | The domains do not resolve and may be generated or invalid |
| New destination resolved | `cdn-update.invalid` resolves to `203.0.113.90` | A new external destination appears after the DNS burst |
| HTTP check-in path | `GET /checkin HTTP/1.1` | DNS activity is followed by outbound web traffic |
| Repeated interval | `/checkin` appears multiple times | Repetition increases suspicion and suggests automated behavior |

## What the Packet Evidence Proves

The packet evidence proves that the same internal host generated suspicious DNS activity and then made outbound HTTP requests to a newly observed destination. It does **not** prove malware by itself. Endpoint telemetry would still be required to confirm root cause.

## Repeatable analysis

Run `bash scripts/analyze_pcap.sh` with TShark installed. Continuous integration runs the same command and uploads the DNS and HTTP tables as a workflow artifact.

The SVG files under `screenshots/` and `docs/images/` are explanatory diagrams, not Wireshark screenshots. Only the PCAP and tool-generated text should be treated as packet evidence.

## What this adds to the lab

This moves the repository beyond static CSV evidence by keeping a real lab capture artifact, its hash, filters, generated TShark tables, stored tcpdump text, and packet-level observations. It still does not identify the endpoint process or prove compromise.
