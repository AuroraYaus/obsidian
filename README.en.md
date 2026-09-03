# obsidian — Full-Stack Teaching Knowledge Base for 3GPP LTE/NR Decoding Chains

A full-stack teaching Obsidian knowledge base for the 3GPP LTE/NR decoding chain: from mathematical foundations, physical-layer links, and channel coding algorithms, to floating-point simulation, fixed-point models, and RTL microarchitecture & verification — bridging "theory → algorithm → hardware implementation" end to end.

## Repository Layout

```
├── CLAUDE.md                  # Workspace rules entry (required-reading list / behavior constraints)
├── .claude/                   # Project rules + user-level SKILL executables copy (skills/, synced from ~/.claude/skills/)
├── docs/rules/                # User global rules mirror copy (full text of ~/.claude/CLAUDE.md, synced on update)
├── 3gpp/                      # Core knowledge base (lectures / concepts / audits / tools)
│   ├── docs/L0_协议阅读引导/    # Protocol reading map, master glossary (255 terms + 114 concept index)
│   ├── docs/L1_基础/           # Math foundations, OFDM & soft demodulation, CRC/segmentation, decoding theory, HW basics
│   ├── docs/L2_协议算法/       # Decoder protocols & algorithms (Turbo/LDPC/Polar), MIMO reception, probabilistic shaping
│   ├── docs/L3_工程实现/       # Decoder engineering (simulation/fixed-point/RTL/verification), receiver-link engineering budgets
│   ├── docs/concepts/          # Concept graph (114 concept notes, six-section template)
│   ├── docs/audits/            # Audit ledgers, lessons-learned library (25 items) & reviews
│   ├── docs/memory/            # Authoritative in-project auto-memory copy (travels with the folder, CLAUDE.md rule 17)
│   ├── sim/ tools/ tests/      # Python simulation, audit toolchain, unit tests
│   ├── CLAUDE.md               # Session hard rules (17 rules)
│   ├── 合规与遵从.md            # 23 Hard Constraints
│   ├── 项目规则与记忆索引.md     # Rules / writing conventions / sync checklist
│   └── README.md               # Detailed knowledge-base documentation (Chinese)
├── .obsidian/                 # Obsidian app configuration
└── 3gpp/3GPP_Rel19/           # Protocol evidence data (optional clone, see "Protocol evidence data")
```

## Quick Start

1. **Detailed docs**: see [`3gpp/README.md`](3gpp/README.md) (structure / lecture system / reading path / quality system)
2. **Reading entry**: `3gpp/docs/3GPP_讲义入口.md`
3. **Terminology lookup**: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`
4. **Lecture system**: L1 foundations (T1-T5 + TX1-TX5 TX mirror) → L2 protocol/algorithms (M6-M16: decoding/control-plane/uplink/scheduling) → L3 engineering (T17-T23: decoder/RX chain/backend), all complete ✅ (156 lectures + 6 entry/glossary files + 114 concept notes)

## Quality System

- Compliance baseline: 23 Hard Constraints (`3gpp/合规与遵从.md`)
- SVG mandatory validation: geometry audit R1-R11 (boundary gaps ≥8px, no overlap)
- Lecture audits: term pairing / LaTeX rendering / depth / headings
- Code comments: DOXYGEN style enforced
- Lessons-learned library: `3gpp/docs/audits/lessons/` (25 items; every correction is solidified and pushed with the repo)
- Full-base sync: 8 sync categories (terms/entries/numbers/assets/paths/ledgers) — see `3gpp/项目规则与记忆索引.md` §6

## Usage

This repository is an **Obsidian vault**. Open it with Obsidian for the full experience (`[[wikilink]]` graph navigation, backlinks, relationship graphs).

### Downloading & Installing Obsidian

| Platform | How to get it |
|---|---|
| **Official site (recommended)** | [obsidian.md](https://obsidian.md/) → **Download** button, or go directly to [obsidian.md/download](https://obsidian.md/download) |
| Windows | `.exe` installer from the site (or Microsoft Store: search "Obsidian") |
| macOS | `.dmg` from the site (or App Store: search "Obsidian") |
| Linux | AppImage / Snap / Flatpak / deb / rpm (Debian/Ubuntu: `snap install obsidian`) |
| iOS / Android | App Store / Google Play: search "Obsidian" (read & sync on mobile) |

> Obsidian is **free for personal use** (commercial use requires a license). A vault is just a folder — clone this repo and **"Open folder as vault"** — no extra setup needed.

### Opening This Knowledge Base

1. Clone: `git clone https://gitee.com/aurorayaus/obsidian.git`
2. Obsidian → **Open folder as vault** → select the cloned `obsidian` folder
3. Start reading from `3gpp/docs/3GPP_讲义入口.md`; the file tree follows `L0_协议阅读引导 → L1_基础 → L2_协议算法 → L3_工程实现`

- Lecture bodies embed runnable numpy verification snippets to reproduce numerical results
- Concepts and lectures are bidirectionally linked; each concept note is a standalone six-section teaching unit

## Protocol Evidence Data

`3gpp/3GPP_Rel19/` holds Rel-19 protocol sources and structured extraction — the local reference for lecture protocol anchors, concept-note "Protocol Anchors" sections, and evidence tables (`3gpp/docs/audits/*_evidence.md`). This directory has been split into a **separate data repository** (Gitee `gitee.com/aurorayaus/3gpp_docs`, GitHub mirror `AuroraYaus/3gpp_docs`); the main repo no longer tracks it — cloning the main repo does not include this directory, so it must be configured separately.

### Setup

1. Run the clone from the repository root (`obsidian/`). **The target must be exactly `3gpp/3GPP_Rel19/`**:

   ```bash
   git clone https://gitee.com/aurorayaus/3gpp_docs.git 3gpp/3GPP_Rel19
   ```

   If Gitee is unreachable, use the GitHub mirror: `git clone https://github.com/AuroraYaus/3gpp_docs.git 3gpp/3GPP_Rel19`.

2. Verify the setup — the directory structure should be complete:

   ```text
   3gpp/3GPP_Rel19/
   ├── manifest.csv          # Spec numbers, ZIP names, SHA-256, official URLs
   ├── Rel19_协议下载清单.md   # Spec / ZIP / official URL lookup table
   ├── archive/              # Official ZIP downloads
   ├── specs/                # Extracted official Word documents
   └── processed/            # Structured extraction (manifest.json / extraction_report.md / Rel19_processed_目录入口.md)
   ```

   The main repo's `git status` should also remain clean (the root `.gitignore` ignores this directory).

3. Later data updates: `3GPP_Rel19/` is its own git repository — run `git pull` inside that directory.

### Placement Warning

The clone must include the target path `3gpp/3GPP_Rel19`. Placing it elsewhere (e.g. directly at the repository root as `3GPP_Rel19/`) causes:

1. All protocol-anchor references to break — links in `3GPP_Rel19_资料入口总览.md`, the "Protocol Anchors" sections of concept notes, and lecture evidence tables resolve relative to `3gpp/3GPP_Rel19/`;
2. The data directory to become an untracked directory in the main repo (~80,000 files) — the root `.gitignore` rule only matches `3gpp/3GPP_Rel19/`, so `git add .` would accidentally commit the data into the main repo.

Without the data repo, lecture and concept-note bodies are unaffected (still fully readable); only protocol-anchor jumps break.

## Contribution

1. New content (concept notes / lectures / terms) must be checked against the sync checklist item by item
2. Code must carry DOXYGEN comments and pass tests
3. Push after commit (gitee 2FA accounts require a personal access token)
