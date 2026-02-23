---
title: "GuardScan Privacy Policy"
date: 2026-02-22
draft: false
---

**Last Updated:** February 2026

## Overview

GuardScan ("the Service") is a free website security scanning tool operated by Rinse Repeat Labs. This privacy policy explains how we collect, use, and protect information when you use GuardScan at guardscan.dev.

We are committed to protecting your privacy and being transparent about the data we handle.

## Data We Collect

### Scan Data

When you submit a URL for scanning, we collect and store:

- The domain name or URL you submit for scanning
- The scan results, including security grades and scores
- A timestamp of when the scan was performed

This data is stored to generate shareable report URLs and to display scan results. Scan results are publicly accessible via their unique report URL.

### Server Logs

Our hosting infrastructure may automatically collect:

- Your IP address (used for rate limiting to prevent abuse)
- Request timestamps
- Browser user-agent string

IP addresses used for rate limiting are held in memory only and are not persisted to any database or log file.

### What We Do Not Collect

- We do not require account creation or registration
- We do not collect names, email addresses, or other personal identifiers
- We do not use cookies for tracking purposes
- We do not use analytics services, advertising networks, or third-party tracking technologies

## How We Use Data

Scan data is used solely to:

- Display scan results to you and anyone you share the report link with
- Generate OpenGraph preview images when report links are shared on social media
- Display an aggregate scan counter on the homepage

We do not sell, rent, or share your data with third parties.

## Data Security

- All connections to guardscan.dev are encrypted via HTTPS/TLS
- The Service is hosted on Railway with managed PostgreSQL, which provides infrastructure-level encryption
- Traffic is proxied through Cloudflare, which provides DDoS protection and a web application firewall

## Data Retention

- Scan results are retained indefinitely to keep shareable report URLs functional
- Rate limiting data (IP addresses) is held in memory only and cleared on service restart

## Third-Party Services

The Service integrates with the following third-party services:

- **Cloudflare** — DNS, CDN, and security (subject to [Cloudflare's Privacy Policy](https://www.cloudflare.com/privacypolicy/))
- **Railway** — Application and database hosting (subject to [Railway's Privacy Policy](https://railway.app/legal/privacy))

When you scan a website, GuardScan makes outbound connections to the target domain to check HTTP headers, SSL/TLS certificates, DNS records, and cookies. These connections are made from our servers, not from your browser.

## Children's Privacy

The Service does not knowingly collect personal information from children under 13. The Service requires no account creation and collects no personal identifiers.

## Your Rights

You may:

- Choose not to use the Service at any time
- Contact us to request removal of specific scan results

## Changes to This Policy

We may update this privacy policy from time to time. Changes will be reflected by updating the "Last Updated" date at the top of this page.

## Contact

If you have questions about this privacy policy, contact us at:

**Email:** {{< email >}}
**Website:** [rinserepeatlabs.com](https://rinserepeatlabs.com)
