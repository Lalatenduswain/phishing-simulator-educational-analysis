#!/usr/bin/env python3
"""
Phishing Detector - All-in-One Email Security Tool

Comprehensive phishing detection combining email analysis, URL validation,
and attachment scanning. Uses Python standard library only.

Usage:
    python phishing_detector.py <email.eml>
    python phishing_detector.py --batch <directory>
    python phishing_detector.py --help

Author: Phishing Detection Toolkit
License: MIT
"""

import os
import sys
import argparse
from datetime import datetime
import json

# Import our detection modules
from email_analyzer import EmailAnalyzer
from url_validator import URLValidator
from attachment_scanner import AttachmentScanner


class PhishingDetector:
    """Comprehensive phishing detection system"""

    def __init__(self, eml_file):
        """Initialize detector with .eml file"""
        self.eml_file = eml_file
        self.results = {
            'file': eml_file,
            'timestamp': datetime.now().isoformat(),
            'email_analysis': None,
            'url_analysis': [],
            'attachment_analysis': [],
            'overall_score': 0,
            'overall_risk': '',
            'recommendation': ''
        }

    def detect(self):
        """Run complete phishing detection"""
        # 1. Analyze email
        email_analyzer = EmailAnalyzer(self.eml_file)
        email_result = email_analyzer.analyze()
        self.results['email_analysis'] = email_result

        # 2. Extract and analyze URLs (if any found in indicators)
        # URLs are already analyzed by email_analyzer
        self.results['url_analysis'] = {'note': 'URLs analyzed as part of email analysis'}

        # 3. Analyze attachments (if any)
        # Attachments are already analyzed by email_analyzer
        self.results['attachment_analysis'] = {'note': 'Attachments analyzed as part of email analysis'}

        # 4. Calculate overall score
        self.results['overall_score'] = email_result['score']

        # 5. Determine overall risk
        self._calculate_overall_risk()

        return self.results

    def _calculate_overall_risk(self):
        """Calculate overall risk assessment"""
        score = self.results['overall_score']

        if score >= 60:
            self.results['overall_risk'] = "HIGH - Phishing Attack Detected"
            self.results['recommendation'] = (
                "⚠️ CRITICAL: This email shows strong phishing indicators.\n"
                "   - DO NOT click any links\n"
                "   - DO NOT download attachments\n"
                "   - DO NOT reply to this email\n"
                "   - REPORT to your IT/Security team immediately\n"
                "   - DELETE the email after reporting"
            )
        elif score >= 30:
            self.results['overall_risk'] = "MEDIUM - Suspicious Email"
            self.results['recommendation'] = (
                "⚠️ WARNING: This email contains suspicious elements.\n"
                "   - Verify sender through alternate channel (phone, in-person)\n"
                "   - Do not click links or download attachments until verified\n"
                "   - Check with IT/Security if unsure\n"
                "   - Report if confirmed as phishing"
            )
        else:
            self.results['overall_risk'] = "LOW - Appears Legitimate"
            self.results['recommendation'] = (
                "✓ This email appears legitimate.\n"
                "   - However, always remain vigilant\n"
                "   - Verify unexpected requests through alternate channels\n"
                "   - Never provide passwords or sensitive data via email\n"
                "   - When in doubt, report to IT/Security"
            )

    def print_report(self, detailed=True):
        """Print comprehensive detection report"""
        result = self.results
        email_result = result['email_analysis']

        print("\n" + "=" * 70)
        print("COMPREHENSIVE PHISHING DETECTION REPORT")
        print("=" * 70)
        print(f"File:     {result['file']}")
        print(f"Analyzed: {datetime.fromisoformat(result['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")

        # Email metadata
        print("\n" + "=" * 70)
        print("EMAIL INFORMATION")
        print("=" * 70)
        print(f"From:    {email_result['metadata']['from']}")
        print(f"To:      {email_result['metadata']['to']}")
        print(f"Subject: {email_result['metadata']['subject']}")
        print(f"Date:    {email_result['metadata']['date']}")

        # Overall assessment
        print("\n" + "=" * 70)
        print("OVERALL RISK ASSESSMENT")
        print("=" * 70)
        print(f"Risk Score: {result['overall_score']}/100")
        print(f"Risk Level: {result['overall_risk']}")
        print(f"\n{result['recommendation']}")

        # Detailed indicators
        if detailed and email_result['indicators']:
            print("\n" + "=" * 70)
            print(f"PHISHING INDICATORS DETECTED ({len(email_result['indicators'])})")
            print("=" * 70)
            for i, indicator in enumerate(email_result['indicators'], 1):
                print(f"{i:2}. {indicator}")

        # Summary statistics
        print("\n" + "=" * 70)
        print("DETECTION SUMMARY")
        print("=" * 70)
        print(f"Total Indicators Found: {len(email_result['indicators'])}")

        # Risk breakdown
        critical_count = sum(1 for ind in email_result['indicators']
                           if any(word in ind.lower() for word in
                                  ['critical', 'dangerous', 'credential', 'authentication', 'lookalike']))
        warning_count = len(email_result['indicators']) - critical_count

        print(f"Critical Indicators:    {critical_count}")
        print(f"Warning Indicators:     {warning_count}")

        print("\n" + "=" * 70)
        print("END OF REPORT")
        print("=" * 70)

    def export_json(self, output_file=None):
        """Export results to JSON"""
        if not output_file:
            output_file = self.eml_file + '.analysis.json'

        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)

        print(f"\nResults exported to: {output_file}")


