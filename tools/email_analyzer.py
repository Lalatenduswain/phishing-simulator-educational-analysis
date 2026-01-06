#!/usr/bin/env python3
"""
Email Analyzer - Basic Phishing Detection Tool

Analyzes .eml files for phishing indicators using Python standard library only.
No external dependencies required.

Usage:
    python email_analyzer.py <email_file.eml>
    python email_analyzer.py --help

Author: Phishing Detection Toolkit
License: MIT
"""

import email
import re
from email import policy
from email.parser import BytesParser
from urllib.parse import urlparse
import sys
import argparse
from datetime import datetime


class EmailAnalyzer:
    """Analyzes email files for phishing indicators"""

    # Suspicious TLDs commonly used in phishing
    SUSPICIOUS_TLDS = [
        '.tk', '.ml', '.ga', '.cf', '.gq',  # Free domains
        '.top', '.xyz', '.work', '.click', '.link',  # Cheap domains
        '.zip', '.mov', '.exe', '.scr'  # Suspicious extensions as TLDs
    ]

    # Legitimate email providers
    LEGITIMATE_PROVIDERS = [
        'gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com',
        'protonmail.com', 'icloud.com', 'aol.com'
    ]

    # Common phishing keywords
    URGENCY_KEYWORDS = [
        'urgent', 'immediate action', 'suspend', 'verify', 'confirm',
        'urgent action required', 'act now', 'limited time',
        'expires', 'unauthorized', 'suspicious activity'
    ]

    FINANCIAL_KEYWORDS = [
        'bank account', 'credit card', 'ssn', 'social security',
        'wire transfer', 'payment', 'refund', 'tax', 'irs'
    ]

    def __init__(self, eml_file):
        """Initialize analyzer with an .eml file"""
        self.eml_file = eml_file
        self.message = None
        self.indicators = []
        self.score = 0
        self._load_email()

    def _load_email(self):
        """Load and parse the .eml file"""
        try:
            with open(self.eml_file, 'rb') as f:
                self.message = BytesParser(policy=policy.default).parse(f)
        except Exception as e:
            print(f"Error loading email: {e}")
            sys.exit(1)

    def analyze(self):
        """Run all analysis checks"""
        self.check_sender()
        self.check_reply_to()
        self.check_subject()
        self.check_urls()
        self.check_attachments()
        self.check_content()
        self.check_headers()

        return self.get_result()

    def check_sender(self):
        """Analyze sender address for suspicious patterns"""
        from_header = self.message.get('From', '')

        # Extract email address
        email_match = re.search(r'<(.+?)>', from_header)
        sender_email = email_match.group(1) if email_match else from_header

        # Extract display name
        display_name = re.sub(r'<.+?>', '', from_header).strip(' "')

        # Check for domain issues
        if '@' in sender_email:
            domain = sender_email.split('@')[1].lower()

            # Check for lookalike characters
            if re.search(r'[0-9]', domain.replace('.com', '').replace('.net', '')):
                self.indicators.append("Sender domain contains suspicious numbers")
                self.score += 15

            # Check for suspicious TLDs
            for tld in self.SUSPICIOUS_TLDS:
                if domain.endswith(tld):
                    self.indicators.append(f"Sender uses suspicious TLD: {tld}")
                    self.score += 20
                    break

            # Check for subdomain tricks
            subdomain_count = domain.count('.')
            if subdomain_count > 2:
                self.indicators.append(f"Excessive subdomains ({subdomain_count})")
                self.score += 15

        # Check display name mismatch
        if display_name and '@' in sender_email:
            domain = sender_email.split('@')[1].lower()
            display_lower = display_name.lower()

            # Check if display name claims to be a company but domain doesn't match
            known_companies = ['paypal', 'microsoft', 'google', 'apple', 'amazon', 'facebook']
            for company in known_companies:
                if company in display_lower and company not in domain:
                    self.indicators.append(f"Display name claims '{company}' but domain is '{domain}'")
                    self.score += 35

    def check_reply_to(self):
        """Check if Reply-To differs from From"""
        from_header = self.message.get('From', '')
        reply_to = self.message.get('Reply-To', '')

        if reply_to and reply_to != from_header:
            self.indicators.append("Reply-To address differs from From address")
            self.score += 25

    def check_subject(self):
        """Analyze subject line for phishing indicators"""
        subject = self.message.get('Subject', '').lower()

        # Check for urgency
        for keyword in self.URGENCY_KEYWORDS:
            if keyword in subject:
                self.indicators.append(f"Urgency keyword in subject: '{keyword}'")
                self.score += 10
                break

        # Check for all caps
        if subject.isupper() and len(subject) > 10:
            self.indicators.append("Subject line is all caps (shouting)")
            self.score += 10

        # Check for excessive punctuation
        if subject.count('!') > 1 or subject.count('?') > 1:
            self.indicators.append("Excessive punctuation in subject")
            self.score += 5

    def check_urls(self):
        """Extract and analyze URLs in email body"""
        body = self._get_body()
        if not body:
            return

        # Find all URLs
        url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        urls = re.findall(url_pattern, body, re.IGNORECASE)

        for url in urls:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()

            # Check for IP address instead of domain
            if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain):
                self.indicators.append(f"URL uses IP address: {url[:50]}")
                self.score += 30
                continue

            # Check for suspicious TLDs
            for tld in self.SUSPICIOUS_TLDS:
                if domain.endswith(tld):
                    self.indicators.append(f"URL with suspicious TLD: {url[:50]}")
                    self.score += 20
                    break

            # Check for lookalike domains
            lookalike_patterns = [
                (r'paypa1', 'PayPal lookalike (1 instead of l)'),
                (r'micros0ft', 'Microsoft lookalike (0 instead of o)'),
                (r'g00gle', 'Google lookalike (0 instead of o)'),
                (r'app1e', 'Apple lookalike (1 instead of l)'),
            ]

            for pattern, description in lookalike_patterns:
                if re.search(pattern, domain, re.IGNORECASE):
                    self.indicators.append(f"{description}: {url[:50]}")
                    self.score += 40

            # Check for @ symbol (authentication bypass attempt)
            if '@' in parsed.netloc:
                self.indicators.append(f"URL contains @ symbol: {url[:50]}")
                self.score += 35

            # Check for unusually long URL
            if len(url) > 150:
                self.indicators.append(f"Unusually long URL ({len(url)} chars)")
                self.score += 15

    def check_attachments(self):
        """Analyze email attachments"""
        dangerous_extensions = [
            '.exe', '.scr', '.bat', '.cmd', '.com', '.pif',
            '.vbs', '.js', '.jar', '.msi', '.dll',
            '.docm', '.xlsm', '.pptm'  # Macro-enabled Office files
        ]

        for part in self.message.walk():
            filename = part.get_filename()
            if filename:
                filename_lower = filename.lower()

                # Check for dangerous extensions
                for ext in dangerous_extensions:
                    if filename_lower.endswith(ext):
                        self.indicators.append(f"Dangerous attachment: {filename}")
                        self.score += 30
                        break

                # Check for double extensions
                if filename_lower.count('.') > 1:
                    # Check if it looks like .pdf.exe, .doc.exe, etc.
                    parts = filename_lower.split('.')
                    if len(parts) >= 3 and parts[-1] in ['exe', 'scr', 'bat', 'cmd']:
                        self.indicators.append(f"Double extension attack: {filename}")
                        self.score += 40

                # Check for spaces before extension (obfuscation)
                if re.search(r'\s+\.[a-z]{2,4}$', filename_lower):
                    self.indicators.append(f"Suspicious spacing in filename: {filename}")
                    self.score += 20

    def check_content(self):
        """Analyze email body content"""
        body = self._get_body()
        if not body:
            return

        body_lower = body.lower()

        # Check for urgency keywords
        urgency_count = sum(1 for keyword in self.URGENCY_KEYWORDS if keyword in body_lower)
        if urgency_count >= 2:
            self.indicators.append(f"Multiple urgency keywords ({urgency_count})")
            self.score += 15

        # Check for financial keywords
        financial_count = sum(1 for keyword in self.FINANCIAL_KEYWORDS if keyword in body_lower)
        if financial_count >= 2:
            self.indicators.append(f"Multiple financial keywords ({financial_count})")
            self.score += 15

        # Check for generic greetings
        generic_greetings = ['dear customer', 'dear user', 'dear member', 'dear sir/madam']
        for greeting in generic_greetings:
            if greeting in body_lower:
                self.indicators.append(f"Generic greeting: '{greeting}'")
                self.score += 10
                break

        # Check for credential requests
        if re.search(r'(verify|confirm|update).{0,20}(password|account|credentials)', body_lower):
            self.indicators.append("Requests credential verification")
            self.score += 30

        # Check for spelling errors (common indicators)
        common_misspellings = {
            'recieve': 'receive',
            'sercurity': 'security',
            'importnat': 'important',
            'verifiy': 'verify'
        }
        for misspelling, correct in common_misspellings.items():
            if misspelling in body_lower:
                self.indicators.append(f"Spelling error: '{misspelling}' (should be '{correct}')")
                self.score += 15

    def check_headers(self):
        """Analyze email headers for suspicious patterns"""
        # Check for missing headers
        important_headers = ['From', 'To', 'Date', 'Subject']
        for header in important_headers:
            if not self.message.get(header):
                self.indicators.append(f"Missing important header: {header}")
                self.score += 10

        # Check Authentication-Results (if present)
        auth_results = self.message.get('Authentication-Results', '')
        if 'fail' in auth_results.lower():
            self.indicators.append("Authentication check failed (SPF/DKIM/DMARC)")
            self.score += 40

    def _get_body(self):
        """Extract email body text"""
        body = ""

        if self.message.is_multipart():
            for part in self.message.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain' or content_type == 'text/html':
                    try:
                        payload = part.get_payload(decode=True)
                        if payload:
                            body += payload.decode('utf-8', errors='ignore')
                    except:
                        pass
        else:
            try:
                payload = self.message.get_payload(decode=True)
                if payload:
                    body = payload.decode('utf-8', errors='ignore')
            except:
                pass

        return body

    def get_result(self):
        """Get analysis result with risk classification"""
        if self.score >= 60:
            risk_level = "HIGH - Likely Phishing"
            recommendation = "DO NOT interact with this email. Report it immediately."
        elif self.score >= 30:
            risk_level = "MEDIUM - Suspicious"
            recommendation = "Exercise caution. Verify sender through alternate channel."
        else:
            risk_level = "LOW - Appears Safe"
            recommendation = "Email appears legitimate, but always remain vigilant."

        return {
            'file': self.eml_file,
            'score': self.score,
            'risk_level': risk_level,
            'recommendation': recommendation,
            'indicators': self.indicators,
            'metadata': {
                'from': self.message.get('From', ''),
                'to': self.message.get('To', ''),
                'subject': self.message.get('Subject', ''),
                'date': self.message.get('Date', '')
            }
        }

    def print_report(self):
        """Print formatted analysis report"""
        result = self.get_result()

        print("=" * 70)
        print("PHISHING EMAIL ANALYSIS REPORT")
        print("=" * 70)
        print(f"\nFile: {result['file']}")
        print(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("\n" + "-" * 70)
        print("EMAIL METADATA")
        print("-" * 70)
        print(f"From:    {result['metadata']['from']}")
        print(f"To:      {result['metadata']['to']}")
        print(f"Subject: {result['metadata']['subject']}")
        print(f"Date:    {result['metadata']['date']}")

        print("\n" + "-" * 70)
        print("RISK ASSESSMENT")
        print("-" * 70)
        print(f"Risk Score: {result['score']}/100")
        print(f"Risk Level: {result['risk_level']}")
        print(f"\nRecommendation: {result['recommendation']}")

        if result['indicators']:
            print("\n" + "-" * 70)
            print(f"PHISHING INDICATORS DETECTED ({len(result['indicators'])})")
            print("-" * 70)
            for i, indicator in enumerate(result['indicators'], 1):
                print(f"{i}. {indicator}")
        else:
            print("\n" + "-" * 70)
            print("No phishing indicators detected.")
            print("-" * 70)

        print("\n" + "=" * 70)
        print("END OF REPORT")
        print("=" * 70)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Analyze .eml files for phishing indicators',
        epilog='Example: python email_analyzer.py suspicious_email.eml'
    )
    parser.add_argument('eml_file', help='Path to .eml file to analyze')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Only show risk level (no detailed report)')

    args = parser.parse_args()

    analyzer = EmailAnalyzer(args.eml_file)
    result = analyzer.analyze()

    if args.quiet:
        print(f"{result['risk_level']} (Score: {result['score']}/100)")
    else:
        analyzer.print_report()


if __name__ == '__main__':
    main()
