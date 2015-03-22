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
).parse(sheet=1, lastRow=32483)
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
).parse(sheet=1, lastRow=32483)
XLSTable(
    "dclg",
    "skillstrainingdomain",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6876/1871555.xls",
    "skillstrainingdomain.xls"
).parse(sheet=1, lastRow=32483)
XLSTable(
    "dclg",
    "housingandservicebarriers",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6877/1871559.xls",
    "housingandservicebarriers.xls"
).parse(sheet=1, lastRow=32483)
XLSTable(
    "dclg",
    "livingenvironmentdomain",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6879/1871567.xls",
    "livingenvironmentdomain.xls"
).parse(sheet=1, lastRow=32483)
XLSTable(
    "dclg",
    "criminaldomain",
    "https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/6878/1871562.xls",
    "criminaldomain.xls"
).parse(sheet=1, lastRow=32483)
