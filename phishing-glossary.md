# Phishing & Email Security Glossary

## A

**Attachment Sandboxing**
A security technique where email attachments are executed in an isolated virtual environment to detect malicious behavior before allowing them to reach users.

**Authentication**
The process of verifying the identity of a user, device, or sender. In email, this involves verifying that an email truly comes from the claimed sender using protocols like SPF, DKIM, and DMARC.

## B

**BEC (Business Email Compromise)**
A sophisticated phishing attack where criminals compromise or spoof executive email accounts to trick employees into transferring money or sensitive data. Also known as "CEO Fraud" or "Whaling."

**Botnet**
A network of compromised computers controlled by an attacker, often used to send large volumes of phishing emails.

## C

**CDN (Content Delivery Network)**
A distributed network of servers that delivers content to users based on geographic location. CanIPhish uses AWS S3 CDN to host email templates for fast global delivery.

**Credential Harvesting**
The process of stealing usernames and passwords, typically through fake login pages that mimic legitimate websites.

**Conversational Phishing**
A sophisticated phishing technique that involves back-and-forth email exchanges to build trust before making malicious requests, as opposed to single-email phishing attempts.

## D

**DKIM (DomainKeys Identified Mail)**
An email authentication method that uses cryptographic signatures to verify that an email hasn't been altered during transit and comes from an authorized sender.

**DMARC (Domain-based Message Authentication, Reporting and Conformance)**
An email authentication protocol that builds on SPF and DKIM, allowing domain owners to specify how to handle emails that fail authentication and receive reports about email authentication results.

**Domain Spoofing**
The practice of forging an email header so the message appears to have originated from a different domain than the actual source.

**Double Extension**
A file naming trick where a malicious file uses two extensions (e.g., "invoice.pdf.exe") to hide its true file type. Users see ".pdf" and think it's safe, but it's actually an executable ".exe" file.

## E

**Email Gateway**
A security system that filters incoming and outgoing email for spam, phishing, malware, and policy violations before messages reach user inboxes.

**Email Header**
Hidden technical information in an email that shows the path the message took from sender to recipient, including server information, authentication results, and timestamps.

**Entropy**
In file analysis, a measure of randomness in data. High entropy often indicates encryption or compression, which can be a sign of packed malware.

**EV Certificate (Extended Validation Certificate)**
A premium SSL/TLS certificate that shows the verified organization name in the browser address bar, providing higher assurance of website legitimacy.

## F

**False Positive**
When a legitimate email is incorrectly identified as phishing or spam by security filters.

**Forensic Analysis**
Detailed investigation of a security incident to understand what happened, how it happened, and what data was affected.

## G

**GDPR (General Data Protection Regulation)**
European Union regulation governing data privacy and protection, relevant to phishing simulators that collect user interaction data.

**GTM (Google Tag Manager)**
A tag management system that allows tracking user interactions on websites and emails, used by CanIPhish for analytics.

## H

**Header Injection**
An attack where malicious content is inserted into email headers to bypass security filters or alter email routing.

**HTTPS (Hypertext Transfer Protocol Secure)**
Encrypted version of HTTP used for secure communication over the internet. While phishing sites can use HTTPS, legitimate sites should always use it.

**Hover Test**
The practice of moving your mouse cursor over a link without clicking to preview the actual URL destination.

## I

**Impersonation**
Pretending to be someone else, typically a trusted entity like a bank, government agency, or company executive, to gain trust and trick victims.

**Indicator of Compromise (IOC)**
Evidence that a system has been attacked or compromised, such as malicious URLs, IP addresses, or file hashes associated with phishing attacks.

**Iframe (Inline Frame)**
An HTML element that embeds another document within the current page. Used by CanIPhish to safely preview email templates without executing malicious code.

## J

**JavaScript Obfuscation**
The practice of making JavaScript code difficult to read and understand, often used in malicious emails to hide malware or phishing functionality.

**Just-in-Time Training**
Security awareness training delivered immediately after a user fails a phishing simulation, when the lesson is most relevant and likely to be retained.

