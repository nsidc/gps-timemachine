NOTES on GPS -> UTC convertion
------------------------------

GPS time is offset from UTC because UTC time includes leap seconds but GPS does
not. Unfortunately, leap seconds are not added on a well defined schedule, so
the only way to know the GPS-UTC offset is to look up the historical record of
leap second additions. We currently know of three ways this can be accomplished:

1) CURRENTLY IMPLEMENTED - Query a remote resource to get the current list of
leap seconds. In this case, we're using a url at the US Naval Observatory, but
there may be others. With the list of leap seconds and when they were applied,
you can determine the appropriate GPS-UTC offset for any date.
PROS - should always be up-to-date. Fast.
CONS - relies on an external url which could be down for some reason

2) Python package - Use a python package like astropy that has different time
conversions built in. For a possible implementation, see
https://bitbucket.org/nsidc/valkyrie-ingest/commits/51631bdfe3a5ea875f430bd55b60fe18f98174aa.
which uses TAI time as an intermediate. TAI is always 19 seconds ahead of GPS,
and GPS is a variable number of seconds ahead of UTC, depending on the date and t
ime. For exact delta between UTC and TAI, see:
http://hpiers.obspm.fr/eop-pc/index.php?index=TAI-UTC_tab&lang=en
PROS - no external resources required
CONS - First implementation was much slower. Package may need to be updated to
get new leap seconds as they are added?

3) OS file - Read the file(s) on the OS that store time and date information.
For example, /usr/share/zoneinfo
PROS - should be fast, like option #1. Doesn't rely on an external url
CONS - could be platform dependent? OS would need to be updated to get new
files as they are available.
