# Keeping AI on Things - Vault Expanded Notes
Pulled from your latest Vault HTML `tools[]` list on February 12, 2026 (26 tools).
## Tool list (from the HTML)
ChatGPT, Claude, Perplexity, Google Gemini, Writor, Epique AI, Copy.ai, Midjourney, Canva, Virtual Staging AI, Collov AI, Photoroom, Opus Clip, Descript, HeyGen, Captions.ai, Luma Dream Machine, Follow Up Boss, Lofty, Ylopo, ManyChat, Otter.ai, Fathom, Notion, HouseCanary, Zapier

---

## AI Assistants
### ChatGPT

```yaml
name: ChatGPT
category: AI Assistants
pricing: Freemium
link: https://chat.openai.com
tags:
- writing
- analysis
- coding
- general
short_description: General-purpose AI assistant for writing, planning, analysis, and workflow
  drafting.
how_it_works: Chat-based AI that can draft text, summarize, and (when enabled) analyze files
  like PDFs and spreadsheets. Best results come from giving it the facts, your constraints
  (tone, length, compliance), and an exact output format.
agent_uses:
- Turn property notes into MLS description, social captions, email blast, and open-house signage
  copy.
- 'Write call/text scripts for: new lead, price drop, buyer lull, appraisal drama, "we''re
  interviewing agents."'
- Create a 30-day content calendar from your niche + 5 pillar topics (then batch the posts).
- Analyze a lead list (CSV) to segment by likely intent, then generate next-best action scripts.
- 'Draft SOPs (Standard Operating Procedures) for your team: intake -> follow-up -> appointment
  -> offer -> post-close.'
quick_demo: Paste messy listing notes + target buyer avatar -> generate (1) MLS remarks, (2)
  3 Reel hooks, (3) 5 follow-up texts.
sample_prompts:
- 'Write an MLS description from these facts. Keep it compliant (no Fair Housing landmines),
  avoid hype, include key features first, 850-1,000 chars. Facts: ...'
- 'Create 6 text messages for a new online lead: 2-minute response, 2-hour follow-up, next
  day, 3 days, 7 days, 14 days. Ask 1 qualifying question each time. Tone: friendly, direct.'
- Here is a CSV of my leads with tags and last-contact date. Segment into 4 groups and give
  me a call + text script for each group.
watch_out_for:
- Don't paste PII (Personally Identifiable Information) or confidential deal details unless
  your org policy allows it.
- Treat outputs as drafts; verify anything legal/contractual with your broker/attorney.
- If it cites stats, make it show the source or verify separately.
pairs_well_with: Pair with Canva (graphics) + Zapier (automation) + Follow Up Boss (execution).
```
### Claude

```yaml
name: Claude
category: AI Assistants
pricing: Freemium
link: https://claude.ai
tags:
- writing
- summary
- safe
- research
short_description: AI assistant that's especially strong with long documents and clean, natural
  writing.
how_it_works: Claude handles long inputs well and is great at summarizing, rewriting, and
  extracting key points from big documents. Use it when you need clarity from a messy doc
  pile.
agent_uses:
- 'Summarize HOA/condo docs into: fees, restrictions, rental rules, pet rules, parking, red
  flags.'
- Turn inspection reports into a buyer-friendly "Top 10 items + severity + next step."
- Rewrite your bio and "about" pages so they sound confident without being cringe.
- 'Generate negotiation prep: likely objections + responses + concessions plan.'
- Create long-form blog posts that read like a human wrote them.
quick_demo: Drop a long HOA PDF -> ask for a 1-page buyer summary + "questions to ask HOA
  before option ends."
sample_prompts:
- 'Summarize this HOA document for a buyer. Output: fees, rental restrictions, pet limits,
  parking rules, and any unusual restrictions. Quote the exact section headings when possible.'
- 'Turn this inspection report into: (1) safety items, (2) water intrusion risks, (3) expensive
  items, and (4) DIY vs pro fixes. Then draft an email to the buyer explaining next steps.'
- Write a 900-word blog post about living in [neighborhood] for relocating families. Include
  pros/cons, commute vibe, and 3 "local insider" tips.
watch_out_for:
- Document summaries can miss nuance-spot-check the original sections before advising clients.
- 'Same PII rule: don''t upload private client data unless permitted.'
- 'Keep a standard disclosure: ''AI-assisted summary; verify details in original docs.'''
pairs_well_with: Pair with NotebookLM for citation-driven Q&A on your own docs.
```
### Perplexity

```yaml
name: Perplexity
category: AI Assistants
pricing: Freemium
link: https://www.perplexity.ai
tags:
- search
- research
- data
- news
short_description: Research-first AI that answers with sources so you can verify quickly.
how_it_works: Perplexity is built around web research with citations. It's ideal when you
  want market stats, local news, or vendor comparisons and need to show receipts.
agent_uses:
- Build a weekly 'DFW market snapshot' post with clickable sources.
- Research school districts, major employers, and commute changes for relocation clients.
- Compare CRMs, staging tools, or ad platforms with pros/cons and pricing pages.
- Create neighborhood guides with cited facts (parks, trails, development plans).
- 'Prep for listing appointments: pull recent relevant headlines + comps context.'
quick_demo: 'Ask: ''Create a DFW market update with 5 sources + 3 social captions + 1 email
  version.'''
sample_prompts:
- Give me 5 credible sources on Dallas-Fort Worth housing trends in the last 90 days. Summarize
  each in 2 bullets and then write a 150-word Instagram caption with a neutral tone.
- 'Compare Follow Up Boss vs Lofty for a team of 5. Output: features table, best-fit, and
  deal-breakers. Include pricing/source links.'
- 'Find 10 local "what''s being built" updates for [city/neighborhood]. Output: project, status,
  why it matters to homeowners.'
watch_out_for:
- Sources can be wrong or biased-choose reputable outlets and cross-check.
- Don't present stats without date ranges; real estate data changes fast.
- Use it for research, not final legal/contract advice.
pairs_well_with: Pair with ChatGPT to turn cited research into posts, scripts, and client-friendly
  explanations.
```
### Google Gemini

