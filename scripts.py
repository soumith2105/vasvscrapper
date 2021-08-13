import os
import subprocess


def lint():
    os.system("black . && flake8")


def test():
    subprocess.call("pytest")


def release():
    subprocess.call("./release.sh", shell=True)
