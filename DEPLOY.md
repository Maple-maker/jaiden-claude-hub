# Deploying / auto-updating the hub

You have two paths. Pick one.

## Option A — Git auto-deploy (most "set it and forget it")
1. Put this `site/` folder in a GitHub repo (one time).
2. In Netlify: Add new site → Import from Git → pick the repo → publish dir = `/`.
3. From now on, every push to the repo auto-deploys. "Update the site" = commit + push.
   - In Cowork, I can regenerate `site/` and commit+push for you whenever content changes
     (you'd connect the repo + give push access once).

## Option B — One-command deploy from your Mac (no Git)
One-time:
    npm install -g netlify-cli
    netlify login
    cd "path/to/Instagram Content/site"
    netlify link        # choose the existing drag-and-drop site, or create one
Then any time:
    ./deploy.sh         # re-uploads the whole folder, live in ~10s

## Keeping it fresh automatically
- I (Cowork) regenerate this `site/` folder whenever we add posts/guides — that part is automatic.
- A scheduled task can rebuild the site on a cadence (e.g., weekly) so it's always ready to push.
- The actual upload runs Netlify-side (Option A) or on your Mac (Option B), because this
  workspace can't reach Netlify's servers directly.

## To schedule a weekly auto-deploy on your Mac (Option B)
Add a cron entry (runs Mondays 7am):
    0 7 * * 1  cd "/path/to/Instagram Content/site" && ./deploy.sh >> deploy.log 2>&1
