Sync my wiki and deployed configuration.

1. `git -C {{WIKI_PATH}} pull --ff-only`; then commit and push any local
   wiki changes (per its schema's sync rules).
2. `python3 {{HUB_PATH}}/tools/deploy.py --wiki {{WIKI_PATH}} check`; if
   sources changed, redeploy; if deployed copies were hand-edited, show me
   each difference and ask whether to fold it back into the source.
3. Report what moved in one short summary.
