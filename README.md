gps-timemachine
---

GPS Time Machine provides the ability to convert a date and GPS time
(hours, minutes, seconds, fractions of second) to a datetime object.
GPS Time Machine adjusts for the offset between UTC and GPS time based
on the number of leap seconds for the specified date. Because the gap
between UTC and GPS times shift unpredictably based on when leap
seconds are added by the [International Earth Rotation and Reference
Systems Service
(IERS)](https://www.iers.org/IERS/EN/Home/home_node.html), GPS Time
Machine uses data from the U.S. Naval Observatory for this
adjustment. See [NOTES](NOTES.md) for more information.

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

Copyright 2018 National Snow and Ice Datacenter (NSIDC)
<programmers@nsidc.org>.

This software is licensed under the MIT License. See [LICENSE
File](LICENSE).
