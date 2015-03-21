""" Parser module that describes Parser that read a file, (hope is to support
xls, cvs, odt?) and makes the parsed content easilty addressable.
"""
import xlrd
from csv import DictReader


class Parser(object):

    def __init__(self, fileName):
        self.records = []
        self.fileName = fileName

    def parse(self):
        raise NotImplementedError


class CSVParser(Parser, DictReader):

    def parse(self, *args, **kwargs):
        """ Parse the CSV file
        :param args: arguments passed to csv.DictReader
        :param kwargs: keyword arguments passed to csv.DictReader
        :return:
        """
        with open(self.fileName, "r") as f:
            dictReader = DictReader(f, *args, **kwargs)
            self.fields = dictReader.fieldnames
            self.records = [r for r in dictReader]
            return self

class XLSParser(Parser):

    def parse(self, sheet=0, keyRow=0, lastRow=0):

        # open file and get the correct sheet
        b = xlrd.open_workbook(self.fileName)
        s = b.sheet_by_index(sheet)

        # get keys
        keylist = s.row_values(keyRow)
        self.fields = keylist

        # for each line create dict and add to records
        for x in range(keyRow+1, lastRow):
            row = s.row_values(x)
            rowDict = dict(zip(keylist, row))
            self.records.append(rowDict)

        # old way left for giggles
        # self.records = [dict(zip(keylist,s.row_values(n))) for n in range(keyRow+1, lastRow+1)]

        return self
