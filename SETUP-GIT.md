# Option A — Git → Netlify continuous deploy (one-time setup)

Do this once on your Mac. After it's done, every change auto-deploys.

## 1. Open Terminal in the site folder
    cd ~/Desktop/AEGIS/40-CONTENT/Instagram\ Content/site
    rm -rf .git          # clears the partial repo created in the cloud sandbox

## 2. Make it a fresh repo
    git init
    git add -A
    git commit -m "Claude guides hub"

## 3. Create the GitHub repo and push
Easiest (GitHub CLI):
    brew install gh          # if you don't have it
    gh auth login
    gh repo create jaiden-claude-hub --public --source=. --push

Or manually: create an empty repo at github.com, then:
    git remote add origin https://github.com/<you>/jaiden-claude-hub.git
    git branch -M main
    git push -u origin main

## 4. Connect Netlify (one time)
- netlify.com → Add new site → Import an existing project → GitHub → pick the repo
- Build command: (leave blank)   Publish directory: .
- Deploy.

## Done. From now on:
Every push to the repo auto-deploys. "Update the site" = commit + push.

### How I (Cowork) keep it updated for you
When we add posts/guides, I regenerate the `site/` files here. To publish, either:
- you run:  `git add -A && git commit -m "update" && git push`  (3 seconds), or
- give me push access (a GitHub repo URL + token) and I'll commit + push from here —
  GitHub is reachable from this workspace, so I can do the push; Netlify deploys the rest.
