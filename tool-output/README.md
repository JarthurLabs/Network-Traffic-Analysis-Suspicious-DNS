# Tool Output

This folder contains command-line review output from the included benign lab PCAP.

## Files

| File | Purpose |
|---|---|
| `tcpdump-dns-output.txt` | DNS-focused packet review output |
| `tcpdump-http-output.txt` | HTTP-focused packet review output |

## Reproduce Locally

```bash
tcpdump -nn -r captures/benign-dns-http-lab.pcap port 53
```

```bash
tcpdump -nn -A -r captures/benign-dns-http-lab.pcap tcp port 80
```

If using Wireshark, open the PCAP and apply:

```text
dns
```

or:

```text
http || tcp.port == 80
```
