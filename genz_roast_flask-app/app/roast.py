from __future__ import annotations
import random
import re
from html import escape

BLOCKLIST = [
    # Do not allow obvious identity-targeting or violence
    r"""(?i)\b(race|caste|relig|gender|sex|slur)\b""",
    r"""(?i)\b(hate|kill|violence)\b""",
]

SAFE_EMOJIS = ["🔥","💀","🫠","💅","🧃","🚩","🤡","🫣","🫨","📉","😵‍💫"]

ROAST_TEMPLATES = [
    "{n}, that confidence came with a 7‑day free trial.",
    "{n} walking in like a system update: promised vibes, delivered bugs.",
    "{n} is the human version of low‑battery mode.",
    "{n} serving hot takes from a microwave with the door open.",
    "{n} got main‑character energy on a background‑actor budget.",
    "{n}, your aura said ‘buffering…’ please connect to better choices.",
]

def _blocked(text: str) -> bool:
    return any(re.search(pat, text) for pat in BLOCKLIST)

def sanitize_name(name: str) -> str:
    name = (name or "mystery NPC").strip()
    name = re.sub(r"\s+", " ", name)[:40]
    return escape(name)

def generate_roast(name: str) -> dict:
    raw = name or "mystery NPC"
    if _blocked(raw):
        return {
            "roast": "Nice try, bestie. We roast vibes, not identities. 🚧",
            "emoji": "🚧",
            "name": "filtered",
        }
    n = sanitize_name(raw)
    roast = random.choice(ROAST_TEMPLATES).format(n=n)
    emoji = random.choice(SAFE_EMOJIS)
    return {"roast": roast, "emoji": emoji, "name": n}
