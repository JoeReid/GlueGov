"""
DCLG - Department for Communities and Local Government
    http://data.gov.uk/publisher/department-for-communities-and-local-government
"""

from gluegov.lib.tables import XLSTable


XLSTable(
    "dclg",
    "incomedomain",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6873/1871528.xls",
    "incomedomain.xls"
)
XLSTable(
    "dclg",
    "employmentdomain",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6874/1871534.xls",
    "employmentdomain.xls"
).parse(sheet=1, lastRow=32483)
XLSTable(
    "dclg",
    "healthdomain",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6875/1871537.xls",
    "healthdomain.xls"
)
