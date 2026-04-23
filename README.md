# 🗺️ Map of Soil Science · Carte de la science des sols

An interactive, bilingual (FR · EN) map of the **diversity of soil science** — its
disciplines, sub-branches, cross-cutting themes and frontiers. Inspired by
Dominic Walliman's *[Domain of Science](https://www.youtube.com/@domainofscience)*
maps, and born from a brainstorm inside the
[Association Française pour l'Étude du Sol (AFES)](https://www.afes.fr/).

> **Live version:** if GitHub Pages is enabled on this repo, the map is served at
> `https://<your-user>.github.io/map-of-soil-science/`.
> Otherwise just open `index.html` in any browser.

## ✨ What's in the map

- **10 domain zones** laid out on a 16:9 canvas, organised as:
  1. Pédogenèse & genèse des sols · Pedogenesis & Soil Genesis
  2. Morphologie, classification & cartographie · Morphology, Classification & Mapping
  3. Physique & mécanique du sol · Soil Physics & Mechanics
  4. Chimie & biogéochimie · Soil Chemistry & Biogeochemistry
  5. Biologie, microbiologie & écologie · Soil Biology, Microbiology & Ecology
  6. Sols & plantes (édaphologie) · Soils & Plants
  7. Gestion & usage des sols · Soil Management & Land Use
  8. Sols anthropogéniques · Anthropogenic Soils
  9. Sols, environnement & climat · Soils, Environment & Climate
  10. Sols & société · frontières · Soils & Society · Frontiers
- **~85 named disciplines** with bilingual definitions and ~300 sub-topics
- **8 cross-cutting bridge themes** (Soil Carbon & Climate, Soil-Plant-Water
  Continuum, Critical Zone, Soil Security, Digital Soil Assessment,
  Governance & Policy, Ethnopedology, Risk & Contamination) that light up
  related nodes across zones
- **Interactive** — language toggle (FR / EN / FR+EN), click any node for a
  definition panel with sub-branches and related fields, cross-zone link
  visualisation

## 🧭 How it is organised

The taxonomy was informed by:

- [IUSS Divisions & Commissions](https://www.iuss.org/organisation-people/organisation/divisions/)
- [SSSA Divisions](https://www.soils.org/membership/divisions)
- [EGU Soil System Sciences](https://www.egu.eu/sss/)
- [AFES Commissions thématiques](https://www.afes.fr/nos-missions/valoriser/commissions-thematiques-de-lafes/)
- [FAO — World Reference Base for Soil Resources (WRB)](https://www.fao.org/soils-portal/data-hub/soil-classification/world-reference-base/en/)
- *Encyclopedia of Soil Science* (R. Lal, ed.)
- N. C. Brady & R. R. Weil, *The Nature and Properties of Soils*

## 🗂️ Repository layout

```
.
├── index.html                       ← the current map (v2) — GitHub-Pages entrypoint
├── map-of-soil-science-v2.html      ← same file, versioned name
├── archive/
│   └── map-of-soil-science-v1.html  ← first 6-zone draft (kept for history)
├── LICENSE                          ← CC BY-SA 4.0
└── README.md
```

The map is a **single-file HTML artefact** — no build step, no dependencies.
Open it, fork it, remix it.

## 🤝 Contributing

This is an early draft and every soil scientist will rightly want to argue
about the groupings. Issues and pull requests are welcome — in particular:

- **Missing disciplines or sub-branches** you think deserve a node
- **Groupings** you would rearrange (what belongs in which zone?)
- **Bilingual wording** corrections (FR or EN)
- **Cross-cutting themes** you would add

## 🙏 Credits

- **Thomas Fungenzi** — Vice-President, AFES (maintainer)
- **Frédéric Feder** (CIRAD) & **Philippe Billet** (Univ. Lyon 3) — original
  AFES brainstorm, February 2023
- **Christophe Ducommun** (Institut Agro) — later contributor, 2024
- Inspiration: **Dominic Walliman** / *Domain of Science*

## 📄 License

Content and code released under [Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
Reuse freely, with attribution; share-alike if you modify.
