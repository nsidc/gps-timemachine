# Workflow

TL;DR:  Use
[GitHub Flow](https://guides.github.com/introduction/flow/index.html).

In more detail:

1. Create a feature branch.
2. Create and push commits on that branch.
3. The feature branch will get tested on GHA with each push.
4. Update the CHANGELOG with description of changes.
5. Create a Pull Request on GitHub.
6. When the feature PR is merged, main will get built on GHA.


# Releasing

1. Update the CHANGELOG to list the new version.
2. Add files and commit

        $ git add CHANGELOG.md ...
        $ git commit -m "Release v.X.Y.Z"

3. Bump the version to the desired level:

        $ bumpversion (major|minor|patch)

4. Push

        $ git push origin main --tags

GHA will build the conda package and publish it to anaconda.org.
