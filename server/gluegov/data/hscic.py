"""
"""
from gluegov.lib.tables import CSVTable

#Heath social care information centre

#http://www.hscic.gov.uk/catalogue/PUB15937/mhmds-monthly-mrd-aug-2014.csv
CSVTable(
    "hscic",
    "mentalhealth",
    "http://www.hscic.gov.uk/catalogue/PUB15937/mhmds-monthly-mrd-aug-2014.csv",
    "mhmds-monthly-mrd-aug-2014.csv"
).parse()