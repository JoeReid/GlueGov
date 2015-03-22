"""
"""

from gluegov.lib.tables import XLSTable
import xlrd

def format(x):
    try:
        return str(int(x))
    except:
        return str(x)

def isNotEmpty(x):
    return x != "" and x != " "

class onsXLSTable(XLSTable):
    def parse(self):
        # open file and get the correct sheet
        b = xlrd.open_workbook(self.fileName)
        s = b.sheet_by_index(1)

        # get keys
        keylist1 = s.row_values(9)
        keylist2 = s.row_values(10)

        # map keylists to one keylist
        keylist = [e for e in map(lambda x, y: x+" "+format(y), keylist1, keylist2)]
        keylist = [e for e in filter(lambda x: isNotEmpty(x), keylist)]
        self.fields = keylist

        for x in range(13, 463):
            row = s.row_values(x)
            row = [e for e in filter(lambda x: isNotEmpty(x), row)]
            if row != []:
                rowDict = dict(zip(keylist, row))
                self.records.append(rowDict)






onsXLSTable(
    "ons",
    "population-and-household-estimates",
    "http://www.ons.gov.uk/ons/rel/census/2011-census/population-and-household-estimates-for-england-and-wales---unrounded-figures-for-the-data-published-16-july-2012/rft-1-2-ew-pp04.xls",
    "population-and-household-estimates.xls"
).parse()
