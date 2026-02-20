import os
import re

# ==============================================================================
# PHASE 2: FACE-MAXING ETERNAL LEARNING LOOP PIPELINE
# ==============================================================================

def grokipedia_forager(topic_url):
    """
    1. The Forager
    Simulates scraping raw, unfiltered text from a trending live source like Grokipedia,
    YouTube transcripts, or Reddit forums about emerging looksmaxxing techniques.
    """
    print(f"--- [Forager] Active ---")
    print(f"Ingesting raw data stream from: {topic_url}")
    
    # Simulated raw, messy scrape about an underground/controversial technique
    raw_text = """
    Thumb Pulling (Maxilla Forward Growth)
    A highly controversial technique popularized in deep looksmaxxing forums. It involves placing the thumbs inside the mouth against the hard palate (behind the incisors) and applying forward and upward pressure. 
    Proponents claim it can physically move the maxilla bone forward over time, reversing midface recession. 
    However, dentists and orthodontists strongly advise against this. There is a massive risk of tooth displacement, root resorption, and severe palate damage. It should only be done if you accept severe dental risks.
    To do it: Wash hands. Place thumbs on the roof of mouth. Push forward and up for 30 seconds to 2 minutes daily. 
    """
    return raw_text

def weaver_synthesizer(raw_text):
    """
    2. The Weaver
    Simulates an LLM taking the raw, conversational text and structuring it into a 
    strict Agent Knowledge Module (AKM). It extracts hazards and creates GEPA alerts.
    """
    print("--- [Weaver] Active ---")
    print("Synthesizing raw data into strict AKM markdown structure...")
    
    # Simulated LLM transformation
    atomic_md = f"""# Thumb Pulling (Maxilla Forward Growth)

## Overview
Thumb Pulling is an advanced, controversial technique aimed at physically moving the maxilla bone forward to reverse midface recession.

**Category:** Bone Structure / Maxilla
**Difficulty:** Extreme (High Risk)
**Time per Session:** 30 seconds - 2 minutes
**Frequency:** Daily

---

> [!CAUTION] **WEAVER EXTRACTED WARNING:** Severe risk of tooth displacement, root resorption, and palate damage. Orthodontists strongly advise against manually applying force to the hard palate. Proceed at your own risk.

## Technique
1. **Hygiene:** Wash hands thoroughly with soap.
2. **Placement:** Place thumbs inside the mouth, flat against the hard palate directly behind the upper incisors.
3. **Execution:** Apply firm forward and upward pressure.
4. **Duration:** Hold the pressure for 30 seconds to 2 minutes.

## Expected Results
- **Theoretical:** Forward growth of the maxilla bone.
- **Risks:** Significant potential for damaging dental alignment and root structure.

---

*Document Version: 1.0 (Auto-Generated via Eternal Learning Loop)*
*Source: Grokipedia Live Ingestion*
"""
    
    filename = "thumb-pulling-maxilla.md"
    file_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'exercises', filename)
    with open(file_path, 'w') as f:
        f.write(atomic_md)
        
    print(f"Successfully wove raw data into {filename}")
    return filename

def indexer_update(filename, target_category):
    """
    3. The Indexer
    Automatically appends the newly created skill file to the CLAUDE.md index
    so the agent immediately gains this new knowledge passively.
    """
    print(f"--- [Indexer] Active ---")
    print(f"Integrating {filename} into CLAUDE.md zero-decision index under '{target_category}'")
    
    claude_md_path = os.path.join(os.path.dirname(__file__), '..', 'CLAUDE.md')
    
    with open(claude_md_path, 'r') as f:
        content = f.read()
        
    # Check if the category exists
    if f"|{target_category}:" in content:
        # Match the specific category line and extract the bracketed contents
        pattern = rf"\|{target_category}:{{([^}}]+)}}"
        match = re.search(pattern, content)
        if match:
            existing_files = match.group(1)
            # Add the new file if not already present
            if filename not in existing_files:
                new_files = f"{existing_files},{filename}"
                new_line = f"|{target_category}:{{{new_files}}}"
                content = content.replace(match.group(0), new_line)
    else:
        # Create a new category line at the end
        new_line = f"|{target_category}:{{{filename}}}"
        content = content + f"{new_line}\n"
        
    with open(claude_md_path, 'w') as f:
        f.write(content)
        
    print(f"Successfully indexed {filename}.")
    print("\n[SUCCESS] Agent Knowledge Graph expansion complete.")
    print("The Super Agent has evolved and is now aware of Thumb Pulling mechanics.")

def run_loop():
    url = "https://grokipedia.org/look/thumb-pulling"
    raw_data = grokipedia_forager(url)
    new_filename = weaver_synthesizer(raw_data)
    
    # We will let the Indexer create a new category dynamically for bone structure
    indexer_update(new_filename, target_category="10-bone-structure-and-advanced") 

if __name__ == "__main__":
    run_loop()
