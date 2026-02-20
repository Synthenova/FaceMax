# FaceMax Exercise Research - Agent Team Orchestration Prompt

> **Purpose:** Standardized process for adding new exercises to the FaceMax library
> **Version:** 1.0
> **Last Updated:** February 2026

---

## Quick Start for Adding New Exercises

Use this prompt to initiate a uniform research process for new exercises. This ensures all exercises have consistent structure, safety information, and quality standards.

---

## Phase 1: Sourcing (Optional)

If the exercise is already identified, skip to Phase 2. Otherwise, use a sourcing agent:

```
You are a Sourcing Agent. Find detailed information about [EXERCISE NAME] from:
- Google AI / Search (use agent-browser-cdp)
- Reddit (r/looksmaxxing, r/orthotropics, r/FaceGym)
- YouTube tutorials
- Instagram/TikTok trends
- Health/medical websites

Create a file at `docs/exercises/sourced-[exercise-name].md` with:
- Source URLs
- Brief description
- Popularity level
- Any safety warnings from sources
- Key steps if available
```

---

## Phase 2: Research (Primary)

Create a detailed exercise document following this EXACT format:

### File Naming
`docs/exercises/[exercise-name].md` (kebab-case, lowercase)

### Required Document Structure

```markdown
# [Exercise Name]

## Overview
- **Category**: [Jawline & Facial Structure / Neck & Double Chin / Cheeks & Facial Toning / Eyes, Brows & Forehead / Massage & Lymphatic / Full Face & Yoga / Lifestyle & Supporting]
- **Target Areas**: [Specific muscles or areas]
- **Equipment Needed**: [None / List items]

## How It Works
[2-4 paragraph scientific/mechanical explanation of why this exercise works]

## Instructions

### Step-by-Step (All Levels)
1. [Detailed step with starting position]
2. [Detailed step with movement]
3. [Detailed step with engagement]
4. [Detailed step with hold/contraction]
5. [Detailed step with breathing]
6. [Detailed step with release/return]

### Beginner Variation
- **Duration per session**: [X minutes or reps]
- **Frequency**: [X times per week]
- **Intensity**: [Gentle/Moderate description]
- **Specific modifications**:
  - [Modification 1]
  - [Modification 2]
  - [Modification 3]

### Intermediate Variation
- **Duration per session**: [X minutes or reps]
- **Frequency**: [X times per week]
- **Intensity**: [Moderate description]
- **Specific modifications**:
  - [Modification 1]
  - [Modification 2]
  - [Modification 3]

### Advanced Variation
- **Duration per session**: [X minutes or reps]
- **Frequency**: [X times per week]
- **Intensity**: [High/Challenging description]
- **Specific modifications**:
  - [Modification 1]
  - [Modification 2]
  - [Modification 3]

## Common Mistakes
- **[Mistake 1]**: [Description and how to avoid]
- **[Mistake 2]**: [Description and how to avoid]
- **[Mistake 3]**: [Description and how to avoid]
- **[Mistake 4]**: [Description and how to avoid]
- **[Mistake 5]**: [Description and how to avoid]

## Expected Results
- **Timeline**:
  - [Week 1-2]: [What to expect]
  - [Week 3-4]: [What to expect]
  - [Month 2-3]: [What to expect]
  - [Month 6+]: [What to expect]
- **What to expect**:
  - [Result 1]
  - [Result 2]
  - [Result 3]

## Safety & Disclaimers

### Risk Level: [VERY LOW / LOW / MODERATE / HIGH / EXTREME]

### Who Should Avoid
- [Contraindication 1]
- [Contraindication 2]
- [Contraindication 3]

### Warning Signs to Stop
- [Warning sign 1]
- [Warning sign 2]
- [Warning sign 3]

### Potential Side Effects
- [Side effect 1]
- [Side effect 2]
- [Side effect 3]

### Medical Disclaimer
> **IMPORTANT:** This exercise is for informational purposes only. Consult a healthcare professional before starting any new facial exercise routine, especially if you have:
> - TMJ disorder or jaw pain
> - Recent facial surgery or injuries
> - Dental issues or braces
> - Skin conditions
> - [Exercise-specific conditions]
>
> Individual results may vary. This is not medical advice.

## Sources
- [Source 1 with URL if available]
- [Source 2 with URL if available]
- [Source 3 with URL if available]
```

---

## Phase 3: Safety Review (Mandatory)

