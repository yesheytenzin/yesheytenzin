
✅ **Important:** Those comment markers (`<!--NEOFETCH_START-->`, `<!--NEOFETCH_END-->`) are used by the script to insert your system block.

---

## 🐍 Step 4: Create `generate_neofetch.py`

In the same directory (`yesheytenzin/`), create a file:

**`generate_neofetch.py`**
```python
import datetime
from pathlib import Path

# ===============================
# Configuration (edit these)
# ===============================
USERNAME = "yesheytenzin"
OS_NAME = "Debian GNU/Linux x86_64"
SHELL = "fish"
RESOLUTION = "1920x1080 @144Hz"
TERMINAL = "GitHub"
LANGUAGES = "Python, JavaScript, C++, SQL"
PROJECTS = "AI Pest Detection, Smart Greenhouse Automation"
MOOD = "🚀 Always building cool things"
# ===============================


ASCII_ART = r"""
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
"""

def generate_neofetch_block():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""{ASCII_ART}

{USERNAME}@github
----------------------------
OS: {OS_NAME}
Shell: {SHELL}
Resolution: {RESOLUTION}
Terminal: {TERMINAL}
Languages: {LANGUAGES}
Projects: {PROJECTS}
Updated: {now}
Mood: {MOOD}
"""

def update_readme():
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")
    new_block = generate_neofetch_block()

    start_marker = "<!--NEOFETCH_START-->"
    end_marker = "<!--NEOFETCH_END-->"

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("Markers not found in README.md")

    updated_content = (
        content[:start_idx + len(start_marker)]
        + "\n" + new_block + "\n"
        + content[end_idx:]
    )

    readme_path.write_text(updated_content, encoding="utf-8")
    print("✅ README.md updated successfully with new Neofetch block!")

if __name__ == "__main__":
    update_readme()

