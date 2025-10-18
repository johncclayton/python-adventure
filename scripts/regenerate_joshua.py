from pathlib import Path

from joshua_data import EXERCISES

ROOT = Path(__file__).resolve().parents[1] / "joshua"
EX_DIR = ROOT / "exercises"
SOL_DIR = ROOT / "solutions"

for folder in (EX_DIR, SOL_DIR):
    folder.mkdir(parents=True, exist_ok=True)
    for path in folder.glob("*"):
        if path.is_file():
            path.unlink()

TEMPLATE = """1. **Purpose** – {purpose}
2. **Recipe List**

| Concept | Syntax / Example | Docs |
| --- | --- | --- |
| {concept} | `{syntax}` | [{concept}]({docs}) |

3. **Adventure Story / Problem** – {story} {task}

4. **Example Input/Output**

```
{example}
```
"""

for entry in EXERCISES:
    number = entry["number"]
    slug = entry["slug"]
    name = f"{number}-{slug}.md"
    content = TEMPLATE.format(**entry)
    (EX_DIR / name).write_text(content, encoding="utf-8")

    solution_path = SOL_DIR / f"{number}-{slug}.py"
    solution_path.write_text(entry["solution"] + "\n", encoding="utf-8")

print(f"Wrote {len(EXERCISES)} exercises for Joshua.")