```yaml
name: Google Gemini
category: AI Assistants
pricing: Freemium
link: https://gemini.google.com
tags:
- google
- workspace
- writing
short_description: Google's AI that shines when you live inside Gmail/Docs/Sheets/Drive.
how_it_works: Gemini integrates into Google Workspace so you can draft, summarize, and analyze
  without leaving Gmail/Docs/Sheets. It's useful for agents who run their world in Google.
agent_uses:
- Turn a messy spreadsheet into segments + follow-up scripts per segment.
- Draft and refine emails inside Gmail (responses, follow-up sequences).
- Generate Sheets formulas, quick analysis, and charts for KPIs (Key Performance Indicators).
- Summarize Drive docs into checklists and action items.
- Convert meeting notes into tasks and next steps.
quick_demo: 'In Sheets: paste leads -> ask Gemini to create segments and a follow-up plan
  per segment.'
sample_prompts:
- In Google Sheets, help me categorize these leads into 4 groups based on last contact date
  and tags, then generate a follow-up script for each group.
- 'Summarize this Gmail thread into: decisions made, open questions, and next steps. Draft
  a reply that confirms next steps and proposes 2 meeting times.'
- 'Create a simple KPI dashboard in Sheets for: leads, appointments, contracts, closings,
  and commission. Include weekly totals.'
watch_out_for:
- Workspace permissions matter-know what data is visible to the AI per your org settings.
- Still validate formulas and charts before sharing them publicly.
- Avoid pasting sensitive client data if your brokerage policy forbids it.
pairs_well_with: Pair with Zapier to route form fills into Sheets + tasks.
```

## Marketing & Content
### Writor

```yaml
name: Writor
category: Marketing & Content
pricing: Paid
link: https://writor.ai
tags:
- listings
- copywriting
- specialized
short_description: Real-estate-specific AI writer for listings, bios, and local guides.
how_it_works: Writor is tuned for real estate outputs (listing remarks, area guides, scripts).
  Give it property facts + audience + tone and it produces usable drafts fast.
agent_uses:
- MLS descriptions with less fluff and better structure.
- Neighborhood/area guides for SEO (Search Engine Optimization).
- 'Open house promos: email + SMS + social captions from one input.'
- Agent bio variants for website, Zillow, Instagram, and email signature.
- 'Video scripts: ''Just Listed'' and ''3 reasons buyers will love this home.'''
quick_demo: Enter property facts -> export MLS copy + 3 captions + 30-sec video script.
sample_prompts:
- Generate an MLS description using these facts... Keep it compliant, lead with the top 3
  features, and avoid overhype.
- Write a 600-word local area guide for [city/neighborhood] aimed at relocating buyers. Include
  lifestyle, commute vibe, and weekend stuff to do.
- 'Create a 7-message follow-up sequence for open house attendees: 3 texts + 2 emails + 2
  calls.'
watch_out_for:
- Still proof for accuracy (schools, measurements, features).
- Avoid prohibited language; match your MLS/brokerage rules.
- Make sure the voice matches your brand-specialized tools can still sound templated.
pairs_well_with: Pair with Canva for fast turn-key listing marketing packs.
```
### Epique AI

```yaml
name: Epique AI
category: Marketing & Content
pricing: Paid
link: https://epique.ai
tags:
- marketing
- suite
- content
short_description: Real-estate content suite (bios, blogs, campaigns) built around agent workflows.
how_it_works: Epique AI is positioned as an all-in-one real estate AI toolkit for marketing
  content (and, depending on access, broker/legal/transaction assistance). Use it for batching
  agent-grade outputs quickly.
agent_uses:
- Generate a full newsletter (subject lines, sections, CTA) from a weekly theme.
- Create 12-touch nurture campaigns (email cadence + talking points).
- Property descriptions, social captions, and "lead gen ideas" prompts.
- Rewrite your marketing so it's consistent across platforms.
- Quick content for new agents who need volume fast.
quick_demo: Pick a theme (rates, spring market, move-up buyers) -> generate newsletter + 3
  posts + 2 reels scripts.
sample_prompts:
- 'Create a real estate newsletter for this week. Include: market note, buyer tip, seller
  tip, featured neighborhood, and a CTA to book a consult.'
- Build a 12-touch nurture campaign for 'cold leads from last year'. Mix email + text + call
  notes.
- 'Write 10 Instagram captions for: first-time buyer myths, down payment options, and inspection
  tips. Keep them simple and punchy.'
watch_out_for:
- If it outputs legal/regulatory guidance, treat it as a starting point-not final advice.
- Confirm whether features are gated by membership/plan before you promise it in class.
- Review tone; suites can get generic fast without specifics.
pairs_well_with: Pair with Perplexity to feed it current stats and local facts.
```
### Copy.ai

```yaml
name: Copy.ai
category: Marketing & Content
pricing: Freemium
link: https://www.copy.ai
tags:
- ads
- social
- copy
short_description: Marketing/sales AI platform geared toward high-volume content and workflow-style
  generation.
how_it_works: Copy.ai started as copywriting and evolved into workflow-based generation for
  marketing and sales teams. Great for producing lots of variants and building repeatable
  content processes.
agent_uses:
- Ad copy variations (Meta/Google) from one property or niche offer.
- 'Cold outreach sequences: email + SMS scripts + voicemail drops (words only).'
- 'Brand voice standardization: keep team posts consistent.'
- 'Repurpose: blog -> email -> social -> reel script (one input, many outputs).'
- Landing page sections and lead magnet copy (buyer/seller guides).
quick_demo: 'Input: ''Just Listed'' brief -> output: 5 ad angles + 3 captions + email + SMS.'
sample_prompts:
- 'Generate 10 Meta ad primary texts + 5 headlines for this listing. Provide 3 different angles:
  lifestyle, location, and value.'
- Create a 5-email nurture sequence for first-time buyers who downloaded my guide. Include
  subject lines and CTAs.
- 'Turn this blog post into: 1 email, 2 LinkedIn posts, 3 IG captions, and 1 30-sec reel script.'
watch_out_for:
- High volume can mean low specificity-force it to use your facts and local context.
- Don't let it invent stats; provide them or require citations.
- Review for compliance and tone before publishing.
pairs_well_with: Pair with Zapier/Make to push outputs into your content calendar automatically.
```

