#!/usr/bin/env python3
"""Validate the checked-in PCAP without pretending to replace TShark."""

from __future__ import annotations

import argparse
import hashlib
import struct
from pathlib import Path

EXPECTED_SHA256 = "037aa23ccfbe3430fe1b59fc78d475601d38c47c969db6fd6e7a44fe9e41fe75"
EXPECTED_PACKETS = 27


def packet_count(payload: bytes) -> int:
    if len(payload) < 24:
        raise ValueError("capture is smaller than a PCAP global header")
    magic = payload[:4]
    if magic == b"\xd4\xc3\xb2\xa1":
        endian = "<"
    elif magic == b"\xa1\xb2\xc3\xd4":
        endian = ">"
    else:
        raise ValueError(f"unsupported PCAP magic {magic.hex()}")

    offset = 24
    count = 0
    while offset < len(payload):
        if offset + 16 > len(payload):
            raise ValueError("truncated packet header")
        _, _, captured_length, original_length = struct.unpack_from(f"{endian}IIII", payload, offset)
        if captured_length > original_length:
            raise ValueError(f"packet {count + 1} captures more bytes than its original length")
        offset += 16
        if offset + captured_length > len(payload):
            raise ValueError(f"packet {count + 1} payload is truncated")
        offset += captured_length
        count += 1
    return count


def validate(path: Path) -> tuple[str, int]:
    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    count = packet_count(payload)
    if digest != EXPECTED_SHA256:
        raise ValueError(f"SHA-256 mismatch: {digest}")
    if count != EXPECTED_PACKETS:
        raise ValueError(f"expected {EXPECTED_PACKETS} packets, found {count}")
    return digest, count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pcap", type=Path, nargs="?", default=Path("captures/benign-dns-http-lab.pcap"))
    args = parser.parse_args()
    digest, count = validate(args.pcap)
    print(f"validated {args.pcap}: {count} packets, sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
