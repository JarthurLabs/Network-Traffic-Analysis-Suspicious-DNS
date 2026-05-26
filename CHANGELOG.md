# Changelog

## v4.0 - Hands-On PCAP and Wireshark Evidence Layer

### Added

- Added benign self-generated packet capture: `captures/benign-dns-http-lab.pcap`
- Added Wireshark-style DNS filter screenshot: `screenshots/wireshark-dns-filter.svg`
- Added Wireshark-style HTTP filter screenshot: `screenshots/wireshark-http-filter.svg`
- Added packet observations screenshot: `screenshots/packet-observations.svg`
- Added tcpdump DNS output: `tool-output/tcpdump-dns-output.txt`
- Added tcpdump HTTP output: `tool-output/tcpdump-http-output.txt`
- Added packet review notes: `traffic-analysis/pcap-wireshark-analysis.md`
- Added packet evidence summary: `reports/packet-evidence-summary.md`
- Added packet observations data: `data/packet-observations.csv`

### Changed

- Updated README to include inline packet evidence screenshots
- Reframed the lab as including actual packet-level evidence
- Clarified that the PCAP is benign and self-generated, not malware traffic

## v3.0 - Analyst Depth and Detection Logic Upgrade

### Added

- Clear lab framing in `README.md`
- Severity rating with Low / Medium / High reasoning
- DNS-to-HTTP timeline
- Suspicious DNS criteria: query length, frequency, subdomain pattern, response type, newly observed domain, and TLD context
- False positive analysis
- Splunk SPL examples
- Microsoft Sentinel KQL examples
- Google SecOps / Chronicle UDM-style examples
- Pseudo-Sigma rule
- tcpdump command examples
- New inline README screenshots for suspicious DNS criteria, severity rating, timeline, and false positives

### Changed

- Strengthened the analyst conclusion
- Made the limitations clearer
- Reframed the repository as a lab instead of implying production packet evidence
- Improved detection logic and technical credibility

## v2.0 - Evidence-of-Work Upgrade

- Added structured evidence folders
- Added screenshots
- Added IOC documentation
- Added recommendation matrix
- Added final report

## v1.0 - Initial Project

- Initial suspicious DNS traffic analysis project using synthetic data