## Visuals & Staging
### Midjourney

```yaml
name: Midjourney
category: Visuals & Staging
pricing: Paid
link: https://www.midjourney.com
tags:
- art
- images
- creative
short_description: High-quality AI image generation for branding, concepts, and lifestyle
  visuals.
how_it_works: Midjourney generates images from prompts. For agents, it's best used for brand
  visuals and conceptual/lifestyle graphics-not for 'this is what the home looks like.'
agent_uses:
- Create custom "neighborhood vibe" visuals for posts and blog headers.
- Illustrate buyer/seller guides (timelines, checklists, concepts).
- Generate branded imagery for your niche (lake life, urban condo, ranch).
- Create "mood boards" for staging/style ideas to show sellers.
- Make thumbnail images for YouTube/shorts that don't look like stock.
quick_demo: Generate 3 styles of "DFW modern home buyer guide cover" -> pick one -> drop into
  Canva template.
sample_prompts:
- 'Create an image for a real estate Instagram carousel cover: ''3 ways to win in a multiple-offer
  situation''. Style: clean, modern, high-contrast, no text.'
- Generate a 'modern farmhouse kitchen mood board' with warm woods, white cabinets, black
  accents, natural light.
- Create a conceptual skyline/neighborhood vibe image for [city] at golden hour, cinematic,
  photoreal, no logos.
watch_out_for:
- Disclose AI-generated images when appropriate; don't imply they're real property photos.
- Watch copyright/trademark issues (logos, brands, recognizable characters).
- Avoid using it to alter listing reality-MLS rules + consumer protection.
pairs_well_with: Pair with Canva for layout and brand consistency.
```
### Canva

```yaml
name: Canva
category: Visuals & Staging
pricing: Freemium
link: https://www.canva.com
tags:
- design
- social
- branding
short_description: 'Design hub for agents: templates, Brand Kit, and AI helpers (Magic Studio).'
how_it_works: Canva combines templates with quick AI tools (resize, background removal, bulk
  variants) so agents can produce consistent marketing without a designer.
agent_uses:
- Listing carousels, flyers, and open house signage from reusable templates.
- Lead magnets (buyer/seller guides) that match your brand.
- 'Batch create: one design -> 10 versions (different neighborhoods, CTAs).'
- Quick image cleanup (remove clutter/objects) for marketing graphics.
- Reels covers and YouTube thumbnails that look consistent week to week.
quick_demo: Take 1 listing photo -> auto-generate a carousel -> resize to story + flyer in
  60 seconds.
sample_prompts:
- Create a 6-slide Instagram carousel outline for 'What does the option period mean in Texas?'
  Keep it simple and visual.
- Generate 3 headline options and 3 subheads for an open house flyer for a 4/3 in [city].
- 'Give me a template system: 5 core post types and the text blocks I should swap each week.'
watch_out_for:
- Templates are only as good as your Brand Kit-set fonts/colors once.
- Don't over-edit listing photos in ways that mislead; disclose virtual staging.
- Keep text large enough for mobile; most agents cram too much.
pairs_well_with: Pair with Writor/ChatGPT to fill templates with fast, consistent copy.
```
### Virtual Staging AI

```yaml
name: Virtual Staging AI
category: Visuals & Staging
pricing: Paid
link: https://www.virtualstagingai.app
tags:
- staging
- photos
- listings
short_description: Fast virtual staging + furniture removal to make vacant rooms market-ready.
how_it_works: Upload room photos and generate staged versions in different styles. Useful
  for making empty spaces feel livable and helping buyers understand scale.
agent_uses:
- Stage vacant listings for photos and ads.
- Create 'Style A vs Style B' versions to match different buyer types.
- Remove furniture/clutter before staging for cleaner marketing.
- Show sellers the 'what it could look like' version during consults.
- Run a before/after carousel for social (with disclosure).
quick_demo: Stage one empty living room in 2 styles -> ask the class which one gets clicks.
sample_prompts:
- 'Stage this living room in: modern, transitional, and contemporary. Keep furniture realistic
  and scale accurate.'
- Remove the existing furniture and declutter, then stage in a light, neutral style.
- Create a staged version that emphasizes 'work-from-home' (desk area) without looking fake.
watch_out_for:
- Disclose virtual staging per MLS/broker rules-don't invite complaints.
- Avoid 'structural' edits (moving walls/windows). That's not staging; that's fiction.
- 'Keep photos consistent: don''t mix 5 wildly different styles in one listing.'
pairs_well_with: Pair with Canva for before/after graphics and captions.
```
### Collov AI

