# obsidian — Full-Stack Teaching Knowledge Base for 3GPP LTE/NR Decoding Chains

A full-stack teaching Obsidian knowledge base for the 3GPP LTE/NR decoding chain: from mathematical foundations, physical-layer links, and channel coding algorithms, to floating-point simulation, fixed-point models, and RTL microarchitecture & verification — bridging "theory → algorithm → hardware implementation" end to end.

## Repository Layout

```
├── 3gpp/                    # Core knowledge base (lectures / concepts / audits / tools)
│   ├── docs/L0_协议阅读引导/  # Protocol reading map, master glossary (254 terms + 104 concept index)
│   ├── docs/L1_基础/         # Math foundations, OFDM & soft demodulation, CRC/segmentation, decoding theory, HW basics
│   ├── docs/L2_协议算法/     # Decoder protocols & algorithms (Turbo/LDPC/Polar), MIMO reception, probabilistic shaping
│   ├── docs/L3_工程实现/     # Decoder engineering (simulation/fixed-point/RTL/verification), receiver-link engineering budgets
│   ├── docs/concepts/        # Concept graph (71+ concept notes)
│   ├── docs/audits/          # Audit ledgers & reviews
│   ├── sim/ tools/ tests/    # Python simulation, audit toolchain, unit tests
│   ├── CLAUDE.md             # Session hard rules
│   ├── 合规与遵从.md          # 23 Hard Constraints
│   ├── 项目规则与记忆索引.md   # Rules / writing conventions / sync checklist
│   └── README.md             # Detailed knowledge-base documentation (Chinese)
├── .obsidian/               # Obsidian app configuration
└── 3gpp/3GPP_Rel19/         # Rel-19 specs and structured extraction
```

## Quick Start

1. **Detailed docs**: see [`3gpp/README.md`](3gpp/README.md) (structure / lecture system / reading path / quality system)
2. **Reading entry**: `3gpp/docs/3GPP_讲义入口.md`
3. **Terminology lookup**: `3gpp/docs/L0_协议阅读引导/L0_terminology_glossary.md`
4. **Lecture system**: L1 foundations (T1-T5 + TX1-TX5 TX mirror) → L2 protocol/algorithms (M6-M16: decoding/control-plane/uplink/scheduling) → L3 engineering (T17-T23: decoder/RX chain/backend), all complete ✅ (153 lectures + 6 entry/glossary spec files + 106 concept notes)

## Quality System

- Compliance baseline: 23 Hard Constraints (`3gpp/合规与遵从.md`)
- SVG mandatory validation: geometry audit R1-R11 (boundary gaps ≥8px, no overlap)
- Lecture audits: term pairing / LaTeX rendering / depth / headings
- Code comments: DOXYGEN style enforced
- Full-base sync: 8 sync categories (terms/entries/numbers/assets/paths/ledgers) — see `3gpp/项目规则与记忆索引.md` §6

## Usage

This repository is an **Obsidian vault**. Open it with Obsidian for the full experience (`[ [wikilink]]` graph navigation, backlinks, relationship graphs).

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

## Contribution

1. New content (concept notes / lectures / terms) must be checked against the sync checklist item by item
2. Code must carry DOXYGEN comments and pass tests
3. Push after commit (gitee 2FA accounts require a personal access token)
