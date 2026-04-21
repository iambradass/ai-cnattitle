# AGENTS.md

## Project Overview
- Static HTML pages: `ai-hub-landing.html`, `community.html`.
- Static hosting entry/wrapper pages: `index.html`, `vault-hosted.html`.

## Workflows
- No preview tooling or config found in repo; pages appear to be opened directly in a browser.
- `index.html` is a static redirect shell (meta refresh) that forwards root traffic to `ai-hub-landing.html`.
- `the-vault.html` appears to be a standalone page version for direct browser viewing.
- `the vault/The Vault.html` is a self-contained GHL Custom HTML embed; paste the full file into a GoHighLevel Custom HTML element.
- `the vault/The Vault.live-20260316.html` is the live-synced Vault source used by `vault-hosted.html` for the `/the-vault` hosted route.
- `vault-hosted.html` renders the live Vault through an iframe using a URL-encoded path (`./the%20vault/The%20Vault.live-20260316.html`); if the live source filename changes, update this iframe `src`.
- Supporting Vault source documents are stored in `the vault/` (`AI_Tool_Vault_Playbook.xlsx`, `KeepingAIonThings_Vault_Expanded_Notes.md`) and can be referenced when updating Vault copy/content.
- Before editing `the vault/The Vault.html`, create a timestamped backup in `the vault/` to preserve a rollback point.
- `the vault/` keeps timestamped backup copies of The Vault HTML (e.g., `The Vault.backup-YYYYMMDD-*.html`).
- The live-synced Vault source also has targeted backup snapshots (e.g., `The Vault.live-20260316.backup-20260325-overflow-fix.html`) for hosted-route fixes.
- Backup filenames in `the vault/` also include change-focused suffixes (for example `*-mobile-fix.html`, `*-ghl-center-fix.html`), suggesting snapshots are kept before/after targeted embed edits.
- Backup snapshots also include GHL rollout checkpoints like `*-pre-ghl-embed.html` and `*-ghl-center-revert-breakout.html`, indicating iterative embed/layout troubleshooting.
- `the vault/The Vault.backup-20260316-pre-live-sync.html` is present as a zero-byte checkpoint; verify snapshot size before using any backup for rollback.
- Hosted-route wiring is split across platform config files: `vercel.json` (Vercel rewrites) and `.htaccess` (Apache/Hostinger rewrites).

## Commands
- Open standalone pages directly in browser: `open ai-hub-landing.html`, `open community.html`, `open the-vault.html`.
- Open static-hosting entry/wrapper pages for local validation: `open index.html`, `open vault-hosted.html`.
- Confirm root redirect wiring in the static entry page: `open index.html` (or inspect with `rg "meta http-equiv=\"refresh\"|ai-hub-landing.html" index.html`).
- Open the GHL embed source locally for validation before pasting: `open "the vault/The Vault.html"`.
- Open the live-synced hosted Vault source used by the wrapper route: `open "the vault/The Vault.live-20260316.html"`.
- Verify hosted-wrapper iframe target path before/after Vault source renames: `rg "The%20Vault.live-20260316.html|iframe src" vault-hosted.html`.
- Open Vault source-content documents used for copy/reference updates: `open "the vault/AI_Tool_Vault_Playbook.xlsx"`, `open "the vault/KeepingAIonThings_Vault_Expanded_Notes.md"`.
- Open external host/routing context before changing wrappers or hosted-route wiring: `open EXTERNAL_HOSTING_NOTES.md`.
- Open hosting rewrite configs when changing route behavior: `open vercel.json`, `open .htaccess`.
- Create a timestamped Vault backup before edits: `cp "the vault/The Vault.html" "the vault/The Vault.backup-$(date +%Y%m%d-%H%M%S).html"`.
- List Vault backup snapshots: `ls "the vault"/The\ Vault.backup-*.html`.
- Create a timestamped backup before editing the live-synced hosted Vault source: `cp "the vault/The Vault.live-20260316.html" "the vault/The Vault.live-20260316.backup-$(date +%Y%m%d-%H%M%S).html"`.
- List live-source backup snapshots: `ls "the vault"/The\ Vault.live-20260316.backup-*.html`.
- Check for empty/invalid Vault backup snapshots before rollback use: `find "the vault" -maxdepth 1 -name "The Vault*.html" -size 0`.
- TODO: Document formatting or linting commands once identified (none found in repo).
