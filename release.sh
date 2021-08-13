poetry run pytest
poetry version $1
VERSION="$(poetry version -s)"

echo "__version__ = \"$VERSION\"" > vasvscrapper/__init__.py

git add .
git commit -m "Version upgraded to v$VERSION"
git push origin main

if [[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]
then
  echo "Released version $VERSION"
  git tag -a "v$VERSION" -m "Released version v$VERSION"
else
  echo "Released prerelease version $VERSION"
  git tag -a "v$VERSION" -m "Released prerelease version v$VERSION"
fi

git push origin "v$VERSION"