After creating the exercise file, verify the Safety & Disclaimers section includes:

### Checklist
- [ ] Risk level assigned (VERY LOW / LOW / MODERATE / HIGH / EXTREME)
- [ ] Who Should Avoid section with contraindications
- [ ] Warning Signs to Stop section
- [ ] Potential Side Effects section
- [ ] Medical Disclaimer present
- [ ] Exercise-specific warnings added

### Risk Level Guidelines

| Level | Criteria | Examples |
|-------|----------|----------|
| **VERY LOW** | Gentle movements, no equipment, minimal muscle engagement | Face tapping, gentle massage, posture awareness |
| **LOW** | Moderate muscle engagement, some equipment, standard movements | Mewing, Gua Sha, face yoga |
| **MODERATE** | Intense muscle work, equipment required, technique-critical | Mastic gum, Jawzrsize, neck training, hard mewing |
| **HIGH** | Significant force, potential for injury if done wrong | None in recommended library |
| **EXTREME** | Dangerous, not recommended, documented for warning only | Bone smashing |

---

## Phase 4: Integration

### Update Master Files

1. **Update `docs/exercises/README.md`**:
   - Add exercise to appropriate category table
   - Update exercise count
   - Add to Exercise Database section by target area

2. **Update `docs/Exercise-Library-Summary.md`**:
   - Increment total exercise count
   - Update category counts
   - Add to recent additions section

3. **Update version number** if making significant changes

---

## Quality Standards

### All Exercises Must Have
- ✅ Unique, descriptive exercise name
- ✅ Clear category classification
- ✅ 5-6 detailed step-by-step instructions
- ✅ 3 distinct difficulty variations (Beginner/Intermediate/Advanced)
- ✅ Duration, frequency, AND intensity for each variation
- ✅ Scientific/mechanical explanation
- ✅ At least 4 common mistakes documented
- ✅ Realistic timeline expectations
- ✅ Complete Safety & Disclaimers section
- ✅ Medical disclaimer
- ✅ Source references

### Tone Guidelines
- **Professional but accessible** - Anyone should understand
- **Science-backed** - Reference mechanisms when possible
- **Realistic** - No false promises or exaggerated claims
- **Safety-first** - Warnings before instructions
- **Non-judgmental** - Even controversial techniques documented objectively

---

## Research Agent Instructions (Copy-Paste Ready)

```
Research and create a detailed exercise document for: [EXERCISE NAME]

Create file at: docs/exercises/[exercise-name].md

Follow this EXACT structure:
1. Overview (category, target areas, equipment)
2. How It Works (scientific explanation)
3. Instructions with:
   - 5-6 step-by-step instructions
   - Beginner variation (duration, frequency, intensity, modifications)
   - Intermediate variation (duration, frequency, intensity, modifications)
   - Advanced variation (duration, frequency, intensity, modifications)
4. Common Mistakes (4-5 mistakes with corrections)
5. Expected Results (timeline and outcomes)
6. Safety & Disclaimers (risk level, who should avoid, warnings, side effects, medical disclaimer)
7. Sources

Use agent-browser-cdp to research proper form, variations, and safety information.

Report back when complete.
```

---

## Single Agent Workflow (No Team)

If you don't need a full agent team, a single research agent can complete the entire process:

```
Create a comprehensive exercise document for [EXERCISE NAME] following the format in `docs/exercises/prompt.md`.

Steps:
1. Research the exercise using agent-browser-cdp (Google AI, YouTube, Reddit, medical sources)
2. Create file at `docs/exercises/[exercise-name].md` following the exact template structure
3. Include all required sections: Overview, How It Works, Instructions (with 3 variations), Common Mistakes, Expected Results, Safety & Disclaimers
4. Assign appropriate risk level (VERY LOW/LOW/MODERATE/HIGH/EXTREME)
5. Update `docs/exercises/README.md` to include the new exercise in the appropriate category

Maintain consistency with existing exercise documents in the folder.
```

---

## Example Exercise References

For quality reference, see these completed exercises:
- **Standard format:** `fish-face.md`
- **With equipment:** `gua-sha-facial-technique.md`
- **With risk warnings:** `hard-mewing.md`
- **Extreme/dangerous (warning only):** `bonesmashing.md`
- **Posture/lifestyle:** `scapular-retraction.md`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Feb 2026 | Initial prompt creation |

---

*This prompt ensures uniform, high-quality exercise documentation for the FaceMax app.*
