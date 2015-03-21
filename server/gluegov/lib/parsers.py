""" Parser module that describes Parser that read a file, (hope is to support
xls, cvs, odt?) and makes the parsed content easilty addressable.
"""
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
