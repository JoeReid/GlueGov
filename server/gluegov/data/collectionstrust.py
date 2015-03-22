"""
Collections trust
    http://data.gov.uk/dataset/uk-public-library-contacts-14032012/resource/0432918c-5654-467e-8428-8413bb41f44e
"""

from gluegov.lib.tables import XLSTable

XLSTable(
    "collectionstrust",
    "publiclibrariescontact",
    "http://www.culturegrid.org.uk/wp-content/uploads/2012/07/ukpublib05072012.xls",
    "publiclibrariescontact.xls"
).parse(lastRow=4040)
