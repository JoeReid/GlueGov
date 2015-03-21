"""
"""
from gluegov.lib.tables import CSVTable


# https://www.gov.uk/about-the-price-paid-data
CSVTable(
    "landregistry",
    "pricepaid",
    "http://publicdata.landregistry.gov.uk/market-trend-data/price-paid-data/b/pp-2015.csv",
    "price-paid-2015.csv"
).parse(fieldnames=(
    "id", "price", "date", "postcode", "type", "age", "duration", "name",
    "secondname", "street", "locality", "town", "district", "county", "record"
))
