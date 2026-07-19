import json
import random

with open("Assets/pairs.json", encoding="utf-8") as f:
    pairs = json.load(f)

item = random.choice(pairs)

header = f"""<p align="center">
  <img src="{item['gif']}" width="700" />
  <br>
  <i>
    <b>{item['quote']}</b>
  </i>
</p>

---
"""

with open("generated_header.md", "w", encoding="utf-8") as f:
    f.write(header)