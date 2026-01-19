# Formspree Setup and Integration Guide

This guide covers how to set up and integrate Formspree for form processing on the Rinse Repeat Labs website.

## What is Formspree?

Formspree is a form backend service that handles form submissions for static websites. When a user submits a form, Formspree receives the data, sends you an email notification, and stores the submission in your dashboard.

## Creating a Formspree Account

1. Go to [formspree.io](https://formspree.io) and click **Get Started**
2. Sign up with your email or GitHub account
3. Verify your email address

## Creating a Form

1. Log in to your Formspree dashboard
2. Click **+ New Form**
3. Give your form a name (e.g., "Submit Idea Form" or "Tester Application")
4. Copy the **Form ID** - this is the part after `/f/` in the endpoint URL
   - Example: If the endpoint is `https://formspree.io/f/xyzabcde`, the Form ID is `xyzabcde`

### Multiple Forms

You may want separate forms for different purposes:
- **Submit Idea Form** - For project submissions (`HUGO_FORMSPREE_ENDPOINT`)
- **Tester Application Form** - For tester signups (`HUGO_FORMSPREE_TESTER_ENDPOINT`)

Create a separate form in Formspree for each, and note the Form IDs.

## Hugo Integration

### How It Works

Forms in the Hugo templates use this pattern:

```html
<form action="https://formspree.io/f/{{ getenv "HUGO_FORMSPREE_ENDPOINT" | default .Site.Params.formspreeEndpoint }}" method="POST">
  <!-- form fields -->
</form>
```

This checks for an environment variable first (`HUGO_FORMSPREE_ENDPOINT`), then falls back to the config value.

### Form Locations

| Form | Template File | Environment Variable |
|------|--------------|---------------------|
| Submit Idea | `layouts/submit-idea/single.html` | `HUGO_FORMSPREE_ENDPOINT` |
| Become a Tester | `layouts/become-a-tester/single.html` | `HUGO_FORMSPREE_TESTER_ENDPOINT` |

## Configuration

### Local Development

For local testing, uncomment and set values in `config.toml`:

```toml
[params]
  # For local dev, uncomment and set values below:
  formspreeEndpoint = "your-test-form-id"
  # formspreeEndpoint = "xyzabcde"
```

**Tip:** Create a separate "test" form in Formspree for development to avoid mixing test submissions with real ones.

### Production (GitHub Actions)

For production builds, the Form ID is injected via GitHub repository secrets:

1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the following secrets:

| Secret Name | Value |
|-------------|-------|
| `HUGO_FORMSPREE_ENDPOINT` | Your main form ID (e.g., `xyzabcde`) |
| `HUGO_FORMSPREE_TESTER_ENDPOINT` | Your tester form ID (optional) |

The GitHub Actions workflow (`.github/workflows/hugo.yml`) passes these to Hugo at build time:

```yaml
- name: Build with Hugo
  env:
    HUGO_FORMSPREE_ENDPOINT: ${{ secrets.HUGO_FORMSPREE_ENDPOINT }}
```

## Form Field Requirements

Each form input must have a `name` attribute for Formspree to capture it:

```html
<!-- Good - has name attribute -->
<input type="text" name="full_name" required>

<!-- Bad - missing name attribute, won't be captured -->
<input type="text" required>
```

### Special Field Names

Formspree recognizes certain field names:

| Field Name | Purpose |
|------------|---------|
| `email` | Used as reply-to address in notifications |
| `name` | Sender name in notifications |
| `_subject` | Custom email subject line |
| `_replyto` | Alternative to `email` for reply-to |
| `_next` | Redirect URL after submission |

### Hidden Fields

You can add hidden fields for additional data:

```html
<input type="hidden" name="_subject" value="New Project Submission">
<input type="hidden" name="form_source" value="submit-idea-page">
```

## Formspree Dashboard Features

### Submissions

View all form submissions in the Formspree dashboard:
- See submission details and timestamps
- Export submissions as CSV
- Delete individual submissions

### Email Notifications

Configure where submissions are sent:
1. Go to your form in Formspree
2. Click **Settings** → **Email**
3. Add notification email addresses

### Spam Protection

Formspree includes built-in spam protection:
- **reCAPTCHA** - Enable in form settings
- **Honeypot field** - Add a hidden field that bots fill out:

```html
<input type="text" name="_gotcha" style="display:none">
```

### Plugins (Paid Plans)

Paid Formspree plans offer integrations:
- Google Sheets
- Slack notifications
- Webhooks
- Zapier

## Testing Forms

### Local Testing

1. Set `formspreeEndpoint` in `config.toml`
2. Run `hugo server -D`
3. Submit the form
4. Check your Formspree dashboard for the submission

### Production Testing

After deploying:
1. Visit the live form page
2. Submit with test data
3. Verify you receive the email notification
4. Check the Formspree dashboard

## Troubleshooting

### Form Not Submitting

1. **Check the browser console** for JavaScript errors
2. **Verify the Form ID** is correct in config or environment variables
3. **Ensure all required fields** have `name` attributes
4. **Check Formspree dashboard** for any form-specific issues

### Not Receiving Emails

1. Check spam/junk folder
2. Verify email address in Formspree settings
3. Check Formspree dashboard - submissions may be there but email failed

### Submissions Not Appearing

1. Confirm the Form ID matches your Formspree form
2. Check if the form action URL is correct in the rendered HTML
3. Test with browser developer tools Network tab to see the POST request

### Environment Variable Not Working

1. Verify the secret name matches exactly (case-sensitive)
2. Check the GitHub Actions workflow logs for build errors
3. Ensure the secret is set at the repository level, not environment level

## Free vs Paid Plans

| Feature | Free | Paid |
|---------|------|------|
| Submissions/month | 50 | 1,000+ |
| Forms | 2 | Unlimited |
| Email notifications | Yes | Yes |
| File uploads | No | Yes |
| Integrations | No | Yes |
| Custom redirect | Yes | Yes |
| AJAX submissions | Yes | Yes |

For most small business sites, the free plan is sufficient to start.

## Resources

- [Formspree Documentation](https://help.formspree.io/)
- [Formspree AJAX Guide](https://help.formspree.io/hc/en-us/articles/360013470814-Submit-forms-with-JavaScript-AJAX-)
- [Hugo Environment Variables](https://gohugo.io/functions/os/getenv/)
