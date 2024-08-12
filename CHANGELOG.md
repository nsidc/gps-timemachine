# v1.1.4 (2024-08-12)

* Update URL for `tai-utc.dat` leap-seconds file.

# v1.1.3 (2020-12-21)

* Exposing data file so that external clients can make use of it when requesting
  the leap second data.

# v1.1.2 (2020-12-21)

* Fixed a bug where the data file wasn't loading when imported into other projects.

# v1.1.1 (2020-12-21)

* Refactored how the local copy of the data file is loaded to be more package
  friendly

# v1.1.0 (2020-12-18)

* Add a local copy of the `tia-utc.dat` file in case the URL options to retrieve
  it are not working.

# v1.0.0 (2019-08-21)

* Remove `LEAP_SECONDS` variable from the `gps` module. Previously, the variable
  `LEAP_SECONDS` was initialized on import-time. This can cause problems for
  code that depends on this package if network accesss to all of the configured
  leap second data sources is unavailable.

# v0.2.7 (2019-08-19)

* Explicitly catch socket timeout errors when requesting leap second
  data. Sometimes we get a socket timeout error when attempting to fetch data
  from one of the leap second sources. This should be raised as a URLError or a
  TimeoutError but in practice we sometimes see `socket.timeout` errors.

# v0.2.6 (2019-04-08)

* Streamline the CI build and release.
* Add a build target for Python 3.7

# v0.2.5 (2018-11-15)

* Add additional sources for leap second data. When the primary source of leap
  second data is unavailable (we have experienced downtime multiple times),
  fallback on one of the official mirrors for this data.
* Round microseconds in gps_to_utc conversion.

# v0.2.4 (2018-03-06)

* Fix microseconds bug. Microseconds >= 999500 were rounded to 1000
  milliseconds.

# v0.2.3 (2018-03-01)

* Build for Python 3.5 & 3.6

# v0.2.2 (2018-03-01)

* Initial release as an independent package.
