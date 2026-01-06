# Phishing Detection - Quick Reference Guide

## 1-Minute Phishing Check

When you receive a suspicious email, check these indicators in order:

### CRITICAL CHECKS (Stop if any fail)

```
┌─────────────────────────────────────────────────────────────┐
│ ⚠️ CRITICAL: Stop and report if you find ANY of these:     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ ❌ Email asks for passwords, SSN, or credit card info      │
│ ❌ SPF/DKIM/DMARC all show "FAIL"                          │
│ ❌ "From" domain doesn't match company's real domain       │
│ ❌ Unexpected urgent requests for money/wire transfer      │
│ ❌ Links to IP addresses (http://192.168.x.x/)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### QUICK VISUAL SCAN (5 seconds)

```
👁️ LOOK FOR:
   ⚠️ Spelling errors in sender domain (micros0ft.com)
   ⚠️ Urgency language ("URGENT", "24 hours", "suspended")
   ⚠️ Generic greeting ("Dear Customer" vs "Dear John")
   ⚠️ Poor grammar or spelling mistakes
   ⚠️ Mismatched branding/logos
```

### HOVER TEST (10 seconds)

```
🖱️ HOVER OVER LINKS (don't click!):

   Display text: "Click here to verify your account"
   Actual URL:   http://verify-paypal.tk/secure
                     ↑
                  Suspicious!

   ✅ SAFE: URL matches expected domain
   ❌ UNSAFE: URL goes to unexpected/unknown domain
```

### SENDER VERIFICATION (20 seconds)

```
📧 CHECK THE SENDER:

From: Microsoft Security <security@microsoft.com>
       ↑ Display name        ↑ Actual email address
      (can be fake)           (harder to fake)

⚠️ Red flags:
   • Display name doesn't match email domain
   • Lookalike characters (paypa1.com, micros0ft.com)
   • Free email services (gmail, yahoo) for business
   • Extra words in domain (paypal-secure.com)
   • Different country TLD (.ru, .tk, .ml)
```

---

## The SPAM Framework

**S - Sender Analysis**
- [ ] Sender email matches display name
- [ ] Domain is legitimate (no typos)
- [ ] Expected sender for this type of message

**P - Purpose & Pressure**
- [ ] No artificial urgency or threats
- [ ] Request makes sense for this sender
- [ ] No suspicious timing (weekend, midnight)

**A - Attachments & Links**
- [ ] No unexpected attachments
- [ ] Links match expected domains (hover test)
- [ ] No QR codes from unexpected senders

**M - Message Quality**
- [ ] Proper grammar and spelling
- [ ] Personalized (uses your name)
- [ ] Professional formatting

---

## Common Phishing Red Flags

### Urgency Red Flags
```
❌ "Your account will be closed in 24 hours"
❌ "Immediate action required"
❌ "Respond within 1 hour or face penalties"
❌ "Suspicious activity detected - verify NOW"
❌ "Limited time offer - expires today"
```

### Request Red Flags
```
❌ "Verify your password"
❌ "Update your payment information immediately"
❌ "Confirm your SSN/credit card"
❌ "Download this urgent security update"
❌ "Process this wire transfer ASAP"
```

### Technical Red Flags
```
❌ Email from CEO but sent from @gmail.com
❌ Link says paypal.com but goes to paypa1.com
❌ Attachment named "invoice.pdf.exe"
❌ QR code in unexpected email
❌ Reply-To address different from From address
```

---

## URL Safety Checklist

### Safe URL Pattern
```
✅ https://www.paypal.com/security/verify
   │    │   └─ Legitimate domain
   │    └───── Secure connection (HTTPS)
   └────────── Correct protocol
```

### Dangerous URL Patterns
```
❌ http://192.168.1.1/login
   └─ Using IP address instead of domain

❌ https://paypal.com.verify-secure.tk
   └─ Real domain is "verify-secure.tk", not paypal.com

❌ https://paypa1.com
   └─ Number "1" instead of letter "l"

❌ https://microsoft.co
   └─ Wrong TLD (.co instead of .com)

❌ http://example.com:8080
   └─ Unusual port number
```

---

## Email Header Quick Check

### How to View Headers
- **Gmail:** Click "⋮" → Show original
- **Outlook:** File → Properties → Internet headers
- **Apple Mail:** View → Message → All Headers

### What to Look For
```
Authentication-Results: mx.google.com;
    spf=pass smtp.mailfrom=paypal.com;    ✅ GOOD
    dkim=pass header.i=@paypal.com;       ✅ GOOD
    dmarc=pass (p=REJECT)                 ✅ GOOD

vs.

Authentication-Results: mx.google.com;
    spf=fail smtp.mailfrom=unknown.com;   ❌ BAD
    dkim=fail header.i=@paypal.com;       ❌ BAD
    dmarc=fail (p=REJECT)                 ❌ BAD
```

---

## QR Code Safety

### Before Scanning ANY QR Code:

```
❓ ASK YOURSELF:
   • Was I expecting this QR code?
   • Is it from a trusted, verified source?
   • Does the context make sense?

⚠️ NEVER SCAN:
   • QR codes from unexpected emails
   • QR codes on random flyers/stickers
   • QR codes claiming urgent action needed
   • QR codes for payment without verification

✅ SAFE TO SCAN:
   • QR codes on verified business cards
   • Restaurant menus (verify it's official)
   • Event tickets purchased directly
   • After verbal confirmation from sender
```

### After Scanning:

```
1. Check the URL BEFORE tapping "Open"
2. Verify it matches expected domain
3. Don't enter sensitive info without verification
```

---

## Attachment Safety Rules

### Safe Attachment Checklist

```
BEFORE OPENING ANY ATTACHMENT:

[ ] Expected this attachment
[ ] Sender verified through separate channel
[ ] File extension matches type (.pdf is PDF, not .exe)
[ ] No double extensions (.pdf.exe)
[ ] Scanned by antivirus
[ ] Not macro-enabled unless absolutely necessary

DANGEROUS EXTENSIONS:
❌ .exe, .scr, .bat, .cmd, .com
❌ .js, .vbs, .wsf
❌ .pdf.exe, .doc.exe (double extensions)
⚠️ .docm, .xlsm, .pptm (macro-enabled Office docs)
⚠️ .zip, .rar (can contain malware)
```

---

## What to Do If You Suspect Phishing

### Immediate Actions

```
1. DON'T CLICK any links or download attachments
2. DON'T REPLY to the email
3. DON'T FORWARD to others (spreads phishing)
4. DO REPORT using "Report Phishing" button
5. DO DELETE the email after reporting
```

### If You Already Clicked

```
⚠️ DAMAGE CONTROL:

If you clicked a link:
1. Don't enter any information on the site
2. Close the browser tab/window
3. Clear browser cache and cookies
4. Report to IT/Security immediately
5. Run antivirus scan

If you entered credentials:
1. Change password IMMEDIATELY
2. Enable two-factor authentication (2FA)
3. Report to IT/Security immediately
4. Monitor account for suspicious activity
5. Check other accounts with same password

If you downloaded/opened attachment:
1. Disconnect from network (unplug ethernet/disable WiFi)
2. Report to IT/Security immediately
3. Run full antivirus scan
4. Follow IT team instructions
5. DO NOT reconnect until cleared
```

---

## Verification Methods

### How to Verify Suspicious Requests

```
✅ GOOD VERIFICATION:
   • Call the sender using a known number
     (NOT a number from the suspicious email)
   • Visit website by typing URL manually
     (NOT by clicking email link)
   • Walk to colleague's desk to confirm in person
   • Check internal directory for contact info
   • Use company's official communication channels

❌ BAD VERIFICATION:
   • Replying to the suspicious email
   • Calling number provided in email
   • Clicking "Contact Us" link in email
   • Trusting caller ID (can be spoofed)
   • Assuming it's real because it looks professional
```

---

## Real-World Examples

### Example 1: PayPal Phishing

```
From: PayPal <service@paypal.com>
Subject: Your Account Has Been Limited

Dear Customer,

We have limited your account due to unusual activity.
To restore access, please verify your information:

[Verify Now] → http://paypal-verify.tk/secure

⚠️ RED FLAGS:
   • Generic greeting ("Dear Customer")
   • Creates urgency ("limited")
   • Suspicious URL (.tk free domain)
   • Misspelled domain (paypal-verify.tk)

✅ REAL PAYPAL:
   • Uses your name
   • Links to paypal.com or e.paypal.com
   • No urgency threats
   • Has account details visible
```

### Example 2: Microsoft Phishing

```
From: Microsoft Security Team <security-alert@micros0ft.com>
Subject: URGENT: Verify Your Account

Your Microsoft 365 account will be suspended in 24 hours.
Click here to verify: http://192.168.1.1/verify

⚠️ RED FLAGS:
   • "URGENT" creates panic
   • Typo: micros0ft (zero instead of 'o')
   • Links to IP address
   • Suspension threat
   • HTTP instead of HTTPS

✅ REAL MICROSOFT:
   • From @microsoft.com
   • Links to microsoft.com
   • No immediate suspension threats
   • Uses HTTPS
```

### Example 3: CEO Fraud (BEC)

```
From: John Smith (CEO) <john.smith@gmail.com>
Subject: Urgent Wire Transfer

I'm in a meeting with a client and need you to process
a wire transfer immediately for $50,000.

Details:
Account: 123456789
Routing: 987654321
Amount: $50,000

Please confirm ASAP.

⚠️ RED FLAGS:
   • CEO using personal Gmail (not company email)
   • Unusual urgency
   • Financial request via email
   • No standard approval process
   • "In meeting" (can't call to verify)

✅ WHAT TO DO:
   • Call CEO directly at known number
   • Follow company wire transfer policies
   • Get written approval through proper channels
   • Verify with multiple people
```

---

## Browser Security Indicators

### Check Browser Address Bar

```
✅ SECURE CONNECTION:
   🔒 https://paypal.com
   └─ Green padlock = encrypted connection

   Company Name (EV Certificate)
   └─ Shows verified company name

⚠️ INSECURE CONNECTION:
   ⓘ http://paypal.com
   └─ No encryption (data visible to attackers)

❌ DANGEROUS:
   🚫 Not Secure | http://paypal-verify.tk
   └─ Browser warning = high risk
```

---

## Mobile-Specific Tips

### Extra Risks on Mobile

```
⚠️ MOBILE VULNERABILITIES:
   • Can't hover over links to preview
   • Smaller screen = harder to spot details
   • Push notifications create urgency
   • Easier to click wrong button
   • Less visible URL bar

📱 MOBILE SAFETY TIPS:
   1. Long-press links to see URL preview
   2. Don't click links in text messages
   3. Manually type URLs in browser
   4. Use official apps instead of mobile web
   5. Enable 2FA on all accounts
   6. Keep phone OS updated
```

---

## Training Tips for Teams

### Build a Security Culture

```
✅ DO:
   • Celebrate people who report phishing
   • Share phishing examples (anonymously)
   • Regular training (quarterly)
   • Make reporting easy (one-click button)
   • Focus on education, not punishment

❌ DON'T:
   • Shame people who click phishing
   • Make it a "gotcha" game
   • Send simulations during stressful times
   • Use sensitive topics inappropriately
   • Skip follow-up training
```

---

## Emergency Contacts

### Who to Contact

```
SUSPICIOUS EMAIL:
→ IT Help Desk
→ Security Team
→ Your Manager (for requests involving them)

CLICKED PHISHING LINK:
→ IT Security Team (IMMEDIATELY)
→ Password reset team
→ Your manager

ENTERED CREDENTIALS:
→ IT Security Team (IMMEDIATELY - minutes matter)
→ Password reset team
→ Bank/financial institutions (if relevant)

DOWNLOADED MALWARE:
→ Disconnect from network FIRST
→ IT Security Team (IMMEDIATELY)
→ Follow incident response procedures
```

---

## Monthly Security Checklist

```
PERSONAL SECURITY HYGIENE:

[ ] Update all passwords (use password manager)
[ ] Enable 2FA on important accounts
[ ] Review recent account activity
[ ] Update software and OS
[ ] Run antivirus scan
[ ] Review email filters and rules
[ ] Check browser extensions (remove unnecessary)
[ ] Backup important data
[ ] Review privacy settings
[ ] Delete old/unused accounts

WORKPLACE SECURITY:

[ ] Report any suspicious emails received
[ ] Complete required security training
[ ] Review data access permissions
[ ] Update work passwords
[ ] Clear browser cache/cookies
[ ] Lock computer when away from desk
[ ] Shred sensitive documents
[ ] Verify emergency contact procedures
```

---

## Resources

### Quick Tools

**URL Checkers:**
- VirusTotal: https://www.virustotal.com/
- URLScan.io: https://urlscan.io/
- Google Safe Browsing: https://transparencyreport.google.com/safe-browsing/

**Email Header Analyzers:**
- MXToolbox: https://mxtoolbox.com/
- Google Admin Toolbox: https://toolbox.googleapps.com/

**Report Phishing:**
- FTC: reportphishing@apwg.org
- Anti-Phishing Working Group: https://apwg.org/

---

## Remember: When in Doubt...

```
┌──────────────────────────────────────────────┐
│                                              │
│  🛑 STOP                                     │
│     Don't click, don't reply, don't panic   │
│                                              │
│  🤔 THINK                                    │
│     Does this make sense? Was I expecting   │
│     this? Are there red flags?              │
│                                              │
│  ✅ VERIFY                                   │
│     Contact sender through separate         │
│     channel. Check with IT/Security.        │
│                                              │
│  📢 REPORT                                   │
│     Report suspicious emails. Better safe   │
│     than sorry!                              │
│                                              │
└──────────────────────────────────────────────┘
```

**If something feels wrong, it probably is. Trust your instincts and verify!**

---

*Print this guide and keep it near your workspace for quick reference.*

*Last updated: January 6, 2026*