```yaml
name: Collov AI
category: Visuals & Staging
pricing: Paid
link: https://collov.ai
tags:
- design
- renovation
- visualization
short_description: AI interior design + virtual staging with strong 'restyle/declutter' tools.
how_it_works: Collov can stage and also restyle rooms while preserving the underlying structure.
  Useful for visualizing remodel possibilities and improving listing visuals.
agent_uses:
- Virtual staging for vacant rooms and 'style upgrades' for dated spaces.
- Furniture eraser/declutter for cleaner listing photos (marketing use).
- 'Seller consult: show potential modernization ideas without hiring a designer.'
- Create renovation concept posts ('what $15k could do here').
- Help investors visualize rent-ready staging.
quick_demo: Take a dated room -> generate 2 modernized options -> use it in a listing consult
  story.
sample_prompts:
- Restyle this room to 'modern organic' while keeping walls/windows unchanged. Use neutral
  furniture and warm wood accents.
- Remove clutter and furniture, then stage with minimal, bright furnishings.
- 'Create 3 design options: budget, mid, and premium-each with a short explanation of the
  look.'
watch_out_for:
- Same disclosure rules as staging; don't misrepresent property condition.
- Don't imply exact renovation costs from an AI image-use it as inspiration only.
- Check for weird artifacts (floating lamps, impossible shadows) before posting.
pairs_well_with: Pair with Perplexity to find real local renovation cost ranges (then cite
  them).
```
### Photoroom

```yaml
name: Photoroom
category: Visuals & Staging
pricing: Freemium
link: https://www.photoroom.com
tags:
- photos
- headshots
- editing
short_description: AI photo editor for clean cutouts, background removal, and quick marketing
  graphics.
how_it_works: Photoroom excels at removing backgrounds and creating polished images fast (especially
  on mobile). Great for agent headshots, thumbnails, and product-style promo graphics.
agent_uses:
- Turn a basic headshot into clean branded assets for posts and thumbnails.
- Create 'Just Listed' tiles with cutouts + text overlays.
- Make clean images for lead magnets and landing pages.
- Quickly remove background clutter for marketing graphics.
- Batch-edit similar images for consistency.
quick_demo: Cut out an agent headshot -> place on 3 branded backgrounds -> export 3 platforms.
sample_prompts:
- Remove background and smooth lighting naturally (don't make me look plastic).
- 'Create 3 background options: office, neutral studio, and subtle outdoor bokeh.'
- Generate a clean 'Just Sold' tile using this photo and these brand colors.
watch_out_for:
- Don't over-retouch; buyers smell 'fake' a mile away.
- Keep image dimensions consistent for your main platforms.
- If you generate backgrounds, don't imply you were on location.
pairs_well_with: Pair with Canva for layout and template reuse.
```

## Video & Social
### Opus Clip

```yaml
name: Opus Clip
category: Video & Social
pricing: Freemium
link: https://www.opus.pro
tags:
- shorts
- reels
- repurposing
short_description: Repurposes long videos into shorts by finding highlight moments and adding
  captions.
how_it_works: Upload a long video (podcast, market update, training) and OpusClip identifies
  promising segments, reframes them for vertical, and adds captions.
agent_uses:
- Market update video -> 8 reels for the month.
- Record one Q&A session -> clip into FAQ shorts.
- Client testimonial compilation -> highlights for social proof.
- Turn training sessions into recruiter content for your team.
- Build a consistent 'weekly tip' shorts pipeline.
quick_demo: Upload a 5-10 minute market update -> pick the top 3 clips -> post-ready in minutes.
sample_prompts:
- Select clips that start with a strong hook and are under 35 seconds.
- 'Prioritize clips about: pricing strategy, multiple offers, and inspection tips.'
- Generate 5 headline/caption options per clip with a local DFW angle.
watch_out_for:
- AI can clip the 'wrong' moment-review context so you don't sound dumb.
- Confirm captions; proper nouns and city names often get mangled.
- Don't rely on it for property-tour accuracy; tours need careful edits.
pairs_well_with: Pair with Captions.ai for polishing and consistent styling.
```
### Descript

```yaml
name: Descript
category: Video & Social
pricing: Freemium
link: https://www.descript.com
tags:
- editing
- transcription
- voice
short_description: 'Edit audio/video like a document: cut by transcript, remove filler words,
  and polish fast.'
how_it_works: Descript transcribes your recording, then you edit by editing text. It's ideal
  for talking-head content, podcasts, interviews, and training recordings.
agent_uses:
- Clean up market update videos (remove 'ums,' dead air).
- Create podcast-style episodes for your niche (investors, relocations).
- Generate transcripts for blogs, captions, and email content.
- Produce quick 'explainer' videos with tighter pacing.
- Record screen tutorials for your clients (how to search MLS, etc.).
quick_demo: Record 60 seconds, remove filler words, add captions, export vertical clip.
sample_prompts:
- Remove filler words and long pauses but keep my tone natural.
- Create captions and a clean transcript, then generate 5 social captions from it.
- Turn this transcript into a 700-word blog post + 5 bullet highlights.
watch_out_for:
- Voice cloning features require consent-don't fake someone's voice.
- Auto edits can sound robotic; listen once before publishing.
- Keep your raw files backed up outside the app.
pairs_well_with: Pair with Opus Clip (finding clips) and Canva (thumbnails).
```
### HeyGen

```yaml
name: HeyGen
category: Video & Social
pricing: Paid
link: https://www.heygen.com
tags:
- avatars
- translation
- cloning
short_description: Avatar video and video translation (with lip-sync) to go multilingual fast.
how_it_works: HeyGen can generate avatar-driven videos from scripts and translate videos into
  other languages with voice + lip sync. Great for evergreen explainers and multilingual markets.
agent_uses:
- Translate your best-performing videos into Spanish (or other languages) for DFW audiences.
- Create evergreen FAQ videos without setting up a camera every time.
- Build a 'new lead welcome' video series (buyer/seller).
- Create relocation explainers (schools, commute, process) in multiple languages.
- Produce quick announcement videos (price drop, open house, new listing).
quick_demo: Take a 30-sec video -> translate -> post side-by-side versions.
sample_prompts:
- Translate this video to Spanish and keep names/places accurate. Add subtitles too.
- 'Create a 45-second avatar video: ''What happens after you go under contract in Texas?''
  Tone: calm, clear.'
- Write a script for a 'buyer consultation welcome' video with 3 next steps and a booking
  CTA.
watch_out_for:
- Disclose when using an avatar; don't impersonate real people.
- Double-check translations for local terms and proper nouns.
- Don't use it to 'fake' testimonials or client statements.
pairs_well_with: Pair with Descript for transcript cleanup before translation.
```
### Captions.ai

