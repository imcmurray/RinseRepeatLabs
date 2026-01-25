# Cloudflare Security Setup for Rinse Repeat Labs

This guide explains how to configure Cloudflare WAF (Web Application Firewall) custom rules to protect the Rinse Repeat Labs website from malicious traffic and unauthorized endpoint access.

## Overview

The "Block Invalid Endpoints" strategy uses a **whitelist approach** to security. Instead of trying to block known bad paths (which attackers constantly change), we define all legitimate paths and block everything else. This significantly reduces the attack surface.

## Prerequisites

- Cloudflare account with the website added
- Access to Cloudflare Dashboard → Security → WAF → Custom Rules
- Knowledge of all valid endpoints on your website

## Custom Rule Configuration

### Rule: Block Invalid Endpoints

**Purpose:** Block all requests to paths that don't match known valid endpoints.

**Rule Name:** `Block invalid endpoints`

**Action:** Block

**Priority:** First (ensures this rule runs before other rules)

### Expression (Copy/Paste Ready)

```
not (
    http.request.uri.path eq "/" or
    http.request.uri.path in {"/about/" "/portfolio/" "/services/" "/terms/" "/privacy/" "/become-a-tester/" "/submit-idea/"} or
    http.request.uri.path in {"/fevertap/" "/fevertap/privacy-policy/"} or
    http.request.uri.path in {"/robots.txt" "/sitemap.xml" "/index.xml" "/index.json" "/404.html"} or
    http.request.uri.path in {"/favicon.svg" "/favicon.ico" "/apple-touch-icon.png" "/favicon-16x16.png" "/favicon-32x32.png"} or
    starts_with(http.request.uri.path, "/portfolio/") or
    starts_with(http.request.uri.path, "/fevertap/") or
    starts_with(http.request.uri.path, "/images/") or
    starts_with(http.request.uri.path, "/css/") or
    starts_with(http.request.uri.path, "/js/") or
    starts_with(http.request.uri.path, "/fonts/") or
    starts_with(http.request.uri.path, "/assets/")
)
```

## Step-by-Step Setup

### 1. Navigate to Custom Rules

1. Log in to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Select your website (e.g., `rinserepeatlabs.com`)
3. Go to **Security** → **WAF** → **Custom rules**
4. Click **Create rule**

### 2. Configure the Rule

| Field | Value |
|-------|-------|
| Rule name | `Block invalid endpoints` |
| When incoming requests match... | *(paste expression above)* |
| Then take action | `Block` |
| Place at | `First` |

### 3. Deploy the Rule

1. Click **Deploy** to activate the rule immediately
2. Monitor the **Security Events** dashboard for blocked requests

## Understanding the Expression

### Path Types Explained

| Pattern Type | Example | Description |
|--------------|---------|-------------|
| Exact match | `http.request.uri.path eq "/"` | Matches only the homepage |
| List match | `http.request.uri.path in {"/about/" "/terms/"}` | Matches any path in the list |
| Prefix match | `starts_with(http.request.uri.path, "/portfolio/")` | Matches all paths starting with `/portfolio/` |

### Why Use `not`?

The entire expression is wrapped in `not (...)`. This inverts the logic:
- **Without `not`**: Block matching requests (blocklist approach)
- **With `not`**: Block requests that DON'T match (allowlist approach)

The allowlist approach is more secure because it blocks unknown/new attack vectors automatically.

## Customizing for Your Site

### Adding New Pages

When you add new content pages, update the expression:

```diff
  http.request.uri.path in {"/about/" "/portfolio/" "/services/" "/terms/" "/privacy/" "/become-a-tester/" "/submit-idea/"} or
+ http.request.uri.path eq "/new-page/" or
```

### Adding New Sections

For new content sections with multiple subpages:

```diff
  starts_with(http.request.uri.path, "/portfolio/") or
+ starts_with(http.request.uri.path, "/blog/") or
```

