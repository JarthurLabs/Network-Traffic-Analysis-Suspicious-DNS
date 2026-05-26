# Packet Evidence Summary

## Summary

The lab now includes a benign packet capture that can be opened in Wireshark or reviewed with tcpdump. The packet evidence supports the investigation narrative by showing DNS activity followed by HTTP check-ins from the same internal host.

## Filters Used

| Tool | Filter |
|---|---|
| Wireshark | `dns` |
| Wireshark | `http || tcp.port == 80` |
| Wireshark | `ip.addr == 10.10.20.17` |
| tcpdump | `port 53` |
| tcpdump | `tcp port 80` |

## Observations

1. `10.10.20.17` generated repeated DNS queries.
2. Several DNS queries returned NXDOMAIN.
3. `cdn-update.invalid` resolved to `203.0.113.90`.
4. The same host made HTTP `GET /checkin` requests.
5. The check-in request repeated at a consistent interval.

## Analyst Conclusion

The packet evidence strengthens the lab because it shows actual packet-level artifacts instead of only spreadsheet-style evidence. The conclusion remains cautious: the activity is suspicious and should trigger endpoint validation, but the PCAP alone does not prove malware.