```yaml
name: Captions.ai
category: Video & Social
pricing: Paid
link: https://www.captions.ai
tags:
- mobile
- social
- captions
short_description: 'Mobile-first AI editor for talking-head videos: captions, pacing, and
  quick polish.'
how_it_works: Captions.ai is built for short-form video creation-auto captions, editing helpers,
  and options like eye-contact/pacing adjustments. Designed to get from selfie to post quickly.
agent_uses:
- 'Daily reels with clean captions (the #1 retention booster).'
- 'Fast FAQ videos: record -> captions -> export.'
- Polish listing intros and open house invites.
- Create consistent visual style across your videos.
- 'Batch-edit: record 5 tips in a row and process them quickly.'
quick_demo: Record a 20-second 'open house invite' -> auto captions -> export in 60 seconds.
sample_prompts:
- Generate accurate captions, highlight keywords, and keep lines short for mobile.
- Create 3 hook options to overlay at the start of this video (no clickbait).
- Produce a version optimized for Reels and another for YouTube Shorts.
watch_out_for:
- Eye-contact and auto-zoom can look weird-use lightly.
- Always review captions; city names and lender terms get misheard.
- Keep branding consistent-pick one caption style and stick with it.
pairs_well_with: Pair with Opus Clip (clip selection) and Canva (covers/thumbnails).
```
### Luma Dream Machine

```yaml
name: Luma Dream Machine
category: Video & Social
pricing: Freemium
link: https://lumalabs.ai/dream-machine
tags:
- b-roll
- creative
- video
short_description: Text-to-video generator for cinematic b-roll and conceptual clips.
how_it_works: 'Luma''s Dream Machine generates short video clips from text (and sometimes
  image) prompts. Best used for non-literal b-roll: vibes, transitions, intros.'
agent_uses:
- Create 'market update' intro clips (skyline, coffee shop vibe, moving day).
- Add b-roll to talking-head videos to keep retention up.
- Create conceptual visuals for buyer/seller education posts.
- Generate backdrop clips for presentations and reels.
- Make creative transitions between scenes.
quick_demo: Generate a 5-10 second 'DFW skyline intro' clip and use it as your reel opener.
sample_prompts:
- 'Cinematic 8-second video: Dallas skyline at sunrise, smooth camera pan, realistic motion,
  9:16 vertical.'
- 'Create a subtle b-roll clip: hands signing papers at a kitchen table, natural light, documentary
  style.'
- 'Generate a neighborhood vibe clip: tree-lined street, morning joggers, calm, realistic.'
watch_out_for:
- Never present AI video as footage of an actual property or event.
- Expect re-rolls; prompts take iteration.
- Check licensing/terms if you use outputs in paid ads.
pairs_well_with: Pair with Descript to layer b-roll into your edited videos.
```

## CRM & Lead Gen
### Follow Up Boss

```yaml
name: Follow Up Boss
category: CRM & Lead Gen
pricing: Paid
link: https://www.followupboss.com
tags:
- crm
- automation
- leads
short_description: Real-estate-first CRM for lead intake, routing, tasks, and accountability.
how_it_works: Follow Up Boss centralizes leads from many sources, routes them to the right
  person, and makes follow-up measurable. It's strongest for teams who care about speed-to-lead
  and process.
agent_uses:
- Automated lead routing and round-robin distribution for teams.
- 'Action plans: tasks + emails/text templates by lead type.'
- 'Source tracking: know what ad/source produced closings.'
- 'Database cleanup: tags, stages, and follow-up reminders.'
- 'Team accountability: response time, follow-up volume, pipeline clarity.'
quick_demo: 'Show: lead comes in -> auto-assign -> task + text template -> pipeline stage
  update.'
sample_prompts:
- Build me a simple pipeline with stages for buyer leads and seller leads. Include which task
  templates should fire at each stage.
- 'Create 5 text templates for new leads: immediate response, scheduling, no-response, nurture,
  and reactivation.'
- 'Design a weekly KPI report: response time, appointments set, contacts made, and deals created.'
watch_out_for:
- CRMs fail from 'no rules'-define tags, stages, and ownership.
- Beware duplicate lead sources; dedupe and standardize fields.
- Texting compliance (TCPA) is on you-use opt-in/opt-out correctly.
pairs_well_with: Pair with ManyChat + Zapier to capture and route social leads cleanly.
```
### Lofty

```yaml
name: Lofty
category: CRM & Lead Gen
pricing: Paid
link: https://lofty.com
tags:
- crm
- leads
- isa
short_description: 'All-in-one real estate platform (formerly Chime): CRM + marketing + lead
  conversion.'
how_it_works: Lofty bundles CRM, marketing automation, and lead tools in one ecosystem. Best
  for agents/teams who want a single hub and are willing to learn a bigger system.
agent_uses:
- Run IDX capture + nurture + follow-up in one platform.
- Use automated plans to keep leads warm without manual chasing.
- Team lead distribution and ISA-style workflows.
- 'Marketing automation: campaigns and follow-up based on behavior.'
- Centralize your lead sources and track conversion.
quick_demo: 'Show the lead journey: website registration -> automated plan -> agent task ->
  appointment.'
sample_prompts:
- 'Map a ''new buyer lead'' workflow: day 0-14 tasks, texts, and calls. Include a handoff
  point when the lead is appointment-ready.'
- 'Create a seller lead nurture plan built around: home value curiosity, timing, and motivation.'
- Define 6 tags I should use consistently to segment leads and track KPIs.
watch_out_for:
- All-in-ones can get complex-train on one workflow first (new buyer leads).
- Pricing and onboarding can be heavier than lighter CRMs-budget time.
- Don't let automation replace human follow-up; it should tee you up, not ghost clients.
pairs_well_with: Pair with Perplexity for market research content feeding campaigns.
```
### Ylopo