### Adding API Endpoints

If you add API functionality:

```diff
  starts_with(http.request.uri.path, "/assets/") or
+ starts_with(http.request.uri.path, "/api/")
```

## Valid Endpoints Reference

### Content Pages

| Path | Description |
|------|-------------|
| `/` | Homepage |
| `/about/` | About page |
| `/portfolio/` | Portfolio listing |
| `/portfolio/*` | Individual portfolio items |
| `/services/` | Services page |
| `/terms/` | Terms of service |
| `/privacy/` | Privacy policy |
| `/become-a-tester/` | Beta tester signup |
| `/submit-idea/` | Idea submission form |
| `/fevertap/` | FeverTap app section |
| `/fevertap/privacy-policy/` | FeverTap privacy policy |

### Static Assets

| Path Pattern | Description |
|--------------|-------------|
| `/images/*` | Image assets |
| `/css/*` | Stylesheets |
| `/js/*` | JavaScript files |
| `/fonts/*` | Web fonts |
| `/assets/*` | Other static assets |

### Standard Files

| Path | Description |
|------|-------------|
| `/robots.txt` | Search engine directives |
| `/sitemap.xml` | XML sitemap |
| `/index.xml` | RSS feed |
| `/index.json` | JSON index (if used) |
| `/404.html` | Error page |
| `/favicon.*` | Browser icons |

## Monitoring & Maintenance

### Review Blocked Requests

1. Go to **Security** → **Events**
2. Filter by rule name: `Block invalid endpoints`
3. Review blocked paths for:
   - Legitimate paths that need to be added
   - Attack patterns (SQL injection, path traversal, etc.)

### Common False Positives

If legitimate requests are being blocked:

1. Check the blocked path in Security Events
2. Determine if it's a valid endpoint
3. Update the expression to include the path
4. Save and redeploy the rule

### Recommended Review Schedule

- **Weekly**: Check Security Events for false positives
- **After deployments**: Update rule when adding new pages/sections
- **Monthly**: Audit rule against current site structure

## Additional Security Recommendations

### Complementary Rules

Consider adding these additional custom rules:

#### Block Known Bad User Agents

```
http.user_agent contains "sqlmap" or
http.user_agent contains "nikto" or
http.user_agent contains "nmap"
```

#### Rate Limiting (Contact Forms)

Create a rate limiting rule for form endpoints to prevent spam:
- Path: `/submit-idea/` or `/become-a-tester/`
- Rate: 5 requests per 10 seconds
- Action: Block

### Enable Additional Cloudflare Features

| Feature | Location | Recommendation |
|---------|----------|----------------|
| Bot Fight Mode | Security → Bots | Enable |
| Browser Integrity Check | Security → Settings | Enable |
| Hotlink Protection | Scrape Shield | Enable |
| Email Obfuscation | Scrape Shield | Enable |
| SSL/TLS | SSL/TLS → Overview | Full (Strict) |

## Troubleshooting

### Rule Not Blocking Requests

1. Verify rule is deployed (not in draft mode)
2. Check rule order (should be "First")
3. Test with a known invalid path

### Legitimate Traffic Being Blocked

1. Check Security Events for the blocked request
2. Verify the path format (trailing slashes matter)
3. Add the path to the allowlist expression
4. Redeploy the rule

### Testing the Rule

Use `curl` to test:

```bash
# Should be allowed
curl -I https://rinserepeatlabs.com/about/

# Should be blocked
curl -I https://rinserepeatlabs.com/wp-admin/
curl -I https://rinserepeatlabs.com/.env
curl -I https://rinserepeatlabs.com/admin/
```

## Resources

- [Cloudflare WAF Custom Rules Documentation](https://developers.cloudflare.com/waf/custom-rules/)
- [Cloudflare Firewall Rules Expression Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)
- [Cloudflare Security Best Practices](https://developers.cloudflare.com/learning-paths/application-security/)
