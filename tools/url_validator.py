#!/usr/bin/env python3
"""
URL Validator - Phishing URL Detection Tool

Analyzes URLs for phishing indicators using pattern matching.
No external dependencies required - uses Python standard library only.

Usage:
    python url_validator.py <url>
    python url_validator.py --file urls.txt
    python url_validator.py --help

Author: Phishing Detection Toolkit
License: MIT
"""

import re
import argparse
from urllib.parse import urlparse
import sys


class URLValidator:
    """Validates URLs for phishing indicators"""

    # Suspicious TLDs
    SUSPICIOUS_TLDS = [
        '.tk', '.ml', '.ga', '.cf', '.gq',  # Free domains
        '.top', '.xyz', '.work', '.click', '.link',
        '.zip', '.mov', '.download', '.review'
    ]

    # Lookalike domain patterns
    LOOKALIKE_PATTERNS = [
        # Brand name, Pattern, Description
        ('PayPal', [r'paypa1', r'paypa-1', r'paypai', r'paypa11'], 'PayPal'),
        ('Microsoft', [r'micros0ft', r'micro-soft', r'micr0soft'], 'Microsoft'),
        ('Google', [r'g00gle', r'go0gle', r'goog1e', r'gogle'], 'Google'),
        ('Apple', [r'app1e', r'appl3', r'app-le'], 'Apple'),
        ('Amazon', [r'amaz0n', r'amazom', r'arnazon'], 'Amazon'),
        ('Facebook', [r'faceb00k', r'face-book', r'facebo0k'], 'Facebook'),
    ]

    # Legitimate domains for comparison
    LEGITIMATE_DOMAINS = {
        'paypal.com', 'paypal-communication.com',
        'microsoft.com', 'microsoftonline.com', 'office.com',
        'google.com', 'gmail.com', 'goog1e.com',
        'apple.com', 'icloud.com',
        'amazon.com', 'amazon.co.uk',
        'facebook.com', 'fb.com'
    }

    def __init__(self, url):
        """Initialize validator with URL"""
        self.url = url
        self.indicators = []
        self.score = 0
        self.parsed = None
        self._parse_url()

    def _parse_url(self):
        """Parse and validate URL"""
        try:
            # Add scheme if missing
            if not self.url.startswith(('http://', 'https://')):
                self.url = 'http://' + self.url
            self.parsed = urlparse(self.url)
        except Exception as e:
            print(f"Error parsing URL: {e}")
            sys.exit(1)

    def validate(self):
        """Run all validation checks"""
        self.check_scheme()
        self.check_ip_address()
        self.check_suspicious_tld()
        self.check_lookalike_domain()
        self.check_subdomain_tricks()
        self.check_suspicious_patterns()
        self.check_url_length()
        self.check_authentication()

        return self.get_result()

    def check_scheme(self):
        """Check URL scheme"""
        if self.parsed.scheme == 'http':
            self.indicators.append("Unencrypted HTTP (should be HTTPS)")
            self.score += 10

    def check_ip_address(self):
        """Check if URL uses IP address instead of domain"""
        netloc = self.parsed.netloc.split(':')[0]  # Remove port if present

        # IPv4 check
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', netloc):
            self.indicators.append(f"Using IP address instead of domain: {netloc}")
            self.score += 30
            return

        # IPv6 check (simplified)
        if ':' in netloc and re.match(r'^[\da-f:]+$', netloc, re.IGNORECASE):
            self.indicators.append(f"Using IPv6 address instead of domain")
            self.score += 30

    def check_suspicious_tld(self):
        """Check for suspicious top-level domains"""
        netloc = self.parsed.netloc.lower()

        for tld in self.SUSPICIOUS_TLDS:
            if netloc.endswith(tld):
                self.indicators.append(f"Suspicious TLD: {tld}")
                self.score += 20
                return

    def check_lookalike_domain(self):
        """Check for lookalike/typosquatting domains"""
        domain = self.parsed.netloc.lower()

        for brand, patterns, description in self.LOOKALIKE_PATTERNS:
            for pattern in patterns:
                if re.search(pattern, domain):
                    # Make sure it's not the legitimate domain
                    legitimate = False
                    for legit_domain in self.LEGITIMATE_DOMAINS:
                        if legit_domain in domain:
                            legitimate = True
                            break

                    if not legitimate:
                        self.indicators.append(f"{description} lookalike domain detected")
                        self.score += 40
                        return

    def check_subdomain_tricks(self):
        """Check for subdomain tricks"""
        domain = self.parsed.netloc.lower()

        # Check for excessive subdomains
        subdomain_count = domain.count('.')
        if subdomain_count > 3:
            self.indicators.append(f"Excessive subdomains ({subdomain_count} dots)")
            self.score += 15

        # Check for legitimate domain in subdomain
        # Example: paypal.com.phishing.tk
        for legit in self.LEGITIMATE_DOMAINS:
            if legit in domain and not domain.endswith(legit):
                self.indicators.append(f"Legitimate domain '{legit}' in subdomain (trick)")
                self.score += 50
                return

    def check_suspicious_patterns(self):
        """Check for various suspicious patterns"""
        url_lower = self.url.lower()

        # Check for multiple hyphens
        if url_lower.count('-') > 3:
            self.indicators.append(f"Excessive hyphens ({url_lower.count('-')})")
            self.score += 10

        # Check for numbers mixed with letters in domain
        domain = self.parsed.netloc.lower()
        if re.search(r'[a-z]\d+[a-z]', domain) or re.search(r'\d+[a-z]+\d+', domain):
            self.indicators.append("Suspicious number/letter mix in domain")
            self.score += 15

        # Check for URL shorteners (common in phishing)
        shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd']
        for shortener in shorteners:
            if shortener in domain:
                self.indicators.append(f"URL shortener detected: {shortener}")
                self.score += 15
                break

        # Check for homoglyph/lookalike characters
        # Common substitutions: 0/O, 1/l, rn/m
        if re.search(r'[０-９]', domain):  # Full-width digits
            self.indicators.append("Homoglyph characters detected (full-width digits)")
            self.score += 35

    def check_url_length(self):
        """Check for unusually long URLs"""
        if len(self.url) > 150:
            self.indicators.append(f"Unusually long URL ({len(self.url)} characters)")
            self.score += 15

        # Check for very long domain names
        if len(self.parsed.netloc) > 50:
            self.indicators.append(f"Unusually long domain name ({len(self.parsed.netloc)} chars)")
            self.score += 10

    def check_authentication(self):
        """Check for @ symbol (authentication bypass trick)"""
        if '@' in self.parsed.netloc:
            self.indicators.append("Contains @ symbol (authentication bypass attempt)")
            self.score += 35

        # Check for unusual port numbers
        if self.parsed.port:
            common_ports = [80, 443, 8080, 8443]
            if self.parsed.port not in common_ports:
                self.indicators.append(f"Unusual port number: {self.parsed.port}")
                self.score += 10

    def get_result(self):
        """Get validation result with risk classification"""
        if self.score >= 50:
            risk_level = "HIGH - Likely Phishing"
            recommendation = "DO NOT visit this URL. It shows multiple phishing indicators."
        elif self.score >= 25:
            risk_level = "MEDIUM - Suspicious"
            recommendation = "Exercise extreme caution. Verify URL is correct before visiting."
        else:
            risk_level = "LOW - Appears Safe"
            recommendation = "URL appears legitimate, but always verify before entering credentials."

        return {
            'url': self.url,
            'score': self.score,
            'risk_level': risk_level,
            'recommendation': recommendation,
            'indicators': self.indicators,
            'parsed': {
                'scheme': self.parsed.scheme,
                'domain': self.parsed.netloc,
                'path': self.parsed.path,
                'query': self.parsed.query
            }
        }

    def print_report(self):
        """Print formatted validation report"""
        result = self.get_result()

        print("=" * 70)
        print("URL PHISHING ANALYSIS REPORT")
        print("=" * 70)
        print(f"\nURL: {result['url']}")

        print("\n" + "-" * 70)
        print("URL BREAKDOWN")
        print("-" * 70)
        print(f"Scheme:  {result['parsed']['scheme']}")
        print(f"Domain:  {result['parsed']['domain']}")
        print(f"Path:    {result['parsed']['path'] or '/'}")
        if result['parsed']['query']:
            print(f"Query:   {result['parsed']['query']}")

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