```yaml
name: Ylopo
category: CRM & Lead Gen
pricing: Paid
link: https://www.ylopo.com
tags:
- marketing
- nurture
- ads
short_description: Marketing + lead nurture platform with conversational AI texting to drive
  appointments.
how_it_works: Ylopo focuses on digital marketing and follow-up, including AI-driven text conversations
  that keep leads engaged and alert you when they're ready for a human handoff.
agent_uses:
- 'Speed-to-lead: engage instantly via text when someone opts in.'
- Revive old databases with smart re-engagement sequences.
- Qualify leads with basic questions (timing, motivation, lender status).
- Run ad campaigns tied to nurture and appointment setting.
- Improve contact rate without living on your phone.
quick_demo: 'Show a lead flow: new lead -> AI text starts convo -> agent alert when qualified.'
sample_prompts:
- 'Write a reactivation campaign for leads older than 180 days. Goal: get timing + motivation
  in 2 questions.'
- 'Create 10 conversational text responses for common lead replies: ''just looking'', ''already
  have an agent'', ''what''s the price?'', ''not ready''...'
- Build a follow-up script for when AI flags a lead as appointment-ready.
watch_out_for:
- Texting compliance (TCPA) and opt-outs must be handled correctly.
- Review conversations regularly-automation can drift in tone.
- Make sure handoff rules are clear so hot leads don't get stuck in bot mode.
pairs_well_with: Pair with Follow Up Boss to manage the human pipeline once leads are ready.
```
### ManyChat

```yaml
name: ManyChat
category: CRM & Lead Gen
pricing: Freemium
link: https://manychat.com
tags:
- social
- automation
- chat
short_description: 'Instagram/Facebook DM automation: comment triggers, keyword DMs, and lead
  capture flows.'
how_it_works: ManyChat lets you build automated DM conversations based on triggers (comments,
  DMs, story replies). For agents, it's a 'social inbox funnel' that captures leads while
  you're asleep.
agent_uses:
- '''Comment PRICE'' -> auto DM link + capture email/phone.'
- Open house RSVP flow with 2-3 qualifying questions.
- Deliver buyer/seller guides instantly in DMs.
- 'Lead routing: send captured info to CRM/Sheets via Zapier.'
- 'Follow-up: tag people by intent (buyer, seller, investor, relocation).'
quick_demo: Post a reel. When someone comments 'LIST', they get a DM sequence + form link.
sample_prompts:
- 'Design a DM flow for open house RSVPs: confirm time, ask if they''re working with an agent,
  ask financing status, then send the address.'
- 'Create a DM flow for ''Free Buyer Guide'': deliver link, ask their timeline (0-3 / 3-6
  / 6-12 months), then tag them.'
- Write the exact DM messages (short, friendly, not spammy) for each step.
watch_out_for:
- Stay within Meta's rules; don't spam or over-message.
- If you collect phone numbers, handle opt-in and provide opt-out language.
- Don't promise instant availability-set expectations and a booking link.
pairs_well_with: Pair with Zapier -> Follow Up Boss to create the lead automatically.
```

## Voice & Meetings
### Otter.ai

```yaml
name: Otter.ai
category: Voice & Meetings
pricing: Freemium
link: https://otter.ai
tags:
- notes
- meetings
- transcription
short_description: 'AI meeting assistant: records/transcribes and produces summaries and action
  items.'
how_it_works: Otter joins meetings (or records uploads), transcribes, and generates summaries/action
  items. It's great for keeping buyer/seller consults searchable and shareable.
agent_uses:
- Buyer consult recap -> send a clean summary email the same day.
- Listing appointment notes -> create tasks and timelines automatically.
- Team meeting action items -> reduce 'who's doing what?' confusion.
- 'Training library: record classes and make them searchable.'
- Extract client preferences (must-haves vs nice-to-haves) from calls.
quick_demo: Record a mock consult -> generate summary + action items -> paste into CRM note.
sample_prompts:
- 'Summarize this meeting into: goals, constraints, timeline, and next steps.'
- Extract the buyer's must-haves, deal-breakers, and preferred areas from this transcript.
- Draft a follow-up email to the client confirming next steps and what I need from them.
watch_out_for:
- Get recording consent (state law + brokerage policy).
- Transcription errors happen-correct critical numbers and addresses.
- Don't store sensitive info if your policy prohibits it.
pairs_well_with: Pair with Notion to store summaries in a client workspace, or with your CRM
  for notes.
```
### Fathom

```yaml
name: Fathom
category: Voice & Meetings
pricing: Free
link: https://fathom.video
tags:
- zoom
- crm
- notes
short_description: Meeting recorder + AI summaries that can sync notes into your other tools.
how_it_works: Fathom records meetings, generates structured summaries, and can sync notes/actions
  into tools like CRMs and project management systems. Great when you want 'notes that actually
  go somewhere.'
agent_uses:
- Client consults -> auto recap + tasks without manual typing.
- Sales calls -> highlight moments and send clips to team members.
- 'Coaching: review call highlights and improve scripts.'
- Push summaries into your CRM/contact record for continuity.
- Search past calls by topic (e.g., "appraisal", "option period").
quick_demo: Run a short call -> show the summary + action items -> show a sync/export.
sample_prompts:
- 'Create a summary tailored for a buyer consult: goals, timeline, financing status, next
  steps.'
- Generate a short follow-up email and a text message based on this meeting.
- List every commitment I made in the call and assign an owner/date.
watch_out_for:
- Same consent rule as any meeting recorder.
- Check your sync settings so notes don't land on the wrong contact.
- Don't rely on it to interpret legal issues; it's summarizing, not advising.
pairs_well_with: Pair with Follow Up Boss to store call notes automatically.
```

