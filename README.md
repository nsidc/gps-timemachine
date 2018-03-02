Getting Started
---

If this is a new project you will need to complete the following steps (assuming you just created this from the cookiecutter template):

0. Add a project description below.
1. Add the actual project source in `./gps-timemachine`
2. Edit `./recipe/meta.yaml` adding entry points and/or test commands, and dependencies.
3. Update the conda `./environment.yml` with the project's correct
   dependencies. The default values may not be what you need.
4. Add any runtime commands to `./tasks/run.py`.
5. Remove this `Getting Started` section.

gps-timemachine
---

Describe the project here!

[![CircleCI](https://circleci.com/bb/nsidc/gps-timemachine.svg?style=svg)](https://circleci.com/bb/nsidc/gps-timemachine)

[![Anaconda-Server Badge](https://anaconda.org/nsidc/gps-timemachine/badges/version.svg)](https://anaconda.org/nsidc/gps-timemachine)
[![Anaconda-Server Badge](https://anaconda.org/nsidc/gps-timemachine/badges/license.svg)](https://anaconda.org/nsidc/gps-timemachine)
[![Anaconda-Server Badge](https://anaconda.org/nsidc/gps-timemachine/badges/downloads.svg)](https://anaconda.org/nsidc/gps-timemachine)
[![Anaconda-Server Badge](https://anaconda.org/nsidc/gps-timemachine/badges/installer/conda.svg)](https://conda.anaconda.org/nsidc)

Prerequisites
---

* [Miniconda3](https://conda.io/miniconda.html)

Development
---

Install dependencies:

    $ conda env create -f=./environment.yml
    $ source activate gps-timemachine

Workflow
---

TL;DR: Use
[GitHub Flow](https://guides.github.com/introduction/flow/index.html).

In more detail:

1. Create a feature branch.
2. Create commits on that branch and open a PR.
3. The feature branch will get built on CircleCI with each push to
   BitBucket.
4. Bump the version to the next anticipated release version (see
   below).

        $ bumpversion <major|minor|patch>

5. When the feature PR is merged, master will get built on CircleCI,
   and the 'dev' version of the package will be published
   to [Anaconda.org](https://anaconda.org/) with the dev label.
6. Do a release on master when you are ready (See below), and a
   version of the package will be published with the main label.

Releasing
---

1. Update the CHANGELOG.
2. Create a version tag in git
3. Push

        $ git push origin master --tags

Installing
---
To install and use it in another project:

    $ conda install gps-timemachine

License
---

Copyright 2016 National Snow and Ice Datacenter (NSIDC)
<programmers@nsidc.org>