def validate_multiple_urls(file_path):
    """Validate multiple URLs from a file"""
    try:
        with open(file_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    print(f"\nAnalyzing {len(urls)} URLs from {file_path}\n")
    print("=" * 70)

    results = []
    for url in urls:
        validator = URLValidator(url)
        result = validator.validate()
        results.append(result)

        # Print summary line
        print(f"{result['risk_level']:20} | {result['url'][:45]}")

    print("=" * 70)
    print(f"\nSummary:")
    print(f"  Total URLs: {len(results)}")
    print(f"  High Risk:  {sum(1 for r in results if 'HIGH' in r['risk_level'])}")
    print(f"  Medium Risk: {sum(1 for r in results if 'MEDIUM' in r['risk_level'])}")
    print(f"  Low Risk:   {sum(1 for r in results if 'LOW' in r['risk_level'])}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Analyze URLs for phishing indicators',
        epilog='Examples:\n'
               '  python url_validator.py "http://paypa1.com/verify"\n'
               '  python url_validator.py --file urls.txt',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('url', nargs='?', help='URL to analyze')
    group.add_argument('-f', '--file', help='File containing URLs (one per line)')
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='Only show risk level (no detailed report)')

    args = parser.parse_args()

    if args.file:
        validate_multiple_urls(args.file)
    else:
        validator = URLValidator(args.url)
        result = validator.validate()

        if args.quiet:
            print(f"{result['risk_level']} (Score: {result['score']}/100)")
        else:
            validator.print_report()


if __name__ == '__main__':
    main()
