# Capture provenance

The file **benign-dns-http-lab.pcap** is a documentation-safe, self-generated lab capture. It was first committed to this repository on May 26, 2026 in commit 69e7fb7.

The packet payload uses reserved documentation ranges and names, including 203.0.113.0/24, 198.51.100.0/24, .test, .example, and .invalid. It is not a capture from a production network and it does not prove malware.

The original packet-generation command and tool version were not preserved. That gap matters, so this repository does not pretend the capture is independently regenerable. What can be reproduced is its integrity check and its analysis:

    SHA-256: 037aa23ccfbe3430fe1b59fc78d475601d38c47c969db6fd6e7a44fe9e41fe75
    Packets: 27
    Link type: Ethernet

Run **python scripts/validate_capture.py** to verify the file and **bash scripts/analyze_pcap.sh** on a machine with TShark to recreate the packet tables.

One limitation is easy to miss: the broader synthetic CSV narrative includes one DNS event that is not present in this 27-packet capture. The TShark output describes only the PCAP, while the CSV files remain scenario data.
