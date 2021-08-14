import re
import subprocess
import sys


def lint():
    subprocess.run(["black", "."])
    subprocess.run(["flake8"])


def test():
    subprocess.call(["pytest"])


def release(args=None):
    if not args:
        args = " ".join(sys.argv[1:2])
    subprocess.run(["poetry", "version", args])
    version = subprocess.run(["poetry", "version", "--short"], capture_output=True, text=True).stdout.split("\n")[0]

    with open("vasvscrapper/__init__.py", "w") as f:
        f.write(f'__version__ = "{version}"\n')

    subprocess.run(["git", "add", "."])
    message = f"Version upgraded to {version}"
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push", "origin", "main"])

    if re.match(r"^[0-9]+\.[0-9]+\.[0-9]+$", version):
        message = f"Released version {version}"
        print(message)

    else:
        message = f"Released prerelease version {version}"
        print(message)

    subprocess.run(["git", "tag", "-a", version, "-m", message])
    subprocess.run(["git", "push", "origin", version])
