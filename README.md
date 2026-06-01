# StackTrim

Paste your subscriptions, get cheaper alternatives, and a simple cancel/downgrade plan. Runs entirely in the browser — no account required.

## Deploy on Vercel (recommended)

Vercel scans for `app.py` and expects `app = Flask(...)`. This repo includes:

- **`vercel.json`** — serves `index.html` as a static site
- **`.vercelignore`** — excludes `app.py` so Vercel uses static mode (no Python error)

Push to GitHub and import the repo in Vercel. No start command needed.

If you remove `.vercelignore`, `app.py` is a valid Flask app Vercel can run instead.

## Share it (other hosts)

1. Host the folder (GitHub Pages, Netlify Drop, Cloudflare Pages):
   - **GitHub Pages:** repo → Settings → Pages → deploy from `main` / root → your site is `https://<user>.github.io/<repo>/`
2. Send people the link. They paste from iPhone **Settings → Subscriptions**, bank app, or a notes list.

## Free vs Pro

| | Free | Pro ($9 one-time) |
|---|------|-------------------|
| Subscriptions tracked | 8 | Unlimited |
| Paste import | Up to 6 per paste | Unlimited |
| Quick-add chips | ✓ | ✓ |
| Alternatives & swap list | ✓ | ✓ |
| Copy report | ✓ | ✓ |
| CSV import, download, JSON backup | — | ✓ |

**Monetization setup:** In `index.html`, set `PRO_CHECKOUT_URL` to your Stripe Payment Link or Gumroad URL. After purchase, give customers unlock code `STACKTRIM-PRO` (stored in browser localStorage).

For testing: **Pro** modal → “I already paid / unlock” → code `demo` or `STACKTRIM-PRO`.

## Privacy

Data stays in `localStorage` on the user’s device. No backend in this version.

## Local preview

**Static (simplest):**

```bash
cd /path/to/StackTrimAi
python3 -m http.server 8080
# open http://localhost:8080
```

**Python host (Railway, Render, Heroku):** `app.py` exposes `app` for gunicorn. Start command:

```bash
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:8080
```

Or use the included `Procfile` on platforms that read it.
