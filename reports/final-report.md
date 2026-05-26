# Final Analyst Report

## Summary

This lab reviewed suspicious DNS and HTTP activity from one workstation, `10.10.20.17`. The evidence included synthetic DNS/HTTP records, a benign lab PCAP, tcpdump output, and Wireshark-style filter views.

The activity was suspicious but not conclusive. The strongest signal was not the DNS traffic by itself. It was the combination of random-looking DNS queries, NXDOMAIN responses, a newly observed destination, and repeated HTTP `/checkin` requests.

## Initial observations

At first this could have been normal noise. Browsers, update clients, and security tools can generate strange-looking DNS. After filtering down to the single host, the repeated pattern became easier to see.

## Evidence reviewed

- DNS queries and NXDOMAIN responses
- HTTP requests to `/checkin`
- tcpdump output
- Wireshark-style DNS and HTTP views
- Packet observations
- False positive analysis
- SIEM query examples

## What I could not confirm

- Whether a malicious process executed.
- Whether data was accessed or exfiltrated.
- Whether the destination was actually malicious.
- Whether this was caused by malware, adware, misconfiguration, or benign software.

## Analyst conclusion

Treat as suspicious and validate on the endpoint. The network evidence is enough to justify follow-up, but not enough to make a final malware determination.

## Recommended next steps

1. Identify the process responsible for the HTTP traffic.
2. Review EDR or endpoint logs.
3. Check browser extensions and startup items.
4. Compare the destination against approved software/vendor lists.
5. Block the indicators if no benign owner is found.
