# Rinse Repeat Labs Website

A professional Hugo static website for Rinse Repeat Labs, a software development company specializing in mobile, web, and desktop applications.

## Features

- Modern, minimalist design with Tailwind CSS
- Dark/light mode toggle with system preference detection
- Responsive, mobile-first layout
- SEO optimized with meta tags and Open Graph support
- Formspree integration for contact forms
- Stripe integration for consultation payments
- GitHub Pages deployment via GitHub Actions

## Quick Start

### Prerequisites

1. **Hugo Extended** (v0.121.0 or later)

   ```bash
   # macOS (Homebrew)
   brew install hugo

   # Windows (Chocolatey)
   choco install hugo-extended

   # Linux (Snap)
   snap install hugo --channel=extended
   ```

2. **Node.js** (v18 or later)

   ```bash
   # Verify installation
   node --version
   npm --version
   ```

### Local Development

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/RinseRepeatLabs.git
   cd RinseRepeatLabs
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   hugo server -D
   ```

4. Open http://localhost:1313 in your browser.

## Configuration

### Site Settings

Edit `config.toml` to customize:

```toml
[params]
  email = "rinserepeatlabs@gmail.com"
  consultationFee = "$199"
  formspreeEndpoint = "YOUR_FORMSPREE_ENDPOINT"
  stripePaymentLink = "YOUR_STRIPE_PAYMENT_LINK"

[params.social]
  twitter = "yourtwitterhandle"
  linkedin = "yourcompanyname"
  github = "yourgithubname"
```

### Formspree Setup

1. Go to [Formspree.io](https://formspree.io) and create a free account
2. Create a new form
3. Copy the form ID (the part after `/f/` in the endpoint URL)
4. Update `config.toml`:

   ```toml
   formspreeEndpoint = "xyzabcde"  # Your form ID
   ```

### Stripe Payment Link Setup

1. Log in to your [Stripe Dashboard](https://dashboard.stripe.com)
2. Go to **Products** → **Payment Links**
3. Create a new payment link for $199
4. Copy the payment link URL
5. Update `config.toml`:

   ```toml
   stripePaymentLink = "https://buy.stripe.com/your-link-id"
   ```

## Content Management

### Portfolio Projects

Add new portfolio items by creating markdown files in `content/portfolio/`:

```markdown
---
title: "Project Name"
tagline: "Brief description of the project"
platforms: ["iOS", "Android", "Web"]
tech: ["React Native", "Node.js", "PostgreSQL"]
featured: true
weight: 1
year: "2024"
client: "Client Name"
image: "https://images.unsplash.com/photo-xxxxx"
appStoreUrl: "https://apps.apple.com/..."
playStoreUrl: "https://play.google.com/..."
testimonial:
  quote: "Client testimonial here"
  author: "Client Name"
  role: "CEO, Company"
---

## Overview

Project description...
```

### Pages

- **Home**: `content/_index.md` (layout in `layouts/index.html`)
- **Services**: `content/services.md`
- **Portfolio**: `content/portfolio/_index.md`
- **About**: `content/about.md`
- **Submit Idea**: `content/submit-idea.md`

## Deployment

### GitHub Pages (Recommended)

1. Push your code to GitHub
2. Go to **Settings** → **Pages**
3. Set **Source** to "GitHub Actions"
4. The site will deploy automatically on push to `main`

### Custom Domain Setup

1. In your DNS provider, add:
   - **A records** pointing to GitHub Pages IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - Or a **CNAME record** pointing to `yourusername.github.io`

2. In GitHub repo settings, add your custom domain

3. Update `config.toml`:

   ```toml
   baseURL = "https://rinserepeatlabs.com/"
   ```

## File Structure

```
RinseRepeatLabs/
├── .github/workflows/    # GitHub Actions deployment
├── assets/css/           # Tailwind CSS source
├── content/              # Markdown content
│   ├── portfolio/        # Portfolio items
│   └── *.md              # Pages
├── layouts/              # Hugo templates
│   ├── _default/         # Default layouts
│   ├── partials/         # Reusable components
│   └── */                # Section-specific layouts
├── static/               # Static assets
├── config.toml           # Hugo configuration
├── package.json          # npm dependencies
├── tailwind.config.js    # Tailwind configuration
└── postcss.config.js     # PostCSS configuration
```

## Customization

### Colors

Edit `tailwind.config.js` to change the primary color palette:

```javascript
theme: {
  extend: {
    colors: {
      primary: {
        500: '#0ea5e9',  // Main primary color
        600: '#0284c7',  // Darker shade
        // ... other shades
      },
    },
  },
},
```

### Fonts

The site uses Inter font by default. To change, edit:
- `tailwind.config.js` (fontFamily)
- `assets/css/main.css` (Google Fonts import)

### Adding New Sections

1. Create a new markdown file in `content/`
2. Add front matter with layout specification
3. Create corresponding layout in `layouts/`
4. Add to menu in `config.toml`

## Troubleshooting

### Build Errors

- Ensure you have Hugo Extended (not regular Hugo)
- Run `npm install` to install dependencies
- Check for syntax errors in templates

### Tailwind Not Loading

- Verify `postcss.config.js` exists
- Check that all files are in correct directories
- Run `npm install` again

### Form Not Submitting

- Verify Formspree endpoint is correct
- Check browser console for errors
- Ensure form fields have `name` attributes

## License

This project is proprietary to Rinse Repeat Labs.

## Support

For questions or issues, contact: rinserepeatlabs@gmail.com
