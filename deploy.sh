#!/usr/bin/env bash
# One-command deploy of the link-in-bio hub to Netlify.
# One-time setup:
#   npm install -g netlify-cli
#   netlify login          # opens browser, authorizes
#   cd "<this site folder>" && netlify link   # pick/create the site
# After that, just run:  ./deploy.sh
set -e
SITE_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "Deploying $SITE_DIR to Netlify..."
netlify deploy --prod --dir="$SITE_DIR"
echo "Done. Your bio link is updated."
