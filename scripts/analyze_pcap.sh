#!/usr/bin/env bash
set -euo pipefail

pcap="${1:-captures/benign-dns-http-lab.pcap}"
output_dir="${2:-tool-output/generated}"

if ! command -v tshark >/dev/null 2>&1; then
  echo "TShark is required. Install Wireshark/TShark, then run this command again." >&2
  exit 127
fi

(
  cd captures
  sha256sum --check SHA256SUMS
)
mkdir -p "$output_dir"

tshark -r "$pcap" -Y dns -T fields \
  -E header=y -E separator=$'\t' -E quote=d -E occurrence=f \
  -e frame.number -e frame.time_epoch -e ip.src -e ip.dst \
  -e dns.qry.name -e dns.flags.rcode \
  > "$output_dir/tshark-dns.tsv"

tshark -r "$pcap" -Y http.request -T fields \
  -E header=y -E separator=$'\t' -E quote=d -E occurrence=f \
  -e frame.number -e frame.time_epoch -e ip.src -e ip.dst \
  -e http.request.method -e http.host -e http.request.uri \
  > "$output_dir/tshark-http.tsv"

echo "Wrote TShark output to $output_dir"
