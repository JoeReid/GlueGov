"""
"""
from gluegov.lib.tables import CSVTable


pricepaid = CSVTable(
    "http://publicdata.landregistry.gov.uk/market-trend-data/price-paid-data/b/pp-2015.csv",
    "price-paid-2015.csv"
).parse(fieldnames=(
    "id", "price", "date", "postcode", "_", "__", "__", "number", "name",
    "street", "second name", "town", "city", "county", "____"
))
