# Network Traffic Analysis Lab: Suspicious DNS Activity

## Overview

This is a lab-based network traffic analysis project. It uses synthetic DNS/HTTP data and a benign self-generated `.pcap` to investigate traffic from one workstation.

The activity looked suspicious, but not enough to claim malware. The point of the lab is to show the analyst workflow: filter the traffic, look for patterns, compare against possible benign explanations, and decide what to check next.

All hosts, domains, IP addresses, timestamps, and packet data are synthetic or documentation-safe.

---

## What stood out

The first thing that stood out was a burst of DNS queries from `10.10.20.17`. Several queries had short random-looking subdomains and returned NXDOMAIN. By itself, that was only a weak signal.

The severity increased when the same host later made repeated HTTP requests to `/checkin` on a newly observed destination. DNS anomalies alone were not enough to confirm compromise, but DNS plus repeated HTTP check-ins made the activity worth escalating for endpoint validation.

---

## Evidence used

| Evidence | Location |
|---|---|
| Benign lab PCAP | `captures/benign-dns-http-lab.pcap` |
| tcpdump DNS output | `tool-output/tcpdump-dns-output.txt` |
| tcpdump HTTP output | `tool-output/tcpdump-http-output.txt` |
| DNS event data | `data/dns-events.csv` |
| HTTP connection data | `data/http-connections.csv` |
| Timeline | `data/investigation-timeline.csv` |
| False positive analysis | `traffic-analysis/false-positive-analysis.md` |
| Detection examples | `detection-logic/` |
| Packet analysis notes | `traffic-analysis/pcap-wireshark-analysis.md` |

---

## Filters used

```text
dns
```

```text
http || tcp.port == 80
```

```text
ip.addr == 10.10.20.17
```

The initial packet output was noisy, so the review was narrowed to DNS first, then HTTP traffic from the same workstation.

---

## Packet evidence

### DNS filter view

![Wireshark DNS Filter](./screenshots/wireshark-dns-filter.svg)

### HTTP filter view

![Wireshark HTTP Filter](./screenshots/wireshark-http-filter.svg)

### Packet observations

![Packet Observations](./screenshots/packet-observations.svg)

---

## Why this was suspicious

| Signal | Why it mattered |
|---|---|
| Similar random-looking subdomains | Could indicate automated domain generation or unwanted software behavior |
| Multiple NXDOMAIN responses | Failed generated domains can be a weak signal |
| Newly observed destination | The destination was not part of known normal traffic in the lab |
| Repeated `/checkin` requests | Repetition at intervals made the traffic more concerning |
| Same source host | DNS and HTTP activity tied back to one workstation |

---

## False positives considered

This could still be benign. Software updates, browser prefetching, security agent telemetry, misconfigured applications, or ad/tracker traffic can all create unusual DNS and HTTP patterns.

Without endpoint telemetry, process information, browser history, or EDR data, the investigation cannot confirm execution or malware.

---

## Current conclusion

**Disposition:** suspicious network activity requiring endpoint validation.

**Severity:** High for triage purposes, not because compromise is confirmed, but because DNS anomalies correlated with repeated outbound HTTP check-ins.

---

## Next steps

1. Isolate or closely monitor `10.10.20.17`.
2. Check endpoint telemetry for the process that made the connections.
3. Review browser extensions, startup items, and recently installed software.
4. Block observed indicators if they are not tied to approved software.
5. Tune SIEM logic to alert on DNS bursts followed by HTTP check-ins.
