# Phishing Email Simulator: Technical Analysis & Educational Guide

## Disclaimer

**IMPORTANT: This document is for educational and defensive security purposes only.**

This analysis is intended for:
- Security awareness training
- Understanding defensive countermeasures
- Academic research and learning
- Authorized security testing and penetration testing

**DO NOT** use this information for:
- Unauthorized access attempts
- Actual phishing attacks
- Credential theft
- Any malicious activities

Unauthorized phishing and email spoofing are illegal in most jurisdictions. Always obtain proper authorization before conducting security testing.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Technical Architecture Deep Dive](#2-technical-architecture-deep-dive)
3. [Email Template Engineering](#3-email-template-engineering)
4. [Phishing Attack Vectors Explained](#4-phishing-attack-vectors-explained)
5. [AI-Powered Conversational Phishing](#5-ai-powered-conversational-phishing)
6. [Interactive Simulation Features](#6-interactive-simulation-features)
7. [Security Awareness Lessons](#7-security-awareness-lessons)
8. [Privacy and Compliance](#8-privacy-and-compliance)
9. [Building Similar Systems (Educational)](#9-building-similar-systems-educational)
10. [Detection and Defense](#10-detection-and-defense)
11. [Practical Exercises](#11-practical-exercises)
12. [Resources and References](#12-resources-and-references)

---

## 1. Executive Summary

### What is CanIPhish?

CanIPhish is a commercial phishing simulation platform designed for security awareness training. It provides organizations with tools to educate employees about phishing threats through realistic, controlled simulations.

### Key Findings from Technical Analysis

**Scale and Scope:**
- 80+ phishing email templates
- 70+ language support for international organizations
- Multiple threat vectors: credential harvesting, attachments, QR codes
- AI-powered conversational phishing capabilities

**Technical Architecture:**
- Frontend: jQuery + Bootstrap with HTML5 iframe rendering
- Template Storage: AWS S3 CDN for scalable delivery
- Analytics: Google Tag Manager integration
- Personalization: Dynamic variable injection system

**Educational Value:**
- Difficulty-rated templates (Easy/Moderate/Hard) for progressive training
- Safe sandbox environment for practicing detection
- Realistic attack simulations including multi-stage campaigns
- Conversational AI that mimics real attacker follow-up patterns

### Why Study Phishing Simulators?

Understanding how phishing simulators work provides valuable insights into:
1. **Attack methodologies** - How real attackers craft convincing phishing emails
2. **Detection techniques** - What indicators to look for in suspicious emails
3. **Security awareness** - How to design effective training programs
4. **Technical defenses** - What technical controls prevent phishing attacks

---

## 2. Technical Architecture Deep Dive

### Frontend Technology Stack

#### jQuery + Bootstrap Framework

CanIPhish uses a traditional web stack optimized for reliability and browser compatibility:

```javascript
// Simplified example of template selection UI
$(document).ready(function() {
    // Load available templates
    $.ajax({
        url: '/api/templates',
        success: function(templates) {
            templates.forEach(function(template) {
                $('#template-list').append(
                    `<div class="template-card" data-id="${template.id}">
                        <h3>${template.name}</h3>
                        <span class="difficulty ${template.difficulty}">${template.difficulty}</span>
                    </div>`
                );
            });
        }
    });

    // Template preview on click
    $('.template-card').on('click', function() {
        var templateId = $(this).data('id');
        loadTemplatePreview(templateId);
    });
});
```

**Why this stack?**
- **jQuery**: Cross-browser compatibility, easy DOM manipulation
- **Bootstrap**: Responsive design, consistent UI components
- **Stability**: Proven technologies reduce bugs in training platforms

### HTML5 Iframe Rendering

Email previews are rendered in iframes for security isolation:

```html
<!-- Email preview container -->
<div class="email-preview-container">
    <iframe
        id="email-preview"
        sandbox="allow-same-origin allow-popups"
        srcdoc="<!-- Email HTML injected here -->"
    ></iframe>
</div>
```

**Security benefits:**
- Isolates untrusted HTML content
- Prevents JavaScript execution in preview
- Limits interaction with parent page
- Protects against XSS in email templates

### Variable Injection System

The personalization engine replaces placeholders with actual data:

```javascript
// Variable injection example
function personalizeEmail(templateHtml, userData) {
    // Define variable mappings
    const variables = {
        '{{RECIPIENT_NAME}}': userData.name,
        '{{RECIPIENT_EMAIL}}': userData.email,
        '{{COMPANY_NAME}}': userData.company,
        '{{JOB_TITLE}}': userData.jobTitle,
        '{{SUPERVISOR_NAME}}': userData.supervisor,
        '{{CURRENT_DATE}}': new Date().toLocaleDateString()
    };

    // Replace all variables
    let personalizedHtml = templateHtml;
    for (let [placeholder, value] of Object.entries(variables)) {
        personalizedHtml = personalizedHtml.replace(
            new RegExp(placeholder, 'g'),
            escapeHtml(value)
        );
    }

    return personalizedHtml;
}

// Escape HTML to prevent injection
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
```

### AWS S3 CDN Architecture

Email templates are hosted on AWS S3 for scalability and global distribution:

```
Architecture:
┌─────────────┐
│   Client    │
└──────┬──────┘
       │ Request template
       ▼
┌─────────────┐
│ Web Server  │
└──────┬──────┘
       │ Fetch template URL
       ▼
┌─────────────┐
│   AWS S3    │ ← Template storage
│  (CDN URL)  │
└─────────────┘
```

**Benefits:**
- Low latency through edge caching
- High availability and redundancy
- Cost-effective storage
- Easy template updates and versioning

**Example S3 URL structure:**
```
https://s3.amazonaws.com/caniphish-templates/
  ├── paypal-credential-harvest/
  │   ├── en/template.html
  │   ├── es/template.html
  │   └── fr/template.html
  ├── microsoft-account-verify/
  │   └── ...
  └── ...
```

### Google Tag Manager Analytics

GTM tracks user interactions for training effectiveness:

```html
<!-- GTM Implementation -->
<script>
  (function(w,d,s,l,i){
    w[l]=w[l]||[];
    w[l].push({'gtm.start': new Date().getTime()});
    var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';
    j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;
    f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-WXS3HF3');
</script>
```

**Metrics collected:**
- Email open rates
- Link click-through rates
- Form submission attempts
- Time spent viewing email
- Phishing success/failure rates

---

## 3. Email Template Engineering

### Template Structure

Phishing email templates follow a standardized structure:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{EMAIL_SUBJECT}}</title>
    <style>
        /* Inline CSS for email client compatibility */
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            color: #333333;
        }
        .header {
            background-color: #0078d4; /* Microsoft blue */
            padding: 20px;
            text-align: center;
        }
        .logo {
            max-width: 200px;
        }
        .content {
            padding: 30px;
            background-color: #ffffff;
        }
        .urgent {
            color: #d13438;
            font-weight: bold;
        }
        .button {
            background-color: #0078d4;
            color: #ffffff;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 4px;
            display: inline-block;
            margin: 20px 0;
        }
        .footer {
            font-size: 12px;
            color: #666666;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header">
        <img src="{{LOGO_URL}}" alt="{{COMPANY_NAME}}" class="logo">
    </div>

    <div class="content">
        <p>Dear {{RECIPIENT_NAME}},</p>

        <p class="urgent">⚠️ URGENT: Your account requires immediate verification</p>

        <p>
            We have detected unusual activity on your {{SERVICE_NAME}} account
            ({{RECIPIENT_EMAIL}}). To ensure the security of your account, please
            verify your identity within 24 hours.
        </p>

        <p>
            Failure to verify may result in temporary account suspension.
        </p>

        <a href="{{PHISHING_URL}}" class="button">Verify My Account Now</a>

        <p>
            This verification is required due to our enhanced security policies.
        </p>

        <p>
            Thank you for your immediate attention,<br>
            {{COMPANY_NAME}} Security Team
        </p>
    </div>

    <div class="footer">
        <p>
            © {{CURRENT_YEAR}} {{COMPANY_NAME}}. All rights reserved.<br>
            {{COMPANY_ADDRESS}}
        </p>
        <p>
            <small>
                This is an automated message. Please do not reply to this email.
            </small>
        </p>
    </div>
</body>
</html>
```

### Variable Placeholder System

**Standard variables used across templates:**

| Placeholder | Description | Example Value |
|------------|-------------|---------------|
| `{{RECIPIENT_NAME}}` | Target's full name | "John Smith" |
| `{{RECIPIENT_EMAIL}}` | Target's email address | "john.smith@company.com" |
| `{{COMPANY_NAME}}` | Target's organization | "Acme Corporation" |
| `{{JOB_TITLE}}` | Target's position | "Senior Accountant" |
| `{{SUPERVISOR_NAME}}` | Manager's name | "Jane Doe" |
| `{{CURRENT_DATE}}` | Today's date | "January 6, 2026" |
| `{{PHISHING_URL}}` | Tracking/landing page URL | "https://track.simulator.com/xyz" |
| `{{SERVICE_NAME}}` | Impersonated service | "Microsoft 365" |

### Internationalization Approach

Templates are localized for 70+ languages:

```javascript
// Language selection example
const templates = {
    'paypal-verify': {
        'en': {
            subject: 'Action Required: Verify Your PayPal Account',
            urgencyText: 'Immediate action required',
            buttonText: 'Verify Now'
        },
        'es': {
            subject: 'Acción Requerida: Verifique Su Cuenta de PayPal',
            urgencyText: 'Se requiere acción inmediata',
            buttonText: 'Verificar Ahora'
        },
        'fr': {
            subject: 'Action Requise: Vérifiez Votre Compte PayPal',
            urgencyText: 'Action immédiate requise',
            buttonText: 'Vérifier Maintenant'
        }
        // ... 67 more languages
    }
};
```

### Difficulty Rating Methodology

Templates are rated based on detectability:

**Easy (Beginner Level):**
- Obvious spelling/grammar errors
- Generic greetings ("Dear Customer")
- Suspicious sender addresses
- Poor logo quality
- Unencrypted HTTP links

**Moderate (Intermediate Level):**
- Correct branding and logos
- Personalized greetings
- Plausible sender addresses
- HTTPS links
- Subtle urgency tactics

**Hard (Advanced Level):**
- Perfect branding replication
- Full personalization (name, company, role)
- Legitimate-looking sender domains
- Context-aware content (recent company news)
- Multi-stage attacks
- Conversational follow-ups

### Brand Impersonation Examples

**Microsoft/Office 365:**
```
From: Microsoft Security Team <security@microsoft-verify.com>
Subject: [Action Required] Unusual Sign-in Activity Detected
```

**PayPal:**
```
From: PayPal Service <service@paypal-security.com>
Subject: Your Account Has Been Limited
```

**Banking:**
```
From: Chase Security Alert <alerts@chase-secure.com>
Subject: Suspicious Transaction Detected - Verify Now
```

**Cloud Storage:**
```
From: Dropbox Team <noreply@dropbox-share.com>
Subject: Document Shared: Q4_Financial_Report.pdf
```

---

## 4. Phishing Attack Vectors Explained

### Credential Harvesting

The most common phishing attack type focuses on stealing login credentials.

**Attack Flow:**
```
1. Email with urgent message
   ↓
2. Click on "Verify Account" link
   ↓
3. Redirects to fake login page
   ↓
4. User enters credentials
   ↓
5. Credentials captured by attacker
   ↓
6. Redirect to real site (user unaware)
```

**Example Landing Page Code:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Microsoft Account Login</title>
    <!-- Styles mimicking Microsoft login -->
</head>
<body>
    <form id="phishing-form" action="/capture" method="POST">
        <img src="microsoft-logo.png" alt="Microsoft">
        <h2>Sign in to your account</h2>

        <input type="email" name="email" placeholder="Email address" required>
        <input type="password" name="password" placeholder="Password" required>

        <button type="submit">Sign in</button>
    </form>

    <script>
    // In real attack: capture and send credentials
    // In simulation: log attempt and educate user
    document.getElementById('phishing-form').addEventListener('submit', function(e) {
        e.preventDefault();
        // Log phishing attempt
        logTrainingEvent('credential_entry');
        // Show educational message
        showPhishingAlert();
    });
    </script>
</body>
</html>
```

### Attachment-Based Attacks

Malicious attachments disguised as legitimate documents.

**Common attachment types:**
- `.pdf` - Fake invoices, receipts
- `.docx` / `.xlsx` - Fake contracts, reports
- `.zip` - "Encrypted" files requiring password
- `.html` - Phishing pages downloaded to device

**Example email with attachment:**
```
Subject: Invoice #2026-0106 - Payment Due

Dear {{RECIPIENT_NAME}},

Please find attached invoice #2026-0106 for services rendered.
Payment is due within 5 business days.

Attachment: Invoice_2026_0106.pdf (actually .pdf.exe)
```

**Detection indicators:**
- Unexpected attachments
- Double file extensions (.pdf.exe)
- Password-protected files from unknown senders
- Macros in Office documents

### QR Code Phishing (Quishing)

A rapidly growing threat vector exploiting QR code trust.

**Why QR codes are effective for phishing:**
- URLs are not visible before scanning
- Many security tools don't scan QR codes in images
- Mobile devices may have fewer security controls
- Users trust QR codes in professional contexts

**Advanced evasion techniques (2026):**

1. **Split QR Codes:**
```
┌─────────────────┐     ┌─────────────────┐
│  Image 1        │  +  │  Image 2        │
│  (appears       │     │  (appears       │
│   innocent)     │     │   innocent)     │
└─────────────────┘     └─────────────────┘
         ↓                       ↓
         └───────────┬───────────┘
                     ↓
            ┌────────────────┐
            │ Functional QR  │
            │ when rendered  │
            │ together       │
            └────────────────┘
```

2. **Nested QR Codes:**
```
  Outer code: Legitimate URL (for quick scanners)
       ┌──────────────────┐
       │ █▀▀▀▀▀▀▀▀▀▀▀▀▀█ │
       │ █ Inner: Malicious URL
       │ █ █▀▀▀▀▀▀▀█ █ │
       │ █ █ ████ █ █ │
       │ █ █▄▄▄▄▄▄▄█ █ │
       │ █▄▄▄▄▄▄▄▄▄▄▄▄▄█ │
       └──────────────────┘
```

3. **Non-Standard Colors:**
```html
<!-- Standard QR: Black on white -->
<img src="qr-standard.png">

<!-- Evasion: Blue on beige (harder to detect) -->
<svg viewBox="0 0 100 100">
    <rect fill="#F5F5DC" width="100" height="100"/>
    <!-- QR pattern in #003366 -->
</svg>
```

**Real-world quishing statistics (2026):**
- 427% increase in QR code phishing (Aug-Sep 2025)
- 500,000+ phishing emails with embedded QR codes in PDFs (3-month period)
- Primary targets: Microsoft credentials, financial services

### Sender Spoofing and Lookalike Domains

**Spoofing techniques:**

1. **Display Name Spoofing:**
```
From: PayPal <attacker@malicious.com>
     ↑ Looks legitimate in email client
```

2. **Lookalike Domains:**
```
Legitimate:  paypal.com
Lookalike:   paypa1.com (1 instead of l)
             paypal-secure.com (added word)
             paypal.co (different TLD)
             paypa-l.com (added hyphen)
             рaypal.com (Cyrillic 'р' looks like 'p')
```

3. **Subdomain Tricks:**
```
paypal.com.attacker.com
         ↑ Actual domain is attacker.com
```

### Social Engineering in Subject Lines

**Psychological triggers used:**

| Trigger | Example Subject Line | Effectiveness |
|---------|---------------------|---------------|
| Urgency | "URGENT: Account will be closed in 24 hours" | High |
| Fear | "Security Alert: Suspicious login detected" | High |
| Authority | "CEO Request: Review attached document" | Very High |
| Curiosity | "You have 1 unread message" | Medium |
| Greed | "Claim your $500 reward" | Medium |
| Social Proof | "5 colleagues have already completed this" | High |

---

## 5. AI-Powered Conversational Phishing

### How Conversational Phishing Works

Modern phishing isn't just one email - it's an ongoing conversation that builds trust.

**Traditional vs. Conversational Phishing:**

```
TRADITIONAL:
┌────────────────┐
│ Single email   │
│ with phishing  │
│ link           │
└────────────────┘
     ↓
  Success or failure

CONVERSATIONAL:
┌────────────────┐
│ Initial email  │
│ (seemingly     │
│  legitimate)   │
└────────────────┘
     ↓
┌────────────────┐
│ User responds  │
│ with question  │
└────────────────┘
     ↓
┌────────────────┐
│ AI generates   │
│ contextual     │
│ reply          │
└────────────────┘
     ↓
┌────────────────┐
│ Trust built,   │
│ phishing link  │
│ in later email │
└────────────────┘
```

### CanIPhish AI Implementation

**Response timing patterns:**
- **Testing mode**: 1 minute delay (quick validation)
- **Campaign mode**: 10-40 minute delay (realistic human response time)

**Why timing matters:**
- Instant responses seem automated
- Realistic delays build trust
- Mimics actual work schedule patterns

**Victim response types:**

```javascript
const responseTypes = {
    SHORT: {
        pattern: "Brief, compliant response",
        example: "OK, I'll check it out.",
        nextAction: "Send phishing link"
    },
    DOUBTFUL: {
        pattern: "Questioning, skeptical",
        example: "Is this really from IT? I didn't request this.",
        nextAction: "Provide reassurance, authority signals"
    },
    REFUSAL: {
        pattern: "Direct rejection",
        example: "I don't think this is legitimate.",
        nextAction: "Mark as training success, send educational content"
    },
    AGREEABLE: {
        pattern: "Fully trusting, eager to help",
        example: "Sure! What do you need me to do?",
        nextAction: "Escalate request (credentials, wire transfer)"
    }
};
```

### AI Response Generation

**Context-aware follow-up example:**

```
User initial reply: "I'm not sure why I need to verify my account.
                     I just logged in this morning."

AI-generated response:
"Hi {{RECIPIENT_NAME}},

Thanks for getting back to me. I understand your confusion. We recently
upgraded our authentication system over the weekend, and all accounts
created before 2024 need a one-time verification.

This is just a security precaution after the recent industry-wide
security incidents you may have heard about.

The verification only takes 30 seconds:
[Verification Link]

Let me know if you have any issues!

Best,
IT Security Team"
```

**AI elements:**
- Acknowledges user's concern
- Provides plausible explanation
- References real-world context (security incidents)
- Maintains friendly, helpful tone
- Includes call-to-action

---

## 6. Interactive Simulation Features

### Virtual Inbox Functionality

The simulator recreates a realistic email environment:

```
┌─────────────────────────────────────────────────┐
│ 📧 Inbox                                        │
├─────────────────────────────────────────────────┤
│ ☐ Microsoft Security    Action Required: Ve... │
│ ☐ PayPal               Your account has bee... │
│ ☑ LinkedIn             John viewed your pro... │
│ ☐ IT Department        Update your password... │
│ ☐ CEO                  Urgent: Wire transfer...│
└─────────────────────────────────────────────────┘
       ↓ (User clicks email)
┌─────────────────────────────────────────────────┐
│ From: Microsoft Security Team                   │
│ To: john.smith@company.com                      │
│ Subject: Action Required: Verify Your Account   │
│ ───────────────────────────────────────────────│
│ Dear John,                                      │
│                                                 │
│ We detected unusual activity...                 │
│                                                 │
│ [Verify Account] ← Clickable                    │
│                                                 │
│ └─> Clicking shows educational feedback         │
└─────────────────────────────────────────────────┘
```

### Safe Payload Delivery

**Landing page interaction flow:**

```javascript
// When user clicks phishing link
function handlePhishingClick(event) {
    event.preventDefault();

    // Log the click for training metrics
    trackEvent({
        type: 'phishing_click',
        timestamp: new Date(),
        userId: getCurrentUserId(),
        campaignId: getCampaignId()
    });

    // Option 1: Show immediate education
    showEducationalModal({
        title: "⚠️ You Just Clicked a Phishing Link!",
        message: "This was a simulated phishing attack...",
        indicators: [
            "The sender address was suspicious: security@microsoft-verify.com",
            "The urgency created pressure to act quickly",
            "The link URL doesn't match Microsoft's domain"
        ],
        learnMore: "/training/phishing-awareness"
    });

    // Option 2: Show fake landing page first, then educate
    // (more realistic simulation)
    showFakeLandingPage();
}

function showFakeLandingPage() {
    // Display convincing login page
    // When user attempts to enter credentials:
    showCredentialWarning();
}
```

### Campaign Metrics and Measurement

**Key performance indicators:**

```javascript
const campaignMetrics = {
    sent: 1000,              // Total emails sent
    opened: 750,             // Open rate: 75%
    clicked: 200,            // Click rate: 20%
    credentialEntry: 50,     // Credential entry: 5%
    reported: 100,           // Reported as phishing: 10%

    // Improvement over time
    improvement: {
        previousCampaign: {
            clicked: 350,    // 35% -> 20% (43% improvement)
            credentialEntry: 120  // 12% -> 5% (58% improvement)
        }
    },

    // Risk segmentation
    highRisk: [
        // Users who clicked and entered credentials
        "user1@company.com",
        "user2@company.com"
    ],
    mediumRisk: [
        // Users who clicked but didn't enter credentials
        "user3@company.com"
    ],
    lowRisk: [
        // Users who reported the phishing attempt
        "user4@company.com"
    ]
};
```

**Visual dashboard data:**

```
Campaign: Q1 2026 Phishing Simulation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Overall Results:
   Emails Sent:     1,000
   Opened:            750  (75%)  ████████████████░░░░
   Clicked:           200  (20%)  ████░░░░░░░░░░░░░░░░
   Compromised:        50  (5%)   █░░░░░░░░░░░░░░░░░░░
   Reported:          100  (10%)  ██░░░░░░░░░░░░░░░░░░

📈 Trend (vs. previous campaign):
   Click rate:        ↓ 43% improvement
   Compromise rate:   ↓ 58% improvement

🎯 Department Performance:
   Engineering:       8% clicked   ✓ Below average
   Finance:          32% clicked   ⚠ Needs training
   HR:               15% clicked   → Average
   Executive:        45% clicked   ❌ Critical risk

⏱ Response Time Analysis:
   Avg. time to click:     4.5 minutes
   Avg. time to report:    12.3 minutes
   Fastest reporter:       42 seconds
```

---

## 7. Security Awareness Lessons

### How to Identify Phishing Emails

**The SPAM Framework:**

**S - Sender Analysis**
- Check the actual email address, not just the display name
- Look for misspellings in the domain
- Verify sender with known contacts outside of email

**P - Purpose & Pressure**
- Be suspicious of urgent or threatening language
- Question unexpected requests for action
- Slow down - phishing relies on quick, emotional decisions

**A - Attachments & Links**
- Hover over links to see the actual URL
- Don't open unexpected attachments
- Be wary of QR codes in emails

**M - Message Quality**
- Check for grammar and spelling errors
- Look for generic greetings ("Dear Customer")
- Verify logos and branding quality

### Technical Indicators Checklist

```markdown
## Email Header Analysis

### Sender Address Inspection
- [ ] Display name matches email address
- [ ] Domain matches known legitimate domain
- [ ] No lookalike characters (0 vs O, 1 vs l)
- [ ] No suspicious subdomains

### SPF/DKIM/DMARC Check
- [ ] Email passes SPF validation
- [ ] DKIM signature present and valid
- [ ] DMARC policy enforced

## Body Content Analysis

### URL Inspection
- [ ] Hover test performed on all links
- [ ] URLs match expected domain
- [ ] No URL shorteners from unknown sources
- [ ] HTTPS used (but not sufficient alone!)

### Attachment Safety
- [ ] File extension matches file type
- [ ] No double extensions (.pdf.exe)
- [ ] No unexpected macro-enabled files
- [ ] Scanned by antivirus before opening

## Context Verification

### Request Validation
- [ ] Request matches normal business process
- [ ] Contact verified through alternate channel
- [ ] Information requested is appropriate
- [ ] No unusual urgency or pressure

## Red Flags Present

### Immediate Red Flags
- [ ] Threats of account closure
- [ ] Requests for passwords or credentials
- [ ] Wire transfer requests via email
- [ ] Unexpected invoices or payments
- [ ] Prize/lottery winnings
- [ ] Requests to bypass security procedures
```

### Behavioral Red Flags

**Urgency and Pressure:**
```
❌ "Your account will be closed in 2 hours!"
❌ "Immediate action required or face penalties"
❌ "Respond within 30 minutes"
✓  "Please update your payment method at your convenience"
```

**Requests for Sensitive Information:**
```
❌ "Verify your account by providing your password"
❌ "Confirm your SSN for security purposes"
❌ "Update your payment info by clicking here"
✓  "Contact our support team at [known phone number]"
```

**Unusual Requests:**
```
❌ "CEO needs gift cards purchased immediately"
❌ "Update W-9 and send to this new email address"
❌ "Process this wire transfer ASAP, I'm in a meeting"
✓  "Please follow normal procurement process for..."
```

### Best Practices for Organizations

**1. Technical Controls:**
```
Email Security Stack:
┌─────────────────────┐
│ Email Gateway       │ ← SPF/DKIM/DMARC validation
├─────────────────────┤
│ URL Filtering       │ ← Block known phishing domains
├─────────────────────┤
│ Attachment Sandbox  │ ← Detonate suspicious files
├─────────────────────┤
│ Link Rewriting      │ ← Scan links at click-time
├─────────────────────┤
│ User Reporting      │ ← Easy "Report Phishing" button
└─────────────────────┘
```

**2. User Training:**
- Regular phishing simulations (quarterly recommended)
- Progressive difficulty (easy → moderate → hard)
- Just-in-time training after failed tests
- Positive reinforcement for reporting

**3. Incident Response:**
```javascript
// Phishing Incident Response Workflow
const responseWorkflow = {
    detection: {
        actions: [
            "User reports suspicious email",
            "Security team investigates",
            "Determine if genuine threat"
        ],
        SLA: "< 30 minutes"
    },
    containment: {
        actions: [
            "Block sender domain",
            "Remove email from all inboxes",
            "Disable compromised accounts",
            "Reset credentials if needed"
        ],
        SLA: "< 1 hour"
    },
    eradication: {
        actions: [
            "Scan for similar emails",
            "Update email filters",
            "Block IOCs (domains, IPs)"
        ],
        SLA: "< 4 hours"
    },
    recovery: {
        actions: [
            "Restore account access",
            "Monitor for further attempts",
            "Verify no lateral movement"
        ],
        SLA: "< 24 hours"
    },
    lessons: {
        actions: [
            "Analyze what worked/failed",
            "Update training materials",
            "Adjust technical controls"
        ],
        SLA: "< 1 week"
    }
};
```

---

## 8. Privacy and Compliance

### GDPR Compliance in Phishing Simulations

**Data collected by simulators:**
- Email addresses
- Names and job titles
- Interaction data (opens, clicks)
- Device/browser information
- Timestamp data

**GDPR requirements:**

```markdown
## Lawful Basis for Processing
- **Legitimate Interest**: Employee security training
- **Consent**: Optional for non-employees
- **Contract**: May be part of employment agreement

## Data Subject Rights
- Right to access: Users can see their training data
- Right to erasure: Users can request data deletion
- Right to object: Users can opt-out (with HR approval)
- Right to portability: Export training records

## Privacy by Design
- Minimize data collection (only what's needed)
- Pseudonymization where possible
- Encryption in transit and at rest
- Regular data deletion (retain only necessary period)

## Transparency
- Clear privacy notice before campaigns
- Explanation of how data will be used
- Contact information for privacy questions
```

**Privacy notice example:**
```
Security Awareness Training Notice

Our organization conducts periodic phishing simulations to help
protect against cyber threats. These simulations may:

✓ Send realistic phishing emails to your work address
✓ Track whether you open, click, or report these emails
✓ Collect device and browser information
✓ Use your name, email, and job title for personalization

Your data will:
✓ Be used solely for security training purposes
✓ Be stored securely and encrypted
✓ Be retained for 12 months
✓ Not be shared with third parties
✓ Be accessible to you upon request

For questions: privacy@company.com
```

### Regional Data Storage

CanIPhish offers regional storage to comply with data residency requirements:

```
Data Residency Options:
├── North America
│   ├── United States (US-EAST, US-WEST)
│   └── Canada (CA-CENTRAL)
├── Europe
│   ├── United Kingdom (UK-LONDON)
│   ├── Germany (EU-FRANKFURT)
│   └── Ireland (EU-DUBLIN)
├── Asia Pacific
│   ├── Australia (AP-SYDNEY)
│   ├── Singapore (AP-SINGAPORE)
│   └── Japan (AP-TOKYO)
└── South America
    └── Brazil (SA-SAOPAULO)
```

### Ethical Considerations

**Ethical guidelines for phishing simulations:**

```markdown
## DO's
✓ Obtain management approval before campaigns
✓ Inform employees that simulations occur (not when/how)
✓ Provide immediate education after failed tests
✓ Celebrate employees who report phishing attempts
✓ Use realistic scenarios relevant to actual threats
✓ Protect employee data privacy
✓ Track trends, not individual "failures"

## DON'Ts
❌ Use sensitive topics (health, finance, layoffs) without care
❌ Simulate attacks from trusted internal sources (CEO, HR) too often
❌ Publicly shame employees who fail tests
❌ Conduct simulations during stressful periods
❌ Make it a "gotcha" game
❌ Use overly sophisticated attacks beyond real threat level
❌ Collect unnecessary personal data
```

**Controversial scenarios:**

```markdown
## Scenarios to Avoid or Use with Extreme Caution

### Health-Related Phishing
Example: "Click here for COVID test results"
Risk: May cause unnecessary anxiety
When acceptable: During actual health crises with HR approval

### Financial Distress
Example: "Company layoffs announced - view list"
Risk: Creates workplace fear and distrust
When acceptable: Generally not recommended

### HR/Benefits Phishing
Example: "Update W-2 information"
Risk: Employees expect these communications
When acceptable: With HR coordination and clear alternatives

### Executive Impersonation
Example: CEO requesting urgent wire transfer
Risk: Undermines trust in leadership
When acceptable: When actual BEC attacks are occurring
```

---

## 9. Building Similar Systems (Educational)

### Architecture Recommendations

If building an educational phishing simulator, consider this architecture:

```
┌─────────────────────────────────────────────────────────┐
│                    Load Balancer                        │
└───────────────────────┬─────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
┌───────▼──────┐ ┌──────▼──────┐ ┌─────▼──────┐
│  Web Server  │ │ Web Server  │ │ Web Server │
│   (Django/   │ │   (Django/  │ │   (Django/ │
│    Flask)    │ │    Flask)   │ │    Flask)  │
└───────┬──────┘ └──────┬──────┘ └─────┬──────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
┌───────▼──────┐ ┌──────▼──────┐ ┌─────▼──────┐
│   Database   │ │   Message   │ │   Object   │
│  (PostgreSQL)│ │    Queue    │ │  Storage   │
│              │ │   (Redis/   │ │  (S3/Minio)│
│              │ │   RabbitMQ) │ │            │
└──────────────┘ └─────────────┘ └────────────┘
```

### Template Management Strategy

**Database schema for templates:**

```sql
-- Templates table
CREATE TABLE phishing_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    difficulty VARCHAR(20) CHECK (difficulty IN ('easy', 'moderate', 'hard')),
    threat_vector VARCHAR(50) CHECK (threat_vector IN ('credentials', 'attachment', 'qr_code', 'link')),
    language_code VARCHAR(10) NOT NULL,
    subject_template TEXT NOT NULL,
    body_template_url TEXT NOT NULL,  -- S3 URL
    sender_template VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN DEFAULT true
);

-- Template variables
CREATE TABLE template_variables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    template_id UUID REFERENCES phishing_templates(id),
    variable_name VARCHAR(100) NOT NULL,
    variable_type VARCHAR(50),  -- 'text', 'email', 'url', 'date'
    is_required BOOLEAN DEFAULT true,
    default_value TEXT
);

-- Campaign templates (which templates are used in which campaigns)
CREATE TABLE campaign_templates (
    campaign_id UUID REFERENCES campaigns(id),
    template_id UUID REFERENCES phishing_templates(id),
    weight INTEGER DEFAULT 1,  -- For A/B testing
    PRIMARY KEY (campaign_id, template_id)
);
```

**Template versioning:**

```python
# Template version control
class PhishingTemplate:
    def __init__(self, template_id):
        self.template_id = template_id
        self.version_history = []

    def create_version(self, content, author):
        """Create new version of template"""
        version = {
            'version_number': len(self.version_history) + 1,
            'content': content,
            'author': author,
            'timestamp': datetime.now(),
            'checksum': hashlib.sha256(content.encode()).hexdigest()
        }
        self.version_history.append(version)

        # Upload to S3 with version path
        s3_key = f"templates/{self.template_id}/v{version['version_number']}.html"
        upload_to_s3(s3_key, content)

        return version

    def rollback_to_version(self, version_number):
        """Rollback to previous version"""
        if version_number <= len(self.version_history):
            return self.version_history[version_number - 1]
        raise ValueError("Version not found")
```

### Safe Payload Delivery

**Educational landing page implementation:**

```python
from flask import Flask, request, render_template, redirect
import logging

app = Flask(__name__)

@app.route('/phishing/<campaign_id>/<user_token>')
def phishing_landing(campaign_id, user_token):
    """
    Phishing landing page that educates rather than captures credentials
    """
    # Log the phishing click
    log_phishing_attempt(
        campaign_id=campaign_id,
        user_token=user_token,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent'),
        timestamp=datetime.now()
    )

    # Option 1: Immediate education (recommended for testing)
    if get_campaign_mode(campaign_id) == 'immediate_feedback':
        return render_template(
            'phishing_caught.html',
            indicators=get_phishing_indicators(campaign_id),
            training_resources=get_training_materials()
        )

    # Option 2: Show fake login page, then educate when credentials entered
    elif get_campaign_mode(campaign_id) == 'realistic_simulation':
        return render_template(
            'fake_login.html',
            brand=get_campaign_brand(campaign_id)
        )

@app.route('/phishing/<campaign_id>/<user_token>/submit', methods=['POST'])
def phishing_credential_attempt(campaign_id, user_token):
    """
    Handle credential entry attempt (DO NOT actually capture!)
    """
    # Log the credential entry attempt (not the actual credentials!)
    log_credential_attempt(
        campaign_id=campaign_id,
        user_token=user_token,
        timestamp=datetime.now()
    )

    # Show educational content
    return render_template(
        'phishing_caught_credentials.html',
        severity='high',
        immediate_actions=[
            "Change your password immediately",
            "Enable two-factor authentication",
            "Review recent account activity",
            "Complete phishing awareness training"
        ]
    )

def log_phishing_attempt(campaign_id, user_token, **kwargs):
    """Log phishing attempt without storing sensitive data"""
    log_entry = {
        'event_type': 'phishing_click',
        'campaign_id': campaign_id,
        'user_id': get_user_from_token(user_token),  # Hashed/anonymized
        'timestamp': kwargs.get('timestamp'),
        'ip_address_hash': hash_ip(kwargs.get('ip_address')),  # Hash IP for privacy
        'user_agent': kwargs.get('user_agent')
    }

    # Store in database
    store_training_event(log_entry)

    # Send notification to security team
    if is_high_risk_user(user_token):
        notify_security_team(log_entry)

# Educational content template
PHISHING_CAUGHT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phishing Awareness Alert</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        .alert-box {
            background-color: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 30px;
        }
        .warning-icon {
            font-size: 48px;
            text-align: center;
        }
        h1 {
            color: #856404;
            text-align: center;
        }
        .indicators {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 4px;
            margin: 20px 0;
        }
        .learn-more {
            background-color: #0078d4;
            color: white;
            padding: 12px 30px;
            text-decoration: none;
            border-radius: 4px;
            display: inline-block;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="alert-box">
        <div class="warning-icon">⚠️</div>
        <h1>You Just Clicked a Simulated Phishing Link!</h1>

        <p><strong>Don't worry - this was a training exercise.</strong></p>

        <p>
            This was a simulated phishing attack designed to help you recognize
            and avoid real phishing attempts. No harm was done, but in a real
            attack, clicking this link could have compromised your account.
        </p>

        <div class="indicators">
            <h3>🔍 Red Flags You Should Have Noticed:</h3>
            <ul>
                {{ phishing_indicators }}
            </ul>
        </div>

        <h3>✅ What to Do Next Time:</h3>
        <ol>
            <li><strong>Check the sender</strong> - Verify the email address matches the claimed sender</li>
            <li><strong>Hover over links</strong> - See the real URL before clicking</li>
            <li><strong>Look for urgency</strong> - Phishing emails create false urgency</li>
            <li><strong>When in doubt, report it</strong> - Use the "Report Phishing" button</li>
        </ol>

        <a href="/training/phishing-awareness" class="learn-more">
            Complete Phishing Awareness Training (15 minutes)
        </a>
    </div>
</body>
</html>
"""
```

### Tracking Without Compromising Privacy

**Privacy-preserving analytics:**

```python
import hashlib
import hmac

class PrivacyPreservingAnalytics:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def anonymize_user_id(self, user_id):
        """Create consistent but anonymized user identifier"""
        return hmac.new(
            self.secret_key.encode(),
            user_id.encode(),
            hashlib.sha256
        ).hexdigest()[:16]

    def anonymize_ip(self, ip_address):
        """Hash IP address for privacy"""
        # Keep only network portion for geolocation
        if '.' in ip_address:  # IPv4
            parts = ip_address.split('.')
            network = '.'.join(parts[:3]) + '.0'
            return hashlib.sha256(network.encode()).hexdigest()[:16]
        # Similar for IPv6
        return hashlib.sha256(ip_address.encode()).hexdigest()[:16]

    def record_event(self, event_type, user_id, metadata):
        """Record event with privacy protection"""
        event = {
            'type': event_type,
            'user_hash': self.anonymize_user_id(user_id),
            'timestamp': datetime.now().isoformat(),
            'campaign_id': metadata.get('campaign_id'),
            'template_id': metadata.get('template_id'),
            # Don't store: email content, credentials, full IPs
        }

        # Aggregate immediately, discard individual events after 30 days
        self.aggregate_metrics(event)
        self.store_event(event, ttl=30)  # Auto-delete after 30 days

    def aggregate_metrics(self, event):
        """Create aggregate metrics without storing individual data"""
        metrics_key = f"campaign:{event['campaign_id']}:daily:{date.today()}"

        # Increment counters (no individual tracking)
        increment_counter(f"{metrics_key}:sent")
        if event['type'] == 'email_opened':
            increment_counter(f"{metrics_key}:opened")
        elif event['type'] == 'link_clicked':
            increment_counter(f"{metrics_key}:clicked")
        elif event['type'] == 'credentials_entered':
            increment_counter(f"{metrics_key}:compromised")
        elif event['type'] == 'reported':
            increment_counter(f"{metrics_key}:reported")
```

---

## 10. Detection and Defense

### Email Authentication Protocols

#### SPF (Sender Policy Framework)

SPF allows domain owners to specify which servers can send email for their domain.

**How SPF Works:**

```
1. Attacker sends email claiming to be from victim.com
   From: support@victim.com
   Actual server: attacker-server.com (IP: 203.0.113.5)

2. Recipient's mail server receives email

3. Mail server queries DNS for victim.com's SPF record
   DNS Query: TXT record for victim.com

4. SPF Record Found:
   v=spf1 ip4:192.0.2.0/24 include:_spf.google.com -all

5. Check if sending IP (203.0.113.5) is authorized
   - NOT in 192.0.2.0/24
   - NOT in Google's SPF record
   - Policy: -all (reject)

6. Result: FAIL - Email rejected or marked as spam
```

**SPF Record Syntax:**

```dns
; SPF record for example.com
example.com. IN TXT "v=spf1 ip4:192.0.2.0/24 ip4:198.51.100.5 include:_spf.google.com include:sendgrid.net -all"

Breakdown:
v=spf1              - SPF version 1
ip4:192.0.2.0/24    - Authorize this IP range
ip4:198.51.100.5    - Authorize this specific IP
include:_spf.google.com - Include Google's SPF record (for Gmail)
include:sendgrid.net    - Include SendGrid's SPF record (for email service)
-all                - Reject all other senders (strict policy)

Alternatives for -all:
~all    - Soft fail (mark as suspicious but don't reject)
?all    - Neutral (no policy)
+all    - Accept all (insecure, not recommended)
```

#### DKIM (DomainKeys Identified Mail)

DKIM adds a cryptographic signature to email headers.

**How DKIM Works:**

```
1. Sending server signs the email
   ┌─────────────────────────────────────┐
   │ Email Content:                      │
   │ From: support@example.com           │
   │ To: user@recipient.com              │
   │ Subject: Account Update             │
   │ Body: Please verify your account... │
   └─────────────────────────────────────┘
            ↓
   Hash content with private key
            ↓
   ┌─────────────────────────────────────┐
   │ DKIM-Signature: v=1; a=rsa-sha256;  │
   │   d=example.com; s=selector1;       │
   │   h=from:to:subject:date;           │
   │   bh=base64hash;                    │
   │   b=signaturebase64                 │
   └─────────────────────────────────────┘

2. Email sent with signature header

3. Receiving server validates
   - Extract DKIM signature from header
   - Query DNS for public key:
     selector1._domainkey.example.com
   - Decrypt signature with public key
   - Compare hash to actual email content
   - If match: PASS, If not: FAIL
```

**DKIM DNS Record:**

```dns
; Public key published in DNS
selector1._domainkey.example.com. IN TXT "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC..."

Components:
v=DKIM1     - DKIM version
k=rsa       - Key type (RSA)
p=...       - Public key (base64 encoded)
```

**DKIM Protection:**
- Prevents email tampering in transit
- Verifies email came from claimed domain
- Attacker can't forge signature without private key

#### DMARC (Domain-based Message Authentication, Reporting & Conformance)

DMARC builds on SPF and DKIM to provide policy enforcement and reporting.

**DMARC Policy:**

```dns
_dmarc.example.com. IN TXT "v=DMARC1; p=reject; rua=mailto:dmarc-reports@example.com; ruf=mailto:dmarc-forensics@example.com; fo=1; adkim=s; aspf=s; pct=100"

Components:
v=DMARC1    - DMARC version
p=reject    - Policy: reject emails that fail (alternatives: none, quarantine)
rua=mailto:dmarc-reports@example.com  - Aggregate report destination
ruf=mailto:dmarc-forensics@example.com - Forensic report destination
fo=1        - Forensic options (when to send failure reports)
adkim=s     - DKIM alignment mode (s=strict, r=relaxed)
aspf=s      - SPF alignment mode (s=strict, r=relaxed)
pct=100     - Percentage of emails to apply policy to
```

**DMARC Flow:**

```
1. Email received from support@example.com

2. Check SPF
   ✓ PASS - Sending server authorized

3. Check DKIM
   ✓ PASS - Signature valid

4. Check DMARC Alignment
   - SPF domain matches From domain? ✓
   - DKIM domain matches From domain? ✓

5. DMARC Result: PASS
   - Deliver email normally

6. Send aggregate report to rua address
   (Daily summary of authentication results)

Alternative scenario:
2. SPF: FAIL
3. DKIM: FAIL
4. DMARC: FAIL
5. Apply policy (p=reject) → Email rejected
6. Send forensic report to ruf address
```

### URL Analysis Techniques

**Manual URL inspection:**

```python
from urllib.parse import urlparse
import re

def analyze_phishing_url(url):
    """Analyze URL for phishing indicators"""
    indicators = []
    risk_score = 0

    parsed = urlparse(url)

    # 1. Check for IP address instead of domain
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', parsed.netloc):
        indicators.append("Using IP address instead of domain name")
        risk_score += 30

    # 2. Check for suspicious TLDs
    suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.zip', '.mov']
    if any(parsed.netloc.endswith(tld) for tld in suspicious_tlds):
        indicators.append(f"Suspicious TLD: {parsed.netloc.split('.')[-1]}")
        risk_score += 20

    # 3. Check for lookalike characters
    lookalike_patterns = [
        (r'paypa1', 'Lookalike: paypa1 (1 instead of l)'),
        (r'g00gle', 'Lookalike: g00gle (0 instead of o)'),
        (r'micros0ft', 'Lookalike: micros0ft (0 instead of o)'),
    ]
    for pattern, message in lookalike_patterns:
        if re.search(pattern, parsed.netloc, re.IGNORECASE):
            indicators.append(message)
            risk_score += 40

    # 4. Check for excessive subdomains
    subdomain_count = parsed.netloc.count('.')
    if subdomain_count > 3:
        indicators.append(f"Excessive subdomains ({subdomain_count})")
        risk_score += 15

    # 5. Check for misleading subdomain
    # Example: paypal.com.attacker.com
    trusted_domains = ['paypal.com', 'microsoft.com', 'google.com', 'apple.com']
    for trusted in trusted_domains:
        if trusted in parsed.netloc and not parsed.netloc.endswith(trusted):
            indicators.append(f"Misleading subdomain containing '{trusted}'")
            risk_score += 50

    # 6. Check for unusual port
    if parsed.port and parsed.port not in [80, 443]:
        indicators.append(f"Unusual port: {parsed.port}")
        risk_score += 10

    # 7. Check URL length (phishing URLs often very long)
    if len(url) > 150:
        indicators.append(f"Unusually long URL ({len(url)} characters)")
        risk_score += 15

    # 8. Check for @ symbol (username in URL)
    if '@' in parsed.netloc:
        indicators.append("Contains @ symbol (authentication bypass attempt)")
        risk_score += 35

    # 9. Check for HTTP instead of HTTPS
    if parsed.scheme == 'http':
        indicators.append("Unencrypted HTTP connection")
        risk_score += 10

    # Risk classification
    if risk_score >= 50:
        risk_level = "HIGH - Likely phishing"
    elif risk_score >= 25:
        risk_level = "MEDIUM - Suspicious"
    else:
        risk_level = "LOW - Appears safe"

    return {
        'url': url,
        'risk_score': risk_score,
        'risk_level': risk_level,
        'indicators': indicators,
        'domain': parsed.netloc,
        'scheme': parsed.scheme
    }

# Example usage
urls_to_check = [
    "https://paypa1.com/verify",
    "http://192.168.1.1/login",
    "https://paypal.com.verify-account.tk/secure",
    "https://microsoft.com",  # Legitimate
]

for url in urls_to_check:
    result = analyze_phishing_url(url)
    print(f"\n{'='*60}")
    print(f"URL: {result['url']}")
    print(f"Risk: {result['risk_level']} (Score: {result['risk_score']})")
    if result['indicators']:
        print("Indicators:")
        for indicator in result['indicators']:
            print(f"  - {indicator}")
```

### Attachment Sandboxing

**Sandbox workflow:**

```python
import subprocess
import hashlib
import os

class AttachmentSandbox:
    def __init__(self, sandbox_vm):
        self.sandbox_vm = sandbox_vm
        self.malware_signatures = self.load_signatures()

    def analyze_attachment(self, file_path):
        """Analyze email attachment for malicious behavior"""
        results = {
            'file_name': os.path.basename(file_path),
            'file_hash': self.calculate_hash(file_path),
            'static_analysis': {},
            'dynamic_analysis': {},
            'verdict': 'unknown'
        }

        # Step 1: Static Analysis
        results['static_analysis'] = self.static_analysis(file_path)

        # Step 2: Signature Matching
        if self.check_known_malware(results['file_hash']):
            results['verdict'] = 'malicious'
            results['reason'] = 'Known malware signature'
            return results

        # Step 3: Dynamic Analysis (in sandbox)
        if self.requires_dynamic_analysis(file_path):
            results['dynamic_analysis'] = self.dynamic_analysis(file_path)

        # Step 4: Determine verdict
        results['verdict'] = self.determine_verdict(results)

        return results

    def static_analysis(self, file_path):
        """Analyze file without executing it"""
        analysis = {}

        # Check file extension vs actual type
        claimed_ext = os.path.splitext(file_path)[1]
        actual_type = self.get_file_type(file_path)

        if claimed_ext != actual_type:
            analysis['extension_mismatch'] = True
            analysis['claimed'] = claimed_ext
            analysis['actual'] = actual_type

        # Check for double extensions
        if file_path.count('.') > 1:
            analysis['double_extension'] = True

        # For Office docs, check for macros
        if actual_type in ['.docx', '.xlsx', '.pptx']:
            analysis['contains_macros'] = self.check_for_macros(file_path)

        # For PDFs, check for JavaScript
        if actual_type == '.pdf':
            analysis['contains_javascript'] = self.check_pdf_javascript(file_path)

        # Check file entropy (high entropy = encrypted/packed)
        analysis['entropy'] = self.calculate_entropy(file_path)
        if analysis['entropy'] > 7.5:  # High entropy threshold
            analysis['possibly_packed'] = True

        return analysis

    def dynamic_analysis(self, file_path):
        """Execute file in isolated sandbox and monitor behavior"""
        behaviors = {
            'file_operations': [],
            'registry_changes': [],
            'network_connections': [],
            'process_creation': [],
            'suspicious_api_calls': []
        }

        # Start monitoring
        snapshot_before = self.create_vm_snapshot(self.sandbox_vm)

        # Copy file to sandbox
        self.copy_to_sandbox(file_path)

        # Execute with monitoring
        self.execute_in_sandbox(file_path, timeout=60)

        # Collect behaviors
        behaviors['file_operations'] = self.get_file_changes()
        behaviors['registry_changes'] = self.get_registry_changes()
        behaviors['network_connections'] = self.get_network_activity()
        behaviors['process_creation'] = self.get_new_processes()

        # Restore VM to clean state
        self.restore_vm_snapshot(snapshot_before)

        return behaviors

    def determine_verdict(self, results):
        """Determine if file is malicious based on analysis"""
        score = 0

        # Static analysis indicators
        if results['static_analysis'].get('extension_mismatch'):
            score += 30
        if results['static_analysis'].get('double_extension'):
            score += 25
        if results['static_analysis'].get('contains_macros'):
            score += 15
        if results['static_analysis'].get('possibly_packed'):
            score += 20

        # Dynamic analysis indicators
        dynamic = results.get('dynamic_analysis', {})
        if len(dynamic.get('network_connections', [])) > 0:
            score += 35  # Unexpected network activity
        if len(dynamic.get('registry_changes', [])) > 10:
            score += 25  # Excessive registry changes
        if any('cmd.exe' in p or 'powershell' in p
               for p in dynamic.get('process_creation', [])):
            score += 40  # Spawning command shells

        # Verdict based on score
        if score >= 60:
            return 'malicious'
        elif score >= 30:
            return 'suspicious'
        else:
            return 'clean'

    def calculate_hash(self, file_path):
        """Calculate SHA-256 hash of file"""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def calculate_entropy(self, file_path):
        """Calculate Shannon entropy of file"""
        import math
        from collections import Counter

        with open(file_path, 'rb') as f:
            data = f.read()

        if not data:
            return 0

        # Count byte frequency
        counter = Counter(data)
        length = len(data)

        # Calculate entropy
        entropy = 0
        for count in counter.values():
            probability = count / length
            entropy -= probability * math.log2(probability)

        return entropy
```

### User Reporting Systems

**Phishing report button implementation:**

```javascript
// Gmail-style "Report Phishing" button
class PhishingReportButton {
    constructor() {
        this.init();
    }

    init() {
        // Add report button to email toolbar
        const toolbar = document.querySelector('.email-toolbar');
        const reportBtn = this.createReportButton();
        toolbar.appendChild(reportBtn);
    }

    createReportButton() {
        const button = document.createElement('button');
        button.className = 'report-phishing-btn';
        button.innerHTML = '🚨 Report Phishing';
        button.addEventListener('click', () => this.reportPhishing());
        return button;
    }

    async reportPhishing() {
        // Get current email details
        const emailData = {
            message_id: this.getCurrentMessageId(),
            sender: this.getCurrentSender(),
            subject: this.getCurrentSubject(),
            received_time: this.getCurrentTimestamp(),
            headers: this.getEmailHeaders(),
            urls: this.extractURLs(),
            attachments: this.getAttachments()
        };

        // Submit to security team
        const response = await fetch('/api/report-phishing', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(emailData)
        });

        if (response.ok) {
            // Move email to spam
            this.moveToSpam(emailData.message_id);

            // Show confirmation
            this.showConfirmation(
                'Thank you for reporting! Our security team will investigate.'
            );

            // If it's a training email, show educational content
            const result = await response.json();
            if (result.is_training) {
                this.showTrainingSuccess();
            }
        }
    }

    showTrainingSuccess() {
        const modal = document.createElement('div');
        modal.className = 'training-success-modal';
        modal.innerHTML = `
            <div class="modal-content">
                <h2>✅ Great Job!</h2>
                <p>
                    You correctly identified this as a phishing simulation.
                    This is exactly what you should do when you receive a
                    suspicious email.
                </p>
                <div class="stats">
                    <p><strong>Your Stats:</strong></p>
                    <p>Phishing emails reported: <span class="stat-number">15</span></p>
                    <p>Success rate: <span class="stat-number">94%</span></p>
                </div>
                <button onclick="this.closest('.modal').remove()">Close</button>
            </div>
        `;
        document.body.appendChild(modal);
    }
}
```

---

## 11. Practical Exercises

### Exercise 1: Identify the Phishing Email

**Scenario:** You receive the following email. Identify all phishing indicators.

```
From: Microsoft Security Team <security-alert@micros0ft-teams.com>
To: you@company.com
Subject: URGENT: Your account will be suspended in 24 hours

Dear User,

We have detected unusual sign-in activity on your Microsoft 365 account
from the following location:

Location: Lagos, Nigeria
IP Address: 102.89.23.147
Time: January 6, 2026 at 3:47 AM

If this was not you, your account will be automatically suspended in
24 hours to protect your data. Click below to verify your identity:

[Verify My Identity] → http://verify-microsoft.tk/secure?id=8g7f6d5s4

This is an automated security alert. Do not reply to this email.

Regards,
Microsoft Security Team
```

<details>
<summary>Click to see analysis</summary>

**Phishing Indicators Found:**

1. **Sender Address:**
   - Domain: `micros0ft-teams.com` (zero instead of 'o')
   - Not Microsoft's legitimate domain (microsoft.com)
   - ⚠️ **Risk Level: CRITICAL**

2. **Urgency/Pressure:**
   - "URGENT" in subject
   - "24 hours" deadline creates panic
   - ⚠️ **Risk Level: HIGH**

3. **Generic Greeting:**
   - "Dear User" instead of your actual name
   - Real Microsoft emails use your account name
   - ⚠️ **Risk Level: MEDIUM**

4. **Suspicious URL:**
   - Domain: `verify-microsoft.tk`
   - `.tk` is a free domain (common in phishing)
   - Not HTTPS
   - Not microsoft.com
   - ⚠️ **Risk Level: CRITICAL**

5. **Geographic Logic:**
   - If you're not in Nigeria, this alone is suspicious
   - But Microsoft would show your actual location if real
   - ⚠️ **Risk Level: MEDIUM**

**Verdict: PHISHING**
**Recommended Action: Report and delete**

</details>

### Exercise 2: QR Code Analysis

**Scenario:** You receive a physical flyer on your car windshield:

```
┌───────────────────────────────────┐
│   PARKING VIOLATION NOTICE        │
│                                   │
│ Your vehicle is scheduled for tow │
│ due to expired parking permit.    │
│                                   │
│ Scan to pay fine and avoid tow:   │
│                                   │
│     ┌─────────────┐              │
│     │ █▀▀▀▀▀▀▀▀█ │              │
│     │ █ ████  █ █ │              │
│     │ █ ▀▀▀▀  █ █ │              │
│     │ █▄▄▄▄▄▄▄▄█ │              │
│     └─────────────┘              │
│                                   │
│ Fine: $75 if paid within 2 hours  │
└───────────────────────────────────┘
```

<details>
<summary>Click to see analysis</summary>

**Red Flags:**

1. **Physical Distribution:**
   - Legitimate parking notices are issued by parking enforcement
   - Would have official letterhead and citation number
   - ⚠️ **Risk Level: HIGH**

2. **Payment Method:**
   - Legitimate parking tickets have specific payment portals
   - QR codes on physical notices are unusual
   - ⚠️ **Risk Level: CRITICAL**

3. **Urgency:**
   - "2 hours" creates panic
   - Real citations have standard payment windows (weeks)
   - ⚠️ **Risk Level: HIGH**

4. **No Official Information:**
   - No citation number
   - No contact information
   - No agency name
   - ⚠️ **Risk Level: CRITICAL**

**What Could Happen:**
- QR code leads to fake payment site
- Captures credit card information
- Installs malware on phone

**Correct Action:**
1. Do NOT scan the QR code
2. Check with your parking management office
3. Look for legitimate citation on your vehicle
4. Report to local police (parking scam)

</details>

### Exercise 3: Email Header Analysis

**Scenario:** Analyze these email headers to determine authenticity.

```
Received: from mail-sender.gmail.com (209.85.220.41)
From: "PayPal Service" <service@paypal.com>
Reply-To: support@paypal-verify.tk
Subject: Account Limited - Action Required
To: victim@example.com
Date: Mon, 6 Jan 2026 10:23:45 -0800
Authentication-Results: mx.google.com;
    spf=fail smtp.mailfrom=paypal-verify.tk;
    dkim=fail header.i=@paypal.com;
    dmarc=fail (p=REJECT)
```

<details>
<summary>Click to see analysis</summary>

**Header Analysis:**

1. **From Address:**
   - Displays: `service@paypal.com`
   - Looks legitimate
   - ⚠️ **Status: SUSPICIOUS** (check other indicators)

2. **Reply-To Address:**
   - `support@paypal-verify.tk`
   - Different domain from "From" address
   - `.tk` free domain
   - ⚠️ **Risk Level: CRITICAL**

3. **Authentication Results:**
   - **SPF: FAIL** - Sending server not authorized
   - **DKIM: FAIL** - Signature invalid/missing
   - **DMARC: FAIL** - Domain policy violated
   - ⚠️ **Risk Level: CRITICAL**

4. **DMARC Policy:**
   - `p=REJECT` means PayPal's policy is to reject failed emails
   - This email should have been blocked
   - Your email provider may have filtering disabled
   - ⚠️ **Risk Level: CRITICAL**

**Verdict: DEFINITE PHISHING**

Real PayPal emails:
- Pass SPF, DKIM, and DMARC
- Have matching Reply-To and From domains
- Come from `@paypal.com` or `@e.paypal.com`

**Action: Delete and report**

</details>

### Self-Assessment Quiz

**Question 1:** Which of the following is the MOST reliable indicator that an email is legitimate?

A) Professional-looking logo and design
B) Personalized greeting with your name
C) HTTPS link in the email
D) Passing SPF, DKIM, and DMARC authentication

<details>
<summary>Answer</summary>

**D) Passing SPF, DKIM, and DMARC authentication**

Explanation: All other indicators can be faked by attackers. Technical authentication protocols are the most reliable security measure, though they can also be bypassed if a legitimate account is compromised.

</details>

**Question 2:** You receive an email from your CEO requesting an urgent wire transfer. What should you do?

A) Process it immediately since it's from the CEO
B) Verify through a separate communication channel (call, in-person)
C) Reply to the email asking for confirmation
D) Forward to accounting department

<details>
<summary>Answer</summary>

**B) Verify through a separate communication channel**

