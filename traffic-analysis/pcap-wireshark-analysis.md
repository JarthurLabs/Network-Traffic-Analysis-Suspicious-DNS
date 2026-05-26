# PCAP and Wireshark Analysis

## Purpose

This file documents the hands-on packet review layer added to the lab. The included `.pcap` is a benign, self-generated lab capture that contains synthetic DNS queries and HTTP requests.

## Included Capture

```text
captures/benign-dns-http-lab.pcap
```

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

## What This Adds to the Lab

This moves the repository beyond static CSV evidence by adding a real packet capture artifact, filters used for analysis, tcpdump-readable output, and packet-level observations.
