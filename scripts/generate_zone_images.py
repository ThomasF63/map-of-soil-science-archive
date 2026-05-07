"""Generate the 10 zone illustrations for Map of Soil Science via Gemini 2.5 Flash Image.

Reads the API key from the GEMINI_API_KEY environment variable. Uses
afes_z1_pedogenesis.png as a style reference to keep all 10 outputs
visually consistent. Outputs replace the existing afes_zN_*.png files.

Usage (from map-soil-science/):
    $env:GEMINI_API_KEY = "..."
    python scripts/generate_zone_images.py            # all 10
    python scripts/generate_zone_images.py z2 z9       # selected zones only
"""

import os
import sys
from pathlib import Path

from google import genai
from google.genai import types

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
REFERENCE = ASSETS / "afes_z1_pedogenesis.png"

MODEL = "gemini-2.5-flash-image"

STYLE_HEADER = (
    "Generate a square 1:1 illustration in the EXACT same flat painted style "
    "as the reference image attached. The palette must use only these earthy "
    "tones: deep warm brown #3B322C, muted olive green #657D58, warm beige "
    "and dusty sage, with optional small accents of soft amber #E89B48, "
    "rust terracotta #C46B42, and dusty blue #6B9AC4. Background outside the "
    "illustrated subject must be plain off-white #F7F5F0 or pure white. "
    "Use simplified painted shapes with subtle texture, flat shading, gentle "
    "edges, no harsh outlines. Composition must be centered with comfortable "
    "breathing space.\n\n"
    "STRICT CONSTRAINTS — the output MUST NOT contain any of the following: "
    "no text of any kind, no letters, no words, no numbers, no labels, no "
    "captions, no titles, no logos, no AFES branding, no callout arrows "
    "with labels, no chemical formulas, no map legends, no scale bars, no "
    "compass roses, no symbols (no C, N, P chemical letters, no CO2, no "
    "math), no UI/diagram elements, no human faces. Pure illustration only.\n\n"
    "SUBJECT: "
)

ZONE_PROMPTS = {
    "z1": (
        "afes_z1_pedogenesis.png",
        "A vertical soil profile cross-section showing distinct horizons from "
        "leaf litter at the top, through dark organic topsoil, lighter "
        "subsoil, to fragmented bedrock at the bottom. Tree roots descend "
        "through the layers, fallen leaves and small twigs rest on the surface, "
        "and a tiny seedling sprouts on top. Painterly, naturalistic.",
    ),
    "z2": (
        "afes_z2_morphology.png",
        "A gentle aerial three-quarter view of a rolling rural landscape with "
        "irregular patches of different soil types shown as flat painted areas "
        "in browns, olive greens and dusty sage. Smooth contour-like ridges in "
        "the terrain (purely as natural relief, NOT as drawn diagram lines). "
        "A small soil auger or thin vertical sampling tool is gently embedded "
        "into one hillside. Quiet, naturalistic, no map elements.",
    ),
    "z3": (
        "afes_z3_physics.png",
        "A textured cross-section block of soil showing aggregated soil peds "
        "and crumbs stacked together with visible pore spaces between them. "
        "A few small water droplets sit between particles, suggesting "
        "infiltration. Painterly soil structure, three-dimensional but flat-shaded, "
        "no diagram arrows.",
    ),
    "z4": (
        "afes_z4_chemistry.png",
        "A close-up painted view of soil particles and humus fragments with "
        "tiny abstract dots and curved organic shapes drifting between them, "
        "suggesting nutrient exchange. Roots threaded through the scene with "
        "small painted bead-like nodules. Entirely abstract and painterly — "
        "no molecules drawn as ball-and-stick, no chemistry letters.",
    ),
    "z5": (
        "afes_z5_biology.png",
        "A horizontal cross-section of soil bursting with hidden life: an "
        "earthworm tunneling through, painted mycorrhizal fungal threads "
        "weaving among root tips, tiny silhouettes of soil arthropods (springtails, "
        "mites) at home in the substrate, and small painted bacteria-shape "
        "blobs nestled near roots. Naturalistic and serene.",
    ),
    "z6": (
        "afes_z6_edaphology.png",
        "A single healthy plant with a vigorous root system reaching into "
        "soil. Above ground: simplified leaves and a slim stem. Below ground: "
        "a fine root network spreading through painted soil layers. Subtle "
        "color gradients between roots and soil suggest water and nutrient "
        "exchange — no arrows, no diagram lines.",
    ),
    "z7": (
        "afes_z7_management.png",
        "A pastoral agricultural landscape painted in the same flat style: "
        "terraced fields and strips of crops in browns and olive greens, a "
        "hedgerow, a small simplified farmhouse silhouette in the distance, "
        "gentle rolling hills. No text, no signage, no roads with labels.",
    ),
    "z8": (
        "afes_z8_anthropogenic.png",
        "A cross-section meeting urban and natural ground: above the surface, "
        "the corner of a simplified building foundation and a strip of asphalt "
        "meet a patch of grass. Below the surface, a technosol layer mixes "
        "soil with painted fragments of brick, broken ceramic and construction "
        "debris, transitioning into deeper natural soil layers below. Quiet, "
        "painterly, no arrows or labels.",
    ),
    "z9": (
        "afes_z9_environment.png",
        "A wide pastoral landscape suggesting soil's role in the climate and "
        "water cycle: hills with trees, soft simplified clouds, gentle rain "
        "lines falling on the canopy, and below-ground a glimpse of deep "
        "soil layers where roots reach down. Natural and peaceful, no diagram "
        "arrows, no chemical labels, no cycle annotations.",
    ),
    "z10": (
        "afes_z10_society.png",
        "A pair of cupped hands gently holding a clump of dark soil from which "
        "a small green seedling sprouts. Soft pastoral landscape silhouette "
        "in the background as a quiet horizon. Symbolic and poetic. No "
        "people's faces visible (only the hands), no signage, no logo.",
    ),
}


