# tcpdump Examples

These commands are examples for a safe lab environment.

## Capture DNS Traffic

```bash
sudo tcpdump -i en0 port 53 -w dns-lab-capture.pcap
```

## Read DNS Capture

```bash
tcpdump -nn -r dns-lab-capture.pcap port 53
```

## Capture HTTP Traffic to a Specific Host

```bash
sudo tcpdump -i en0 host 203.0.113.90 and tcp port 80 -w http-checkin-lab.pcap
```

## Important Note

This repository does not include a real packet capture. These commands show how a future lab could collect safe local traffic for Wireshark analysis.