## Data & Ops
### Notion

```yaml
name: Notion
category: Data & Ops
pricing: Freemium
link: https://www.notion.so
tags:
- organization
- wiki
- planning
short_description: All-in-one workspace (docs + databases) that can become an 'Agent OS' for
  content and operations.
how_it_works: Notion lets you build structured databases (transactions, content calendar,
  vendor list) and use Notion AI to summarize and generate content inside your workspace.
agent_uses:
- Transaction tracker with checklists, dates, and links to docs.
- Content calendar database with status, platform, and reusable templates.
- Vendor and referral database with notes, ratings, and coverage areas.
- 'Team wiki: SOPs, scripts, onboarding, policies.'
- Client portal pages (selectively) with timelines and expectations.
quick_demo: Show a 'Listing Launch' database template that auto-generates a checklist and
  captions.
sample_prompts:
- Create a listing launch checklist with tasks by timeline (T-14, T-7, T-1, launch day).
- Summarize these meeting notes into action items and assign due dates.
- Generate 10 post ideas for my niche and add them as database entries with suggested hooks.
watch_out_for:
- Notion is powerful but can become messy-define 3-5 core databases and stick to them.
- Permissions matter if you share pages externally (clients/vendors).
- Don't store sensitive client documents unless your compliance policy allows it.
pairs_well_with: Pair with Zapier/Make to auto-create Notion items from form fills and leads.
```
### HouseCanary

```yaml
name: HouseCanary
category: Data & Ops
pricing: Paid
link: https://housecanary.com
tags:
- valuation
- investors
- data
short_description: Real estate data + analytics + valuation models (AVMs) for pricing and
  investor-style insights.
how_it_works: HouseCanary provides property data, valuations, and market insights designed
  for lending/investment use cases. Agents use it to support pricing narratives and investor
  conversations.
agent_uses:
- Support a listing price conversation with data-backed ranges and trends.
- 'Create investor briefs: rent estimates, yield conversation starters, neighborhood trend
  context.'
- Market update visuals and talking points for content.
- Identify potential sellers (equity, tenure) depending on your data access and compliance.
- Build better listing presentations with charts and forecasts (as supporting info).
quick_demo: 'Pull a property report -> turn it into a 5-slide seller story: pricing, trend,
  comps context, strategy.'
sample_prompts:
- 'Turn this HouseCanary report into a seller-friendly summary: what the numbers suggest and
  how we''d price/market.'
- Write 3 talking points for an investor buyer using these rent/value estimates. Include risks/assumptions.
- Create a simple market update post using these zip-code trends (include dates).
watch_out_for:
- AVM (Automated Valuation Model) is not an appraisal-present it as one input.
- Local comps and on-the-ground condition still matter; don't outsource judgment to a model.
- Respect data licensing/terms and your brokerage policy when sharing reports.
pairs_well_with: Pair with Perplexity to cite external market sources and with Canva for clean
  visuals.
```
### Zapier

```yaml
name: Zapier
category: Data & Ops
pricing: Freemium
link: https://zapier.com
tags:
- automation
- integration
- workflow
short_description: 'Automation connector: triggers + actions across apps; includes AI-assisted
  Zap building.'
how_it_works: Zapier connects your tools so you don't do copy/paste work all day. You define
  triggers (new lead, form submitted) and actions (create contact, send message, log to sheet).
agent_uses:
- ManyChat lead -> create contact in CRM -> tag -> notify agent -> log in Sheet.
- Google Form open house sign-in -> email follow-up + task creation.
- New Google review request automation after closing.
- 'Content pipeline: idea captured -> Notion card -> reminder to film -> publish checklist.'
- 'Lead enrichment: add city/county, source, tags, and routing rules automatically.'
quick_demo: 'Build one Zap: IG DM lead -> Google Sheet -> email notification -> CRM task.'
sample_prompts:
- 'Design a Zapier workflow for open house sign-ins: form -> CRM contact -> tag -> 3-day follow-up
  task sequence.'
- Create an automation that logs every new lead to a Google Sheet with date, source, and assigned
  agent.
- Build a review request workflow that sends 2 reminders and stops when the review link is
  clicked.
watch_out_for:
- Automations can loop-use filters and naming conventions.
- 'Data security: avoid sending sensitive client data through unnecessary steps.'
- Log errors and alerts; otherwise failures are silent.
pairs_well_with: Pair with Make when you need more complex branching and error handling.
```

---
## Recommended additions (not currently in your HTML)
### NotebookLM

```yaml
name: NotebookLM
category: AI Assistants / Research
pricing: Freemium
link: https://notebooklm.google/
short_description: Chat with your own docs and get cited answers from your sources.
why_add: It reduces hallucinations by forcing answers to anchor to your uploaded sources (great
  for contracts/HOA docs).
agent_uses:
- Upload HOA docs/inspection PDFs and ask questions with citations.
- Build a 'Buyer Guide' notebook and generate FAQ answers grounded in your materials.
- Create a training notebook for your team and keep answers consistent.
watch_out_for:
- Still verify edge-case details in originals; citations help, but humans decide.
- Don't upload sensitive client docs unless policy allows.
```
### Make (Make.com)

```yaml
name: Make (Make.com)
category: Data & Ops
pricing: Freemium
link: https://www.make.com/en
short_description: Visual automation builder for more complex workflows than Zapier.
why_add: For teams who hit Zapier limits and need branching, retries, and visibility.
agent_uses:
- Multi-step lead routing with branching logic and error handling.
- Sync data between CRM, Sheets, email, and Slack with fewer limitations.
- Automate content pipelines (idea -> script -> task -> publish log).
watch_out_for:
- More power = more ways to break things; document your scenarios.
- Be intentional about what data you pass between systems.
```
### Scribe

