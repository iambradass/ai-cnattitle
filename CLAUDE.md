<!-- BEGIN shared-project-workflow -->
Read `PROJECT.md` for the shared source/release/checks guide and `.agent-workflow/STATUS.md` when resuming.
Current task authorization governs deployment. Historical command examples below are not standing authorization, and unrelated edits must remain untouched.
<!-- END shared-project-workflow -->

# ai.cnattitle.com — Project Context

> **Live URLs:** https://ai.cnattitle.com (public AI hub pages) + https://internal.ai.cnattitle.com (CNAT Internal hub — tile dashboard, /admin/users, tool entitlements)
> **Repo:** `iambradass/ai-cnattitle` (branch `main`) — **must stay PUBLIC**, Hostinger auto-deploy requires it
> **Local repo:** `~/Developer/cnat-command-center/ai.cnattitle/`

---

## Deploy

- **Method:** git push to `main` → Hostinger auto-deploys in ~30-60 seconds. Use the `/deploy-ai` skill to handle commit + push.
- **After every deploy:** flush the Hostinger CDN cache — hPanel → Hosting → Cache Manager → Flush All.
- **NEVER** use FTP or Hostinger File Manager. Git push is the only deploy method.

## Host config

- **`.htaccess` is the authoritative host config.** The site is served by Hostinger (Apache); `.htaccess` owns rewrites, hosted routes, and clean URLs.
- **`vercel.json` also exists in the repo but is legacy** — leftover from earlier Vercel-hosted routing (see `EXTERNAL_HOSTING_NOTES.md`). It has no effect on the live Hostinger site. When changing route behavior, edit `.htaccess`.

## Site contents

- Static HTML pages at repo root: `ai-hub-landing.html`, `ai-toolkit.html`, `community.html`, `prompt-forge.html`, `review-request.html`, `setup.html`, `speed-to-lead.html`, `the-vault.html`, `value-builder.html`, `internal.html`, plus OG images.
- `index.html` is a static redirect shell (meta refresh) forwarding root traffic to `ai-hub-landing.html`.
- `vault-hosted.html` renders the live Vault through an iframe using a URL-encoded path (`./the%20vault/The%20Vault.live-20260316.html`); if the live source filename changes, update this iframe `src`.
- `the vault/` holds the Vault sources:
  - `The Vault.html` — self-contained GHL Custom HTML embed (paste whole file into a GHL Custom HTML element)
  - `The Vault.live-20260316.html` — live-synced source used by `vault-hosted.html` for the `/the-vault` hosted route
  - Timestamped `*.backup-*` snapshots — create one (`cp` with a `$(date +%Y%m%d-%H%M%S)` suffix) before editing either Vault file; check for zero-byte snapshots before using one for rollback
  - Reference docs: `AI_Tool_Vault_Playbook.xlsx`, `KeepingAIonThings_Vault_Expanded_Notes.md`

## Rules

- Clean URLs on internal links (no `.html` extensions) — hosted routes are wired in `.htaccess`.
- No em dashes in delivered copy (global rule).
- The internal hub's auth and tools are their own projects (see memory: `project_cnat_internal_hub_deferred.md`); this repo is the static site layer.
