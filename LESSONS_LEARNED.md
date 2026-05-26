# Lessons Learned

- DNS anomalies are usually weak signals until correlated with another data source.
- Packet filters matter. Starting broad was noisy; filtering by `dns`, `http`, and the source host made the investigation clearer.
- A repeated `/checkin` path is more suspicious when it follows unusual DNS behavior.
- False positives are not a weakness in the report. They show better analyst thinking.
- A PCAP makes the project feel more hands-on, but endpoint telemetry is still needed to confirm root cause.
