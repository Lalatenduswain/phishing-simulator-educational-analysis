# Phishing Detection Tools

Practical command-line tools for detecting phishing emails, malicious URLs, and dangerous attachments.

**Key Feature**: Basic tools require **NO external dependencies** - they use Python standard library only!

---

## 🛠️ Available Tools

### 1. Email Analyzer (`email_analyzer.py`)
Analyzes `.eml` email files for phishing indicators.

**Features:**
- Sender address validation
- Subject line analysis
- URL extraction and analysis
- Attachment scanning
- Content analysis for urgency/financial keywords
- Email header inspection
- Risk scoring (0-100)

**Usage:**
```bash
# Analyze single email
python email_analyzer.py suspicious_email.eml

# Quiet mode (risk level only)
python email_analyzer.py -q suspicious_email.eml
```

**Example Output:**
```
==================================================================
PHISHING EMAIL ANALYSIS REPORT
==================================================================

File: suspicious_email.eml
Risk Score: 75/100
Risk Level: HIGH - Likely Phishing

PHISHING INDICATORS DETECTED (8):
1. Sender uses suspicious TLD: .tk
2. Display name claims 'paypal' but domain is 'paypal-verify.tk'
3. Urgency keyword in subject: 'urgent'
4. URL uses IP address: http://192.168.1.1/verify
5. Requests credential verification
...
```

---

### 2. URL Validator (`url_validator.py`)
Validates URLs for phishing indicators using pattern matching.

**Features:**
- IP address detection
- Suspicious TLD checking
- Lookalike domain detection (paypa1.com, micros0ft.com, etc.)
- Subdomain trick detection
- URL shortener identification
- Port/authentication anomaly detection

**Usage:**
```bash
# Analyze single URL
python url_validator.py "http://paypa1.com/verify"

# Analyze multiple URLs from file
python url_validator.py --file urls.txt

# Quiet mode
python url_validator.py -q "https://suspicious-site.tk"
```

**Example:**
```bash
$ python url_validator.py "http://192.168.1.1/login"

Risk Score: 40/100
Risk Level: MEDIUM - Suspicious

PHISHING INDICATORS DETECTED:
1. Unencrypted HTTP (should be HTTPS)
2. Using IP address instead of domain: 192.168.1.1
```

---

### 3. Attachment Scanner (`attachment_scanner.py`)
Scans files for security risks.

**Features:**
- Dangerous file extension detection
- Double extension attack detection
- Filename obfuscation detection
- File size anomaly detection
- Entropy analysis (packed/encrypted files)
- RTLO (Right-To-Left Override) detection

**Usage:**
```bash
# Scan file
python attachment_scanner.py invoice.pdf.exe

# Quiet mode
python attachment_scanner.py -q document.docm
```

**Example:**
```bash
$ python attachment_scanner.py invoice.pdf.exe

Risk Score: 90/100
Risk Level: HIGH - Dangerous

SECURITY INDICATORS DETECTED:
1. Dangerous file type (Executables): .exe
2. Double extension attack: invoice.pdf.exe
```

---

### 4. Phishing Detector (`phishing_detector.py`)
**All-in-one comprehensive detection tool** that combines email analysis, URL validation, and attachment scanning.

**Features:**
- Complete email analysis
- Batch processing (analyze entire directories)
- JSON export for integration
- Summary and detailed reporting modes

**Usage:**
```bash
# Analyze single email (comprehensive)
python phishing_detector.py suspicious_email.eml

# Batch analyze directory
python phishing_detector.py --batch ./emails/

# Batch with JSON export
python phishing_detector.py --batch ./emails/ --export

# Export to specific JSON file
python phishing_detector.py email.eml --json analysis.json

# Summary only (no detailed indicators)
python phishing_detector.py email.eml --summary

# Quiet mode
python phishing_detector.py -q email.eml
```