Explanation: Business Email Compromise (BEC) attacks often impersonate executives. Always verify unusual requests (especially financial) through a separate, trusted channel like calling the person directly at a known number.

</details>

**Question 3:** What is "quishing"?

A) A type of malware
B) Phishing using QR codes
C) Quantum encryption phishing
D) Quick phishing attacks

<details>
<summary>Answer</summary>

**B) Phishing using QR codes**

Explanation: Quishing (QR code + phishing) is a growing threat where QR codes hide malicious URLs. Since you can't see the URL before scanning, it's easier for attackers to bypass security awareness.

</details>

---

## 12. Resources and References

### Security Awareness Organizations

**OWASP (Open Web Application Security Project)**
- Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- Security training resources and best practices

**CISA (Cybersecurity & Infrastructure Security Agency)**
- "Avoiding Social Engineering and Phishing Attacks"
- Free security awareness materials for organizations

**Anti-Phishing Working Group (APWG)**
- Phishing trend reports and statistics
- Industry collaboration on anti-phishing measures

### Email Security Standards

**SPF Documentation:**
- RFC 7208: https://tools.ietf.org/html/rfc7208
- SPF Record Syntax: http://www.open-spf.org/

**DKIM Documentation:**
- RFC 6376: https://tools.ietf.org/html/rfc6376
- DKIM Tools: https://dkimcore.org/

