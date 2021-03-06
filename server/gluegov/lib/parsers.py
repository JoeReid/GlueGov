""" Parser module that describes Parser that read a file, (hope is to support
xls, cvs, odt?) and makes the parsed content easilty addressable.
"""
import xlrd
import csv


class Parser(object):

    def __init__(self, fileName):
        self.records = []
        self.fileName = fileName

    def parse(self):
        raise NotImplementedError


class CSVParser(Parser):

    def parse(self, *args, keyRow=0, firstRow=None, lastRow=None, fieldnames=None):
        """ Parse the CSV file
        :param args: arguments passed to csv.DictReader
        :param kwargs: keyword arguments passed to csv.DictReader
        :return:
        """
        with open(self.fileName, "r") as f:
            reader = csv.reader(f)
            lines = [x for x in reader]

            if fieldnames is not None:
                self.fields = fieldnames
            else:
                self.fields = lines[keyRow]

            if firstRow is None:
                firstRow = keyRow + 1
            if lastRow is None:
                lastRow = len(lines)-firstRow

            for i in range(firstRow, lastRow+1):
                data = lines[i]
                self.records.append(dict(zip(self.fields, data)))


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
