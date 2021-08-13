import os


def lint():
    os.system("black . && flake8")


def test():
    os.system("pytest")


def release():
    os.system("./release.sh")