**Batch Analysis Example:**
```bash
$ python phishing_detector.py --batch ./test_emails/

Batch Analysis: 5 emails found in ./test_emails/

==================================================================
🔴  85/100 | paypal_phishing.eml
🟡  45/100 | suspicious_invoice.eml
🟢  15/100 | legitimate_newsletter.eml
🔴  92/100 | microsoft_fake.eml
🟡  38/100 | questionable_offer.eml
==================================================================

BATCH ANALYSIS SUMMARY
----------------------------------------------------------------------
Total Emails Analyzed: 5
🔴 High Risk:           2
🟡 Medium Risk:         2
🟢 Low Risk:            1
```

---

## 📋 Requirements

### Basic Tools (Default)
**No requirements!** All basic tools use Python 3 standard library only.

```bash
# Check your Python version
python3 --version  # Should be 3.6 or higher
```

### Advanced Tools (Optional)
For advanced features (DNS validation, API integration), see `advanced/` directory.

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Lalatenduswain/phishing-simulator-educational-analysis.git
cd phishing-simulator-educational-analysis/tools
```

### 2. Make Scripts Executable (Linux/Mac)
```bash
chmod +x *.py
```

### 3. Run Your First Scan
```bash
# Create test email or use existing .eml file
python email_analyzer.py your_email.eml
```

---

## 📊 Understanding Risk Scores

| Score Range | Risk Level | Meaning | Action |
|------------|-----------|---------|--------|
| 0-29 | LOW - Appears Safe | Few or no indicators | Remain vigilant |
| 30-59 | MEDIUM - Suspicious | Multiple warning signs | Verify before interacting |
| 60-100 | HIGH - Likely Phishing | Strong phishing indicators | Do not interact, report |

**Risk Score Factors:**
- **Critical** (30-50 points): Authentication bypass, credential requests, dangerous attachments
- **High** (20-30 points): Suspicious TLDs, lookalike domains, Reply-To mismatches
- **Medium** (10-20 points): Urgency language, generic greetings, unusual patterns
- **Low** (5-10 points): Minor anomalies, spelling errors

---

## 🔍 Detection Indicators Explained

### Email Indicators
- **Sender Spoofing**: Display name doesn't match domain
- **Suspicious Domains**: Free TLDs (.tk, .ml, .ga), lookalike characters
- **Reply-To Mismatch**: Reply address differs from sender
- **Urgency Language**: "Immediate action", "account suspended", "verify now"
- **Generic Greetings**: "Dear Customer" instead of your name
- **Credential Requests**: Asking for passwords, SSN, credit cards
- **Authentication Failures**: SPF/DKIM/DMARC failures

### URL Indicators
- **IP Addresses**: Using `http://192.168.1.1` instead of domain names
- **Lookalike Domains**: `paypa1.com` (1 instead of l), `micros0ft.com` (0 instead of o)
- **Suspicious TLDs**: `.tk`, `.ml`, `.xyz`, `.top` (commonly used in phishing)
- **Subdomain Tricks**: `paypal.com.phishing-site.tk` (real domain is phishing-site.tk)
- **Long URLs**: Unusually long URLs to hide malicious destination
- **@ Symbol**: `http://legitimate.com@attacker.com` (goes to attacker.com)

### Attachment Indicators
- **Dangerous Extensions**: `.exe`, `.scr`, `.bat`, `.vbs`, `.js`
- **Double Extensions**: `invoice.pdf.exe` (appears as PDF, actually executable)
- **Macro Files**: `.docm`, `.xlsm`, `.pptm` (can contain malicious macros)
- **Filename Tricks**: Spaces, unicode characters, RTLO attacks
- **High Entropy**: Packed/encrypted files (potential malware)

---

## 💡 Usage Examples

### Example 1: Scan Email and Export Report
```bash
# Analyze email and save JSON report
python phishing_detector.py email.eml --json report.json

# The JSON file can be used for:
# - Integration with SIEM systems
# - Automated workflows
# - Data analysis and metrics
```

### Example 2: Check Multiple URLs
```bash
# Create urls.txt with one URL per line
echo "http://paypa1.com/verify" > urls.txt
echo "https://legitimate-site.com" >> urls.txt
echo "http://192.168.1.1/login" >> urls.txt

# Scan all URLs
python url_validator.py --file urls.txt
```

