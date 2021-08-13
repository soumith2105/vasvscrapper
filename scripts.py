import subprocess


def lint():
    subprocess.run(["black", "."])
    subprocess.run(["flake8"])


def test():
    subprocess.call("pytest")


def release():
    subprocess.run("./release.sh", shell=True, stdin=subprocess.PIPE)
