#!/usr/bin/env python3
"""
Attachment Scanner - Email Attachment Security Tool

Scans email attachments for dangerous file types and suspicious patterns.
No external dependencies required - uses Python standard library only.

Usage:
    python attachment_scanner.py <file_path>
    python attachment_scanner.py --help

Author: Phishing Detection Toolkit
License: MIT
"""

import os
import sys
import argparse
import math
import re
from collections import Counter


class AttachmentScanner:
    """Scans files for security risks"""

    # Dangerous file extensions
    DANGEROUS_EXTENSIONS = {
        'Executables': ['.exe', '.scr', '.bat', '.cmd', '.com', '.pif', '.msi'],
        'Scripts': ['.vbs', '.js', '.jse', '.wsf', '.wsh', '.ps1'],
        'Office Macros': ['.docm', '.xlsm', '.pptm', '.dotm', '.xltm', '.potm'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],  # Can contain malware
        'Java': ['.jar', '.class'],
        'Shortcuts': ['.lnk', '.url'],
        'DLL': ['.dll', '.sys', '.drv']
    }

    # Suspicious file extensions
    SUSPICIOUS_EXTENSIONS = [
        '.pdf', '.doc', '.xls', '.ppt', '.rtf',  # Can contain exploits
        '.html', '.htm', '.svg',  # Can contain scripts
    ]

    def __init__(self, file_path):
        """Initialize scanner with file path"""
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        self.indicators = []
        self.score = 0

        if not os.path.exists(file_path):
            print(f"Error: File not found: {file_path}")
            sys.exit(1)

    def scan(self):
        """Run all security scans"""
        self.check_extension()
        self.check_double_extension()
        self.check_filename_tricks()
        self.check_file_size()
        self.check_entropy()

        return self.get_result()

    def check_extension(self):
        """Check file extension for dangerous types"""
        filename_lower = self.filename.lower()

        # Check dangerous extensions
        for category, extensions in self.DANGEROUS_EXTENSIONS.items():
            for ext in extensions:
                if filename_lower.endswith(ext):
                    self.indicators.append(f"Dangerous file type ({category}): {ext}")
                    self.score += 40
                    return

        # Check suspicious extensions
        for ext in self.SUSPICIOUS_EXTENSIONS:
            if filename_lower.endswith(ext):
                self.indicators.append(f"Potentially risky file type: {ext}")
                self.score += 10
                break

    def check_double_extension(self):
        """Check for double extension tricks"""
        filename_lower = self.filename.lower()

        # Count extensions
        parts = filename_lower.split('.')
        if len(parts) >= 3:
            # Check if looks like document.pdf.exe
            dangerous_final = ['.exe', '.scr', '.bat', '.cmd', '.com', '.vbs', '.js']
            for ext in dangerous_final:
                if filename_lower.endswith(ext):
                    self.indicators.append(f"Double extension attack: {self.filename}")
                    self.score += 50
                    return

            # Multiple extensions even if not dangerous
            self.indicators.append(f"Multiple extensions ({len(parts)-1})")
            self.score += 15

    def check_filename_tricks(self):
        """Check for filename obfuscation tricks"""
        filename_lower = self.filename.lower()

        # Check for spaces before extension
        if re.search(r'\s+\.[a-z]{2,4}$', self.filename):
            self.indicators.append("Suspicious spaces before extension")
            self.score += 20

        # Check for very long filename (obfuscation)
        if len(self.filename) > 100:
            self.indicators.append(f"Unusually long filename ({len(self.filename)} chars)")
            self.score += 15

        # Check for hidden unicode characters
        if len(self.filename.encode('utf-8')) != len(self.filename):
            self.indicators.append("Contains non-ASCII characters")
            self.score += 10

        # Check for right-to-left override (RTLO) attack
        if '\u202e' in self.filename:
            self.indicators.append("RTLO character detected (filename spoofing)")
            self.score += 50

    def check_file_size(self):
        """Check file size for anomalies"""
        size = os.path.getsize(self.file_path)

        # Very small executables are suspicious
        if size < 1024 and any(self.filename.lower().endswith(ext)
                              for exts in self.DANGEROUS_EXTENSIONS.values()
                              for ext in exts):
            self.indicators.append(f"Suspiciously small executable ({size} bytes)")
            self.score += 15

        # Very large files might be zip bombs or similar
        if size > 100 * 1024 * 1024:  # 100 MB
            self.indicators.append(f"Very large file ({size // (1024*1024)} MB)")
            self.score += 10

    def check_entropy(self):
        """Calculate file entropy (high entropy = encrypted/packed)"""
        try:
            with open(self.file_path, 'rb') as f:
                # Read first 8KB for entropy check
                data = f.read(8192)
                if not data:
                    return

                # Calculate Shannon entropy
                counter = Counter(data)
                length = len(data)
                entropy = -sum((count/length) * math.log2(count/length)
                              for count in counter.values())

                # High entropy suggests encryption or packing
                if entropy > 7.5:
                    self.indicators.append(f"High file entropy ({entropy:.2f}) - possibly packed/encrypted")
                    self.score += 20

        except Exception as e:
            # Can't read file
            pass

    def get_result(self):
        """Get scan result with risk classification"""
        if self.score >= 50:
            risk_level = "HIGH - Dangerous"
            recommendation = "DO NOT open this file. It shows multiple security risks."
        elif self.score >= 25:
            risk_level = "MEDIUM - Suspicious"
            recommendation = "Exercise extreme caution. Scan with antivirus before opening."
        else:
            risk_level = "LOW - Appears Safe"
            recommendation = "File appears safe, but always scan attachments with antivirus."

        file_size = os.path.getsize(self.file_path)

        return {
            'file': self.file_path,
            'filename': self.filename,
            'score': self.score,
            'risk_level': risk_level,
            'recommendation': recommendation,
            'indicators': self.indicators,
            'metadata': {
                'size': file_size,
                'size_human': self._human_readable_size(file_size),
                'extension': os.path.splitext(self.filename)[1]
            }
        }

    def _human_readable_size(self, size):
        """Convert bytes to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"

    def print_report(self):
        """Print formatted scan report"""
        result = self.get_result()

        print("=" * 70)
        print("ATTACHMENT SECURITY SCAN REPORT")
        print("=" * 70)
        print(f"\nFile: {result['filename']}")
        print(f"Path: {result['file']}")

        print("\n" + "-" * 70)
        print("FILE METADATA")
        print("-" * 70)
        print(f"Extension: {result['metadata']['extension']}")
        print(f"Size:      {result['metadata']['size_human']}")

        print("\n" + "-" * 70)
        print("RISK ASSESSMENT")
        print("-" * 70)
        print(f"Risk Score: {result['score']}/100")
        print(f"Risk Level: {result['risk_level']}")
        print(f"\nRecommendation: {result['recommendation']}")

        if result['indicators']:
            print("\n" + "-" * 70)
            print(f"SECURITY INDICATORS DETECTED ({len(result['indicators'])})")
            print("-" * 70)
            for i, indicator in enumerate(result['indicators'], 1):
                print(f"{i}. {indicator}")
        else:
            print("\n" + "-" * 70)
            print("No security indicators detected.")
            print("-" * 70)

        print("\n" + "=" * 70)
        print("END OF REPORT")
        print("=" * 70)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Scan email attachments for security risks',
        epilog='Example: python attachment_scanner.py invoice.pdf.exe'
    )
    parser.add_argument('file_path', help='Path to file to scan')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Only show risk level (no detailed report)')

    args = parser.parse_args()

    scanner = AttachmentScanner(args.file_path)
    result = scanner.scan()

    if args.quiet:
        print(f"{result['risk_level']} (Score: {result['score']}/100)")
    else:
        scanner.print_report()


if __name__ == '__main__':
    main()
