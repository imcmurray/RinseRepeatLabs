---
title: "GuardScan Privacy Policy"
date: 2026-02-22
draft: false
---

**Last Updated:** February 28, 2026

## Overview

GuardScan ("the Service") is a website security scanning tool operated by Rinse Repeat Labs. This privacy policy explains how we collect, use, and protect information when you use GuardScan at guardscan.dev, including when you use optional beta access codes to unlock additional features.

We are committed to protecting your privacy and being transparent about the data we handle.

## Data We Collect

### Scan Data

When you submit a URL for scanning, we collect and store:

- The domain name or URL you submit for scanning
- The scan results, including security grades and scores for HTTP headers, SSL/TLS, DNS, cookies, CORS policies, technology detection, and mixed content
- A timestamp of when the scan was performed
- The duration of the scan

This data is stored to generate shareable report URLs and to display scan results. Scan results are publicly accessible via their unique report URL.

### Beta Access Data

If you use a beta access code, we store the following data associated with your code:

- The access code string, its tier, and creation/expiry dates
- Your scans are linked to your access code (enabling scan history)
- Feedback submissions (rating and optional comment) linked to your access code

If you voluntarily subscribe via the beta subscribe feature, we also store:

- Your email address, linked to your access code

### Cached Results

Scans may return cached results from a recent scan of the same domain performed by any user, within a short cooldown window. When a cached result is returned, no new data is collected or stored.

### Server Logs

Our hosting infrastructure may automatically collect:

- Your IP address (used for rate limiting to prevent abuse)
- Request timestamps
- Browser user-agent string

IP addresses used for rate limiting are held in memory only and are not persisted to any database or log file.

### What We Do Not Collect

- We do not require account creation or registration
- We do not collect email addresses unless you voluntarily provide one as a beta subscriber
- We do not use cookies for tracking purposes
- We do not use analytics services, advertising networks, or third-party tracking technologies

## How We Use Data

Scan data is used solely to:

- Display scan results to you and anyone you share the report link with
- Generate OpenGraph preview images when report links are shared on social media
- Display an aggregate scan counter on the homepage
- Provide scan history to beta users for domains they have scanned

Beta access data (including email, if provided) is used solely to:

- Authenticate and rate-limit your access to beta features
- Contact you about GuardScan updates (only if you provided an email)

Feedback data is used to improve the Service.

We do not sell, rent, or share your data with third parties.

## Data Security

- All connections to guardscan.dev are encrypted via HTTPS/TLS
- The Service is hosted on Railway with managed PostgreSQL, which provides infrastructure-level encryption
- Traffic is proxied through Cloudflare, which provides DDoS protection and a web application firewall

## Data Retention

- Scan results are retained indefinitely to keep shareable report URLs functional
- Rate limiting data (IP addresses) is held in memory only and cleared on service restart
- Beta access codes and associated email addresses are retained for the lifetime of the code (up to 30 days from creation, or until manually revoked)
- Feedback data (ratings and comments) is retained indefinitely alongside the scan results they relate to

## Third-Party Services

The Service integrates with the following third-party services:

- **Cloudflare** — DNS, CDN, and security (subject to [Cloudflare's Privacy Policy](https://www.cloudflare.com/privacypolicy/))
- **Railway** — Application and database hosting (subject to [Railway's Privacy Policy](https://railway.app/legal/privacy))

When you scan a website, GuardScan makes outbound connections to the target domain to check HTTP headers, SSL/TLS certificates, DNS records, cookies, CORS policies, technologies, and mixed content. These connections are made from our servers, not from your browser.

## Children's Privacy

The Service does not knowingly collect personal information from children under 13. If we learn that we have collected personal information from a child under 13, we will take steps to delete that information promptly.

## Your Rights

You may:

- Choose not to use the Service at any time
- Contact us to request removal of specific scan results
- Request deletion of your email address from a beta access code
- Request deletion of feedback you have submitted

## Changes to This Policy

We may update this privacy policy from time to time. Changes will be reflected by updating the "Last Updated" date at the top of this page.

## Contact

If you have questions about this privacy policy, contact us at:

**Email:** {{< email >}}
**Website:** [rinserepeatlabs.com](https://rinserepeatlabs.com)
