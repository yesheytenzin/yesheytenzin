import platform
import psutil
import datetime

# === CONFIG ===
NAME = "Yeshey Tenzin"
SYSTEM = "Arch Linux"
LANG_PROG = "Python, JavaScript, C++"
LANG_COMP = "HTML, CSS, SQL"
LANG_REAL = "English, Dzongkha"
HOBBIES_SOFT = "AI Research, ML Projects"
HOBBIES_HARD = "Electronics, IoT Automation"
EMAIL = "yeshey.tenzin@example.com"
GITHUB = "yesheytenzin"
LINKEDIN = "yeshey-tenzin"
IDE = "Neovim, VSCode"
UPTIME = "21 years, 3 months, 12 days"
OS_LIST = "Arch Linux, Android 14"
STARS = 120
REPOS = 45
COMMITS = 1500
FOLLOWERS = 210
LINES_ADDED = 123_456
LINES_REMOVED = 23_890

# === GENERATION ===

def load_ascii_art():
    with open("arch.txt", "r", encoding="utf-8") as f:
        return f.read()

def generate_profile():
    ascii_art = load_ascii_art()
    uname = platform.uname()
    ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    right_block = f"""
{name_line(NAME)}
OS: ................. {OS_LIST}
Uptime: ............. {UPTIME}
Host: ............... Custom Build
Kernel: ............. {uname.release}
IDE: ................ {IDE}

Languages.Programming: ..... {LANG_PROG}
Languages.Computer: ......... {LANG_COMP}
Languages.Real: ............. {LANG_REAL}

Hobbies.Software: ........... {HOBBIES_SOFT}
Hobbies.Hardware: ........... {HOBBIES_HARD}

Contact
-------
Email: ...................... {EMAIL}
LinkedIn: ................... {LINKEDIN}
GitHub: ..................... {GITHUB}

GitHub Stats
------------
Repos: {REPOS} | Stars: {STARS}
Commits: {COMMITS} | Followers: {FOLLOWERS}
Lines of Code: {LINES_ADDED:,}+ / {LINES_REMOVED:,}−
RAM: {ram_gb} GB
Generated: {date_now}
"""

    # Merge ASCII + right panel side by side
    ascii_lines = ascii_art.splitlines()
    info_lines = right_block.splitlines()
    max_left = max(len(l) for l in ascii_lines)
    merged = []
    for i in range(max(len(ascii_lines), len(info_lines))):
        left = ascii_lines[i] if i < len(ascii_lines) else ""
        right = info_lines[i] if i < len(info_lines) else ""
        merged.append(f"{left.ljust(max_left + 4)}{right}")
    return "\n".join(merged)

def name_line(name):
    return f"{name} " + "_" * (60 - len(name))

def update_readme():
    start = "<!--PROFILE_START-->"
    end = "<!--PROFILE_END-->"
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    profile_block = generate_profile()
    before = content.split(start)[0]
    after = content.split(end)[1] if end in content else ""
    new_content = f"{before}{start}\n\n```\n{profile_block}\n```\n\n{end}{after}"
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ README updated successfully!")

if __name__ == "__main__":
    update_readme()

