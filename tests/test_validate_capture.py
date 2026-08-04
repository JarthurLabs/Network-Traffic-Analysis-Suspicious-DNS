import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_capture import EXPECTED_PACKETS, EXPECTED_SHA256, validate  # noqa: E402


class CaptureValidationTests(unittest.TestCase):
    def test_capture_hash_and_packet_count(self):
        digest, count = validate(ROOT / "captures" / "benign-dns-http-lab.pcap")
        self.assertEqual(EXPECTED_SHA256, digest)
        self.assertEqual(EXPECTED_PACKETS, count)

    def test_hash_manifest_matches_validator(self):
        manifest = (ROOT / "captures" / "SHA256SUMS").read_text(encoding="utf-8").split()
        self.assertEqual(EXPECTED_SHA256, manifest[0])
        self.assertEqual("benign-dns-http-lab.pcap", manifest[1])


if __name__ == "__main__":
    unittest.main()
