# StackTrim

Paste your subscriptions, get cheaper alternatives, and a simple cancel/downgrade plan. Runs entirely in the browser — no account required.

## Deploy on Vercel

**There is no `app.py` in the project root** — Vercel deploys `index.html` as a static site.

1. Push this repo to GitHub
2. [vercel.com](https://vercel.com) → Add Project → import repo
3. Leave **Build Command** and **Install Command** empty
4. Deploy

`vercel.json` handles routing. If you still see a Python/`app.py` error, in Vercel → Settings → General set **Framework Preset** to **Other** and redeploy with cache disabled.

## Share it (other hosts)

- **GitHub Pages:** Settings → Pages → deploy from `main` / root
- **Netlify / Cloudflare Pages:** drag the folder or connect the repo (static)

## Python host (Railway / Render) — optional

Use the `server/` folder (not used by Vercel):

```bash
cd server
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:8080
```

Set the platform root directory to `server` and point static files at the parent `index.html` (or deploy the whole repo with start command from `server/`).

## Free vs Pro

| | Free | Pro ($9 one-time) |
|---|------|-------------------|
| Subscriptions tracked | 8 | Unlimited |
| Paste import | Up to 6 per paste | Unlimited |
| Quick-add chips | ✓ | ✓ |
| Alternatives & swap list | ✓ | ✓ |
| Copy report | ✓ | ✓ |
| CSV import, download, JSON backup | — | ✓ |

Set `PRO_CHECKOUT_URL` in `index.html` for your payment link. Unlock code after purchase: `STACKTRIM-PRO` (test: `demo`).

## Local preview

```bash
cd StackTrimAi
python3 -m http.server 8080
# http://localhost:8080
```