### Example 3: Automated Email Sorting
```bash
#!/bin/bash
# Sort emails by risk level

for email in *.eml; do
    risk=$(python phishing_detector.py -q "$email" | grep -o "HIGH\|MEDIUM\|LOW")

    case $risk in
        HIGH)
            mv "$email" ./high_risk/
            ;;
        MEDIUM)
            mv "$email" ./medium_risk/
            ;;
        LOW)
            mv "$email" ./safe/
            ;;
    esac
done
```

---

## 🔬 Advanced Tools (Optional)

Located in `advanced/` directory with additional dependencies.

### SPF/DKIM/DMARC Validator
```bash
# Requires: dnspython
pip install dnspython

python advanced/advanced_email_analyzer.py email.eml
```

### URL Reputation Checker
```bash
# Requires: API keys for VirusTotal, Google Safe Browsing
# See advanced/config.example.py

python advanced/url_reputation_checker.py "http://suspicious-url.com"
```

---

## 🧪 Testing the Tools

### Create Test Email
```python
# save as test_phishing.eml
From: PayPal Security <security@paypa1.tk>
To: victim@example.com
Subject: URGENT: Your account will be suspended!
Date: Mon, 6 Jan 2026 10:00:00 -0800

Dear Customer,

Your PayPal account shows suspicious activity. Click here immediately:
http://192.168.1.1/paypal/verify

Your account will be closed in 24 hours if you don't verify.

PayPal Security Team
```

```bash
# Test with email analyzer
python email_analyzer.py test_phishing.eml

# Expected: HIGH risk score (should detect multiple indicators)
```

---

## ⚠️ Important Notes

### These Tools Are For:
- ✅ Security awareness training
- ✅ Email security testing (authorized)
- ✅ Learning phishing detection techniques
- ✅ Building detection systems
- ✅ Incident response and analysis

### These Tools Are NOT:
- ❌ Replacements for antivirus software
- ❌ Guaranteed to detect all phishing (0% false negatives impossible)
- ❌ For creating actual phishing attacks
- ❌ Legal advice or compliance tools

### Limitations:
- **Pattern-based detection**: May miss novel/sophisticated attacks
- **No sandboxing**: Cannot detect malware behavior (use antivirus)
- **No network analysis**: Cannot detect callback/C2 communications
- **Basic tools only**: Advanced features require additional dependencies

---

## 🛡️ Best Practices

1. **Always verify suspicious emails** through alternate channels (phone, in-person)
2. **Never click links** in suspicious emails before verification
3. **Use these tools as part of** a layered security approach
4. **Keep tools updated** (check GitHub for updates)
5. **Report phishing** to IT/security team and relevant authorities
6. **Share knowledge** - train your team on phishing detection

---

## 📚 Additional Resources

- **Main Documentation**: `../docs/tools-usage-guide.md`
- **Training Materials**: `../docs/phishing-detection-training.md`
- **Security Awareness Program**: `../docs/security-awareness-program-small-business.md`
- **Example Emails**: `../examples/sample_phishing_emails/`

---

## 🤝 Contributing

Found a bug or have a suggestion? Please open an issue on GitHub!

---

## 📄 License

MIT License - See LICENSE file for details

---

## ⚡ Quick Command Reference

```bash
# Email Analysis
python email_analyzer.py <email.eml>              # Analyze email
python email_analyzer.py -q <email.eml>           # Quick scan

# URL Validation
python url_validator.py <url>                     # Check single URL
python url_validator.py --file urls.txt           # Check multiple URLs

# Attachment Scanning
python attachment_scanner.py <file>               # Scan attachment

# Comprehensive Detection
python phishing_detector.py <email.eml>           # Full analysis
python phishing_detector.py --batch <dir>         # Batch mode
python phishing_detector.py --json output.json    # Export JSON

# Get Help
python <tool_name>.py --help                      # Show all options
```

---

**Stay safe online! 🔒**

*Last Updated: January 6, 2026*
