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
