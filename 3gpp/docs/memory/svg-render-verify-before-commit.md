---
name: svg-render-verify-before-commit
description: SVG diagrams must be visually verified (Y-coordinate scan or PNG preview) before declaring done — never trust code-only generation
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0505a215-ab14-46a7-bd95-9e48fe5839d3
---

# SVG Diagram: Verify Before Commit

**What happened:** On 2026-07-23, a circular buffer interleaving SVG was generated via Python script and embedded into T3.2 without visual verification. The figure had text overlapping because Y-coordinate spacing was too tight — arrows, labels, and cells were crammed into a 4px vertical range. The user caught it immediately.

**Why:** Writing the generation script correctly ≠ producing a visually correct output. SVG layout depends on manual coordinate arithmetic; a 10px miscalculation causes text-on-text or text-on-line collisions that are invisible in the source code but obvious in the rendered image.

**How to apply:** After generating ANY SVG (chart, diagram, layout):

1. **Y-coordinate scan** (MANDATORY, 15 seconds):
   ```bash
   python3 -c "
   import re
   with open('diagram.svg') as f:
       svg = f.read()
   elems = []
   for m in re.finditer(r'<(text|rect|line)[^>]*y[12]?=\"([\d.]+)\"[^>]*>', svg):
       elems.append((float(m.group(2)), m.group(0)[:6], m.group(0)[:80]))
   elems.sort()
   for y, t, full in elems:
       print(f'{y:6.0f}  {t}  {full}')
   "
   ```
2. **Check gaps between layers** — each distinct Y-group should have ≥8px clearance from the next
3. **PNG preview** (optional but recommended for complex diagrams): convert SVG → PNG via `cairosvg` or ImageMagick and visually inspect
4. **Only then** embed into the document

This applies to: Mermaid `.mmd`, PlantUML `.puml`, Wavedrom `.json`, and hand-coded SVG via Python.
