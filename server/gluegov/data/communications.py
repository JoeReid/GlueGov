"""
"""
from gluegov.lib.tables import CSVTable


CSVTable(
    "communications",
    "broadbandcoverage",
    "http://d2a9983j4okwzn.cloudfront.net/downloads/ofcom-uk-broadband-speed-data-2013.csv",
    "broadband_coverage_2013.csv"
).parse(keyRow=1)

CSVTable(
    "communications",
    "mopbilecoverage",
    "http://d2a9983j4okwzn.cloudfront.net/downloads/ofcom-uk-mobile-coverage-data-2012.csv",
    "mobile_coverage_2012.csv"
).parse(keyRow=1)

#http://d2a9983j4okwzn.cloudfront.net/downloads/ofcom-uk-broadband-speed-data-2013.csv
#http://d2a9983j4okwzn.cloudfront.net/downloads/ofcom-uk-mobile-coverage-data-2012.csv