def load_reference() -> bytes:
    if not REFERENCE.exists():
        sys.exit(f"Reference image not found: {REFERENCE}")
    return REFERENCE.read_bytes()


def generate_zone(client: genai.Client, zone_id: str, reference_bytes: bytes) -> Path:
    filename, subject = ZONE_PROMPTS[zone_id]
    output_path = ASSETS / filename

    prompt = STYLE_HEADER + subject

    print(f"  -> generating {zone_id} ({filename})...", flush=True)

    response = client.models.generate_content(
        model=MODEL,
        contents=[
            types.Part.from_bytes(data=reference_bytes, mime_type="image/png"),
            prompt,
        ],
    )

    image_bytes = None
    for part in response.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            image_bytes = part.inline_data.data
            break

    if image_bytes is None:
        text_blocks = [p.text for p in response.candidates[0].content.parts if getattr(p, "text", None)]
        raise RuntimeError(
            f"No image returned for {zone_id}. Text response: {' | '.join(text_blocks) or '(none)'}"
        )

    output_path.write_bytes(image_bytes)
    print(f"    saved {output_path.relative_to(ROOT)} ({len(image_bytes)//1024} KB)", flush=True)
    return output_path


def main(argv: list[str]) -> int:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY env var is not set. Aborting.")

    requested = [z.lower() for z in argv[1:]] or list(ZONE_PROMPTS.keys())
    unknown = [z for z in requested if z not in ZONE_PROMPTS]
    if unknown:
        sys.exit(f"Unknown zones: {unknown}. Valid: {list(ZONE_PROMPTS.keys())}")

    print(f"Generating {len(requested)} zone(s): {requested}")
    client = genai.Client(api_key=api_key)
    reference_bytes = load_reference()

    failures = []
    for zone_id in requested:
        try:
            generate_zone(client, zone_id, reference_bytes)
        except Exception as exc:
            print(f"  [error] {zone_id}: {exc}", flush=True)
            failures.append((zone_id, exc))

    if failures:
        print(f"\nDone with {len(failures)} failure(s):")
        for zid, exc in failures:
            print(f"  - {zid}: {exc}")
        return 1
    print("\nAll done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