def batch_analyze(directory, export=False):
    """Analyze all .eml files in a directory"""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory")
        sys.exit(1)

    eml_files = [os.path.join(directory, f) for f in os.listdir(directory)
                 if f.endswith('.eml')]

    if not eml_files:
        print(f"No .eml files found in {directory}")
        sys.exit(0)

    print(f"\nBatch Analysis: {len(eml_files)} emails found in {directory}\n")
    print("=" * 70)

    results = []
    high_risk = []
    medium_risk = []
    low_risk = []

    for eml_file in sorted(eml_files):
        detector = PhishingDetector(eml_file)
        result = detector.detect()
        results.append(result)

        # Categorize by risk
        if 'HIGH' in result['overall_risk']:
            high_risk.append(eml_file)
            risk_symbol = '🔴'
        elif 'MEDIUM' in result['overall_risk']:
            medium_risk.append(eml_file)
            risk_symbol = '🟡'
        else:
            low_risk.append(eml_file)
            risk_symbol = '🟢'

        filename = os.path.basename(eml_file)
        print(f"{risk_symbol} {result['overall_score']:3}/100 | {filename[:50]}")

        if export:
            detector.export_json()

    # Summary
    print("=" * 70)
    print("\nBATCH ANALYSIS SUMMARY")
    print("-" * 70)
    print(f"Total Emails Analyzed: {len(results)}")
    print(f"🔴 High Risk:           {len(high_risk)}")
    print(f"🟡 Medium Risk:         {len(medium_risk)}")
    print(f"🟢 Low Risk:            {len(low_risk)}")

    if high_risk:
        print("\n⚠️ HIGH RISK EMAILS (IMMEDIATE ACTION REQUIRED):")
        for email in high_risk:
            print(f"   - {os.path.basename(email)}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Comprehensive phishing detection for email files',
        epilog='Examples:\n'
               '  python phishing_detector.py suspicious_email.eml\n'
               '  python phishing_detector.py --batch ./emails/ --export\n'
               '  python phishing_detector.py email.eml --json output.json',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('eml_file', nargs='?', help='Path to .eml file to analyze')
    parser.add_argument('-b', '--batch', metavar='DIR',
                        help='Analyze all .eml files in directory')
    parser.add_argument('-j', '--json', metavar='FILE',
                        help='Export results to JSON file')
    parser.add_argument('-e', '--export', action='store_true',
                        help='Export each analysis to JSON (batch mode)')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Quiet mode - only show risk level')
    parser.add_argument('-s', '--summary', action='store_true',
                        help='Show summary only (no detailed indicators)')

    args = parser.parse_args()

    # Batch mode
    if args.batch:
        batch_analyze(args.batch, export=args.export)
        return

    # Single file mode
    if not args.eml_file:
        parser.print_help()
        sys.exit(1)

    detector = PhishingDetector(args.eml_file)
    result = detector.detect()

    if args.quiet:
        print(f"{result['overall_risk']} (Score: {result['overall_score']}/100)")
    else:
        detailed = not args.summary
        detector.print_report(detailed=detailed)

    if args.json:
        detector.export_json(args.json)


if __name__ == '__main__':
    main()