## K

**Keylogger**
Malware that records keystrokes to steal passwords and sensitive information, often delivered through phishing attachments.

**Kill Chain**
The sequence of stages in a cyber attack, from reconnaissance to data exfiltration. Phishing typically occurs in the "delivery" stage.

## L

**Landing Page**
The website users are directed to after clicking a phishing link, often designed to look like a legitimate login page to harvest credentials.

**Link Rewriting**
A security technique where URLs in emails are automatically replaced with links to a security service that scans the destination before allowing the user through.

**Lookalike Domain**
A domain name that closely resembles a legitimate domain but with subtle differences (e.g., "paypa1.com" instead of "paypal.com").

## M

**Macro**
Automated script in Microsoft Office documents that can perform actions. Phishing attacks often use malicious macros in Word or Excel files to install malware.

**Malvertising**
Malicious advertising that redirects users to phishing sites or delivers malware through legitimate ad networks.

**Multi-Factor Authentication (MFA / 2FA)**
Security method requiring two or more verification factors (password + code from phone), making accounts harder to compromise even if credentials are phished.

## O

**OWASP (Open Web Application Security Project)**
Non-profit organization focused on improving software security, provides guidelines and resources for preventing phishing and other attacks.

## P

**Payload**
The malicious component delivered by a phishing attack, such as malware, a credential harvesting page, or a malicious attachment.

**Personalization**
Customizing phishing emails with recipient-specific information (name, company, job title) to make them more convincing.

**Phishing**
Fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity in electronic communication.

**Phishing Kit**
Pre-packaged tools that make it easy for attackers to launch phishing campaigns, including fake login pages, email templates, and credential collection systems.

**Pretexting**
Creating a fabricated scenario (pretext) to manipulate targets into divulging information or performing actions they normally wouldn't.

## Q

**Quarantine**
Isolated area where suspicious emails are held for review before being delivered or deleted.

**Quishing (QR Code Phishing)**
Phishing attack that uses QR codes to hide malicious URLs, making it harder for users to inspect the link before visiting it.

## R

**Ransomware**
Malware that encrypts files and demands payment for decryption, often delivered through phishing emails.

**Redirect Chain**
Series of automatic redirects from one URL to another, often used in phishing to evade detection and complicate URL analysis.

**Replay-To Header**
Email header specifying where replies should be sent, often different from the "From" address in phishing emails.

## S

**Sandbox**
Isolated testing environment where suspicious files or code can be executed safely without risking the production system.

**Sender Policy Framework (SPF)**
Email authentication method that specifies which mail servers are authorized to send email on behalf of a domain.

**Smishing (SMS Phishing)**
Phishing conducted via SMS text messages instead of email.

**Social Engineering**
Manipulation technique that exploits human psychology to trick people into divulging confidential information or performing actions.

**Spam**
Unsolicited bulk email, often used as a vector for phishing attempts.

**Spear Phishing**
Targeted phishing attack customized for a specific individual or organization, more sophisticated than generic phishing.

**Spoofing**
Forging the sender address in an email to make it appear to come from someone else.

**SSL/TLS Certificate**
Digital certificate that authenticates a website's identity and enables encrypted connections (HTTPS).

## T

**Threat Actor**
Individual or group conducting cyber attacks, including phishing campaigns.

**Threat Intelligence**
Information about current and emerging phishing threats, including IOCs, attack techniques, and targeted organizations.

**TLD (Top-Level Domain)**
The last part of a domain name (.com, .org, .tk). Some TLDs like .tk are free and commonly abused for phishing.

**Trojan**
Malware disguised as legitimate software, often delivered through phishing email attachments.

## U

**URL Shortener**
Service that creates short aliases for long URLs, often abused in phishing to hide the true destination.

**User-Agent**
Information sent by a browser or email client identifying itself to servers, can be used to track phishing email opens.

**Urgency**
Common phishing tactic that creates time pressure ("act within 24 hours") to bypass rational decision-making.

