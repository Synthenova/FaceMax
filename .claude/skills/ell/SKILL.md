---
name: ell
description: >
  Eternal Learning Loop — Ingests raw content from any URL or topic (YouTube transcripts,
  Reddit threads, web articles), synthesizes it into a structured Agent Knowledge Module (AKM),
  saves it to docs/exercises/, and registers it in the CLAUDE.md index so the agent
  immediately gains the new knowledge. Usage: /ell <url_or_topic> [--category <category_name>]
---

# Eternal Learning Loop (ELL)

You are executing the **Eternal Learning Loop** — a three-stage pipeline that expands the FaceMax agent knowledge graph with new techniques from live sources.

## Input Parsing

The user will invoke this skill with a URL, YouTube link, Reddit thread, or a topic string. Extract:
- `SOURCE`: the URL or topic provided
- `CATEGORY` (optional): if the user passed `--category <name>`, use that. Otherwise you will determine it from context in the Weave phase.

---

## Stage 1 — FORAGER (You, using MCPs)

Your job is to retrieve the raw source content. Choose the right tool based on source type:

**YouTube URL** (`youtube.com/watch` or `youtu.be`):
- Use `agent-browser-cdp` to navigate to the video page and extract the transcript via the "...more" description / transcript panel, OR
- Use `WebFetch` on `https://youtubetranscript.com/?server_vid2=<VIDEO_ID>` to get a plain-text transcript.
- If neither works, use `WebSearch` to find the video topic and gather equivalent written content.

**Reddit URL** (`reddit.com`):
- Use `WebFetch` on the URL directly. Extract all top-level comment text and the post body.

**Any other web URL** (article, grokipedia, forum):
- Use `WebFetch` on the URL. Extract the main body text.

**Topic string (no URL)**:
- Use `WebSearch` for `"<topic> looksmaxxing technique"` and `"<topic> facial exercise"`.
- Pick the highest-quality result and use `WebFetch` to retrieve its full content.

Store the retrieved content as `RAW_CONTENT`. Log: `[Forager] Source ingested. Character count: <N>`

---

## Stage 2 — WEAVER (Sub-agent via Task tool)

Spawn a **general-purpose sub-agent** using the Task tool. Pass it the following prompt verbatim, substituting `{{RAW_CONTENT}}` with the text you retrieved:

---

**Sub-agent prompt:**

```
You are the FaceMax Weaver. Your job is to transform raw, unstructured content into a strict Agent Knowledge Module (AKM) in markdown format.

RAW CONTENT:
{{RAW_CONTENT}}

INSTRUCTIONS:
1. Identify the primary technique or concept described.
2. Determine the correct filename: lowercase, hyphen-separated, no spaces. E.g. "neck-wall-press.md"
3. Determine the correct CLAUDE.md category from this list:
   - 01-jawline-and-mewing
   - 02-neck-and-posture
   - 03-cheeks-and-midface
   - 04-eyes-and-brows
   - 05-forehead-and-nasolabial
   - 06-mouth-and-lips
   - 07-massage-and-drainage
   - 08-skincare-and-lifestyle
   - 09-index-and-overviews
   - 10-bone-structure-and-advanced
   - 11-looksmaxxing-theory-and-assessment
4. Write the AKM in this exact format:

# <Technique Name>

## Overview
<2-3 sentence science-backed description of what this technique does and why.>

**Category:** <body area>
**Difficulty:** <Beginner / Intermediate / Advanced / Extreme>
**Time per Session:** <duration>
**Frequency:** <Daily / 3x week / etc.>

---

> [!CAUTION] <If any safety risks exist, extract and state them clearly. If none, omit this block.>

## Technique
1. <Step 1>
2. <Step 2>
...

## Expected Results
- <Realistic outcome 1>
- <Realistic outcome 2>

## Scientific Basis
<1-2 sentences on the anatomical or physiological mechanism. If speculative, label it as such.>

---

*Document Version: 1.0 (Auto-Generated via Eternal Learning Loop)*
*Source: <source URL or topic>*

5. Save the AKM file to: docs/exercises/<filename>
   Use the Write tool to create the file.
6. Return ONLY this JSON (no other text):
{"filename": "<filename.md>", "category": "<category-string>"}
```

---

Wait for the sub-agent to return. It will provide `{"filename": "...", "category": "..."}`. Extract these values.

Log: `[Weaver] AKM created → docs/exercises/<filename>`

---

## Stage 3 — INDEXER (Python script)

Run the standalone indexer to register the new file in CLAUDE.md:

```bash
python scripts/indexer.py <filename> <category>
```

The indexer will append the filename to the correct category line in CLAUDE.md.

Log: `[Indexer] CLAUDE.md updated.`

---

## Completion Report

After all three stages succeed, report to the user:

```
✅ Eternal Learning Loop Complete

Forager  → Ingested: <source>
Weaver   → Created:  docs/exercises/<filename>
Indexer  → Indexed:  <category> in CLAUDE.md

The agent now knows: <Technique Name>
Switch to a new conversation — it will have this knowledge immediately.
```

If any stage fails, report the stage that failed and the error. Do not proceed to the next stage on failure.
