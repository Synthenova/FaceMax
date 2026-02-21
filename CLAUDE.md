# FaceMax Project Guide

> **Current Phase:** Planning & Research  
> **Next Milestone:** Phase 1 (MVP) Development

## Project Overview
FaceMax is a looks-focused self-improvement app helping men maximize their facial aesthetics ("looksmaxxing") through **science-backed daily routines**, **AI progress tracking**, and **community accountability**. It moves beyond simple "face ratings" (competitor standard) to provide actionable, guided improvement plans.

## Documentation Index

| File | Purpose | Key Contents |
|---|---|---|
| **[`docs/PRD.md`](./docs/PRD.md)** | **Master Specs** | Full MVP features, database schema, API logic, tech stack (RN + Firebase), success metrics. **Read this for implementation details.** |
| **[`docs/competitive-analysis.md`](./docs/competitive-analysis.md)** | **Strategy** | Deep dive on Umax/LooksMax AI/AscendMax. Pricing models, churn reasons, and the "Routine Gap" opportunity. |
| **[`docs/UI-Design-Prompt.md`](./docs/UI-Design-Prompt.md)** | **Design** | Dark mode color system (`#1E3A5F`), typography, component specs, and detailed layout for all 14 screens. |
| **[`docs/FaceMax-App-Overview.md`](./docs/FaceMax-App-Overview.md)** | **Vision** | High-level "Pitch Deck". Mission, core philosophy, and the "why" behind the product. |
| **[`docs/facemaxing-landscape.md`](./docs/facemaxing-landscape.md)** | **Research** | Cultural context of looksmaxxing. Influencers, techniques (mewing, chewing), and "toxic" vs "healthy" trends. |
| **[`docs/looksmaxing apps- grok.md`](./docs/looksmaxing%20apps-%20grok.md)** | **Raw Data** | AI summary of top apps & user pain points (paywalls, inconsistencies). |
| **[`docs/looksmaxing apps-gai.md`](./docs/looksmaxing%20apps-gai.md)** | **Raw Data** | Google AI research on "paywall traps" and the pivot to "Ethical Looksmaxxing". |
| **[`docs/looksmaxing apps-reddit.md`](./docs/looksmaxing%20apps-reddit.md)** | **Raw Data** | Reddit threads analysis. Highlights "Looksglo" as a positive example for actionable data. |

## Core Rules for Development
1. **Routines First:** The app is about *doing*, not just *rating*. Prioritize exercise timers and trackers.
2. **Tech Stack:** React Native (Expo), Firebase (Auth/Firestore), Gemini Flash (AI), TensorFlow Lite (On-device).
3. **Design:** Dark, premium, masculine (Oura/Whoop aesthetic).
4. **Ethics:** No toxicity. Science-backed advice only.

## AI-Generated Content

**`ai-gen/`** folder stores all AI-generated marketing and design assets (images, copy, social posts). When using any skill to generate AI images, save outputs directly to this folder.

## Quick Links
- [Product Requirements (PRD)](./docs/PRD.md)
- [UI Guidelines](./docs/UI-Design-Prompt.md)
- [Competitive Strategy](./docs/competitive-analysis.md)

---