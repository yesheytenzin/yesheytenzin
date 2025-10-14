import platform
import psutil
import datetime

def generate_neofetch_block():
    # Collect system info
    uname = platform.uname()
    cpu = platform.processor() or "Unknown CPU"
    ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Customize your ASCII logo here if you want
    ascii_logo = r"""
          __     ______  _____
         \ \   / / __ \|  __ \
          \ \_/ / |  | | |__) |
           \   /| |  | |  _  /
            | | | |__| | | \ \
            |_|  \____/|_|  \_\
    """

    # System info block
    info = f"""
{ascii_logo}

**Yeshey Tenzin**
-------------------------
OS: {uname.system} {uname.release}
Kernel: {uname.version.split()[0]}
CPU: {cpu}
Arch: {uname.machine}
RAM: {ram_gb} GB
Python: {platform.python_version()}
Generated: {now}
"""

    return info.strip()


def update_readme():
    readme_path = "README.md"
    start_marker = "<!--NEOFETCH_START-->"
    end_marker = "<!--NEOFETCH_END-->"
    neofetch_content = generate_neofetch_block()

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

    before = readme.split(start_marker)[0]
    after = readme.split(end_marker)[1] if end_marker in readme else ""

    new_readme = f"{before}{start_marker}\n\n```\n{neofetch_content}\n```\n\n{end_marker}{after}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)

    print("✅ README updated with system info.")


if __name__ == "__main__":
    update_readme()