**DMARC Documentation:**
- RFC 7489: https://tools.ietf.org/html/rfc7489
- DMARC Guide: https://dmarc.org/

### QR Code Phishing (Quishing) Research

**Recent Research and Analysis:**
- [Hoxhunt - QR Code Phishing Explained](https://hoxhunt.com/blog/quishing)
- [Palo Alto Networks - QR Code Phenomenon](https://unit42.paloaltonetworks.com/qr-code-phishing/)
- [Cloudflare - What is Quishing?](https://www.cloudflare.com/learning/security/what-is-quishing/)
- [Barracuda - Evolving QR Codes in Phishing](https://blog.barracuda.com/2024/10/22/threat-spotlight-evolving-qr-codes-phishing-attacks)
- [SecurityHQ - QR Code Vulnerabilities](https://www.securityhq.com/blog/qr-code-vulnerabilities-dissecting-new-techniques-seen-in-the-wild/)

### Training Platforms

**Commercial Phishing Simulators:**
- CanIPhish: https://caniphish.com/
- KnowBe4: https://www.knowbe4.com/
- Cofense (PhishMe): https://cofense.com/
- Proofpoint Security Awareness: https://www.proofpoint.com/

**Open Source Tools:**
- Gophish: https://getgophish.com/
- King Phisher: https://github.com/securestate/king-phisher
- Social-Engineer Toolkit (SET): https://github.com/trustedsec/social-engineer-toolkit

### Legal and Ethical Framework

**Regulations to Consider:**
- CAN-SPAM Act (United States)
- GDPR (European Union)
- Computer Fraud and Abuse Act (CFAA)
- State-specific cybersecurity laws

**Ethical Guidelines:**
- Always obtain written authorization
- Have clear opt-out mechanisms
- Provide immediate education after simulations
- Never cause actual harm or distress
- Respect privacy and data protection laws

### Detection Tools

**Email Header Analysis:**
- MXToolbox: https://mxtoolbox.com/
- Google Admin Toolbox: https://toolbox.googleapps.com/
- Mail-Tester: https://www.mail-tester.com/

**URL Analysis:**
- VirusTotal: https://www.virustotal.com/
- URLScan.io: https://urlscan.io/
- PhishTank: https://phishtank.org/
- Google Safe Browsing: https://transparencyreport.google.com/safe-browsing/

**Sandbox Services:**
- Any.run: https://any.run/
- Hybrid Analysis: https://www.hybrid-analysis.com/
- Joe Sandbox: https://www.joesandbox.com/

### Books and Reading

- "The Art of Deception" by Kevin Mitnick
- "Social Engineering: The Science of Human Hacking" by Christopher Hadnagy
- "Phishing Dark Waters" by Michele Fincher and Christopher Hadnagy

---

## Conclusion

This analysis of phishing simulators like CanIPhish demonstrates the sophisticated techniques used in modern phishing attacks and the importance of comprehensive security awareness training. Key takeaways:

**For Individuals:**
1. Always verify sender addresses and domains
2. Never trust urgency alone as a reason to act
3. Use email authentication indicators (SPF/DKIM/DMARC)
4. Report suspicious emails immediately
5. When in doubt, verify through alternate channels

**For Organizations:**
1. Implement technical controls (email authentication, URL filtering, sandboxing)
2. Conduct regular phishing simulations with progressive difficulty
3. Provide immediate education, not punishment
4. Track trends and improvements over time
5. Ensure privacy and ethical compliance

**For Researchers:**
1. Study emerging attack vectors like QR code phishing
2. Understand both technical and psychological aspects
3. Share knowledge to improve collective defense
4. Always maintain ethical boundaries
5. Consider privacy implications in security research

Phishing remains one of the most effective attack vectors because it exploits human psychology rather than technical vulnerabilities. The best defense is a combination of technical controls, user education, and a security-conscious organizational culture.

**Stay vigilant. Stay secure.**

---

*This document was created for educational purposes to help individuals and organizations better understand and defend against phishing attacks.*

*Last updated: January 6, 2026*