## V

**Variable Injection**
Process of replacing placeholder text in email templates with personalized information for each recipient.

**Vishing (Voice Phishing)**
Phishing conducted via phone calls, often following up on email phishing attempts.

**Virtual Inbox**
Simulated email environment used in phishing training to let users practice identifying phishing emails safely.

**VirusTotal**
Free online service that analyzes files and URLs using multiple antivirus engines to detect malware and phishing.

## W

**Watering Hole Attack**
Compromising a website commonly visited by the target to deliver malware or phishing, often combined with email lures.

**Whaling**
Phishing attack specifically targeting high-level executives (C-suite) in an organization.

**Whitelist**
List of approved senders, domains, or IP addresses that bypass email filtering.

## X

**XSS (Cross-Site Scripting)**
Web vulnerability that can be exploited in phishing attacks to inject malicious scripts into legitimate websites.

## Z

**Zero-Day**
Previously unknown vulnerability exploited in attacks, sometimes used in highly sophisticated phishing campaigns.

**Zero-Trust Security**
Security model that requires verification for every access request, treating all emails as potentially malicious until verified.

---

## Common Abbreviations

- **2FA**: Two-Factor Authentication
- **APT**: Advanced Persistent Threat
- **BEC**: Business Email Compromise
- **CISO**: Chief Information Security Officer
- **DKIM**: DomainKeys Identified Mail
- **DMARC**: Domain-based Message Authentication, Reporting and Conformance
- **DNS**: Domain Name System
- **GDPR**: General Data Protection Regulation
- **GTM**: Google Tag Manager
- **HTTPS**: Hypertext Transfer Protocol Secure
- **IOC**: Indicator of Compromise
- **IP**: Internet Protocol
- **MFA**: Multi-Factor Authentication
- **OWASP**: Open Web Application Security Project
- **QR**: Quick Response (code)
- **S3**: Simple Storage Service (AWS)
- **SMTP**: Simple Mail Transfer Protocol
- **SPF**: Sender Policy Framework
- **SSL**: Secure Sockets Layer
- **TLD**: Top-Level Domain
- **TLS**: Transport Layer Security
- **URL**: Uniform Resource Locator
- **XSS**: Cross-Site Scripting

---

## Phishing Types Quick Reference

| Type | Description | Example |
|------|-------------|---------|
| **Phishing** | Generic mass email attack | "Your PayPal account needs verification" |
| **Spear Phishing** | Targeted at specific person/organization | "Hi John, regarding the merger discussion..." |
| **Whaling** | Targeting executives | Fake email from board member to CEO |
| **Clone Phishing** | Resending legitimate email with malicious changes | Re-sending real invoice with changed payment details |
| **Smishing** | SMS/text message phishing | "Your package delivery failed. Click: http://..." |
| **Vishing** | Voice/phone phishing | Call claiming to be from bank's fraud department |
| **Quishing** | QR code phishing | QR code on fake parking ticket |
| **BEC** | Business email compromise | CEO requesting urgent wire transfer |
| **Angler Phishing** | Through social media | Fake customer support accounts on Twitter |
| **Search Engine Phishing** | Fake sites in search results | Paid ads for fake "PayPal login" |

---

## Attack Vectors

| Vector | Delivery Method | Goal |
|--------|----------------|------|
| **Credential Harvesting** | Fake login page | Steal usernames/passwords |
| **Malware Delivery** | Malicious attachment | Install ransomware, keylogger, trojan |
| **Link-Based** | Malicious URL in email | Redirect to phishing site or exploit |
| **Attachment-Based** | PDF, Office doc, ZIP file | Execute malware when opened |
| **QR Code** | Image with embedded QR | Hide malicious URL from inspection |
| **Social Engineering** | Conversational manipulation | Extract info through dialogue |
| **BEC/Wire Fraud** | Impersonation | Trick into transferring money |

---

*This glossary covers terms used in phishing analysis, email security, and defensive security training.*

*Last updated: January 6, 2026*
