"""
"""
from gluegov.lib.tables import CSVTable


# https://www.gov.uk/about-the-price-paid-data
CSVTable(
    "traffic",
    "majorroads",
    "http://data.dft.gov.uk/gb-traffic-matrix/Traffic-major-roads-miles.csv",
    "road_traffic.csv"
).parse()


#http://data.gov.uk/dataset/gb-road-traffic-counts/resource/bc89410e-5a0a-4b6d-a6e1-e206d138fbb0
#http://data.dft.gov.uk/gb-traffic-matrix/Traffic-major-roads-km.csv