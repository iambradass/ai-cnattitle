# External Hosting Notes

## Source of truth
- As of March 16, 2026, `https://ai.cnattitle.com` is the active live GHL host for the AI Hub.
- The live Vault page is `https://ai.cnattitle.com/the-vault`.
- The newest synced local Vault source in this workspace is `/the vault/The Vault.live-20260316.html`, extracted from the live `ai.cnattitle.com/the-vault` page on March 16, 2026.
- The older local `/the vault/The Vault.html` snapshot is not the newest source of truth anymore.
- The root-level `/the-vault.html` is older and should not be treated as the latest Vault build.
- `/ai-hub-landing.html` and `/community.html` are already standalone static pages and do not depend on GHL.

## Live site findings
- On March 16, 2026, `https://ai.cnattitle.com/` served the AI Hub page and matched the local `ai-hub-landing.html` structure.
- On March 16, 2026, `https://ai.cnattitle.com/community` redirected back to `/`, so Community was not live on the GHL host at that time.
- On March 16, 2026, `https://ai.cnattitle.com/the-vault` served a 47-item Vault page.
- The live Vault included a `BP Custom Tools` filter and a `CNAT AI Toolkit` entry, which were not present in the older local snapshot.
- The main CNAT marketing site is separately served elsewhere, but the AI Hub/Vault source of truth for this migration is the `ai.cnattitle.com` GHL host.

## Chosen migration format
- Static HTML/CSS/JS is the lowest-risk format for this project.
- Next.js is unnecessary for the current site because the AI Hub, Community page, and Vault are static documents.
- This repo now includes:
  - `index.html` as the generic static hosting entry point
  - `vault-hosted.html` as the clean hosted Vault route wrapper
  - `vercel.json` for clean Vercel routing
  - `.htaccess` for clean Hostinger routing

## Routing
- `/` -> `index.html` -> `ai-hub-landing.html`
- `/community` -> `community.html`
- `/the-vault` -> `vault-hosted.html`
- `vault-hosted.html` loads the live-synced Vault source from `/the vault/The Vault.live-20260316.html`

## Recommendation
- Use Vercel or standard static hosting first.
- Keep WordPress and GHL out of the AI Hub/Vault delivery path unless there is a hard business reason to embed them again.