```yaml
name: Scribe
category: Data & Ops
pricing: Freemium
link: https://scribe.com/
short_description: Records your process and auto-creates step-by-step SOPs.
why_add: Saves hours of training time and makes your systems teachable.
agent_uses:
- Document your lead intake and follow-up workflow once, then reuse forever.
- Create quick 'how to use the CRM' guides for new agents/assistants.
- Build transaction checklist SOPs agents can actually follow.
watch_out_for:
- Scrub screenshots if sensitive data appears.
- Keep SOPs updated as tools change.
```
### Highnote

```yaml
name: Highnote
category: Marketing & Content
pricing: Paid
link: https://highnote.io/real-estate/
short_description: Digital buyer/listing presentations with analytics (what clients viewed).
why_add: Turns presentations into trackable sales assets (and helps follow-up timing).
agent_uses:
- Listing presentations that look modern and track engagement.
- Buyer consult decks + offer strategy pages.
- Send follow-up decks after appointments instead of PDFs that die in email.
watch_out_for:
- Don't overload decks; keep to a clear narrative.
- Make sure your analytics tracking is disclosed per your policy.
```
### Calendly

```yaml
name: Calendly
category: CRM & Lead Gen
pricing: Freemium
link: https://calendly.com/
short_description: Scheduling links that convert 'maybe' into an actual appointment.
why_add: It ends the back-and-forth and improves speed-to-appointment.
agent_uses:
- DM someone a booking link the moment they show interest.
- Automate reminders and reduce no-shows.
- 'Route meeting types: buyer consult vs listing consult vs lender intro.'
watch_out_for:
- Protect your calendar rules (buffers, travel time).
- Use time-zone handling for relocation clients.
```
### Loom

```yaml
name: Loom
category: Video & Social
pricing: Freemium
link: https://www.loom.com/
short_description: Quick screen + camera videos for follow-up that feels personal.
why_add: It boosts trust without adding meeting time.
agent_uses:
- Personalized 'here are 3 homes I'd shortlist' videos to a buyer.
- Seller update videos (show traffic, showing feedback, next steps).
- 'Quick tutorials: how to use your search portal, how to sign docs.'
watch_out_for:
- Don't show private MLS data publicly; share only with intended recipient.
- Keep videos short-aim 60-120 seconds.
```
### CapCut

```yaml
name: CapCut
category: Video & Social
pricing: Freemium
link: https://www.capcut.com/
short_description: Fast video editor with strong captions/templates for social.
why_add: Great "cheap + fast" editing option for agents who won't learn Premiere.
agent_uses:
- Polish tours, reels, and market updates fast.
- Auto captions and quick visual effects for retention.
- Batch-edit multiple clips consistently.
watch_out_for:
- Templates can look generic-use your Brand Kit and keep it clean.
- Review captions for accuracy.
```
### Riverside

```yaml
name: Riverside
category: Video & Social
pricing: Freemium
link: https://riverside.fm/
short_description: High-quality remote recording for podcasts, interviews, and client stories.
why_add: Better audio/video quality makes clips feel more professional immediately.
agent_uses:
- Record lender/inspector interviews and repurpose into clips.
- Client success-story interviews (with permission).
- Team training recordings that don't sound like a tin can.
watch_out_for:
- Get written permission before using client clips for marketing.
- Keep backups of raw recordings.
```
### Fireflies.ai

```yaml
name: Fireflies.ai
category: Voice & Meetings
pricing: Freemium
link: https://fireflies.ai/
short_description: Meeting recorder + summaries + searchable call library (alt to Otter/Fathom).
why_add: Gives agents options; some prefer its integrations/UX.
agent_uses:
- Auto notes for consults and team calls.
- Search call history by keyword (e.g., 'option period').
- Share meeting recaps with assistants and transaction coordinators.
watch_out_for:
- Consent rules still apply.
- Double-check what integrations are available on your plan.
```
### CallRail

```yaml
name: CallRail
category: CRM & Lead Gen
pricing: Paid
link: https://www.callrail.com/
short_description: Call + form tracking to prove which marketing actually produced leads.
why_add: Stops 'I think this ad works' guessing with real attribution.
agent_uses:
- Track calls from Google Business Profile (GBP) and ads.
- Attribute leads to campaigns and cut wasted spend.
- Record calls for quality and training (with consent).
watch_out_for:
- Recording disclosure and compliance matter.
- Keep tracking numbers consistent across campaigns.
```
### Chatbase

```yaml
name: Chatbase
category: AI Assistants / Website
pricing: Paid
link: https://www.chatbase.co/
short_description: Train a website chatbot on your docs/website to answer FAQs 24/7.
why_add: Turns your site into a 24/7 assistant without building custom code.
agent_uses:
- Embed on your site to answer buyer/seller FAQs instantly.
- Qualify leads with 2-3 questions before handing to you.
- Reduce 'basic question' calls and increase bookings.
watch_out_for:
- Don't let the bot answer legal/contract advice-set guardrails.
- Review and update its source docs regularly.
```
### Relevance AI

```yaml
name: Relevance AI
category: Data & Ops
pricing: Paid
link: https://relevanceai.com/
short_description: No-code platform for building multi-step AI agents that run workflows.
why_add: If you're moving toward agentic workflows, this is a step up from simple chat + zaps.
agent_uses:
- Build an 'AI content coordinator' that drafts, checks, and schedules content.
- Create an 'agent concierge' that triages inbound leads and routes tasks.
- Automate research -> summary -> draft sequences without manual prompting.
watch_out_for:
- More advanced tool; requires setup discipline.
- Be careful with data you connect and store.
```
