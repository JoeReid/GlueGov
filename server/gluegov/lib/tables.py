""" Collection of tables, a collection of records with filtering methods

Using the word table, due to lack of a better idea!
"""
import os
import configparser

from gluegov.lib.parsers import CSVParser
from gluegov.lib.download.downloader import Downloader

config = configparser.ConfigParser()
config.read("development.ini")


class Table(object):
    SUPPORTED_FUNCS = ["eq", "gt", "lt", "gte", "lte", "neq"]

    def __init__(self, records):
        self.records = records

    def _filter(self, func):
        return [elem for elem in filter(func, self.records)]

    def eq(self, field, value):
        return Table(self._filter(lambda d: d[field] == value))

    def gt(self, field, value):
        return Table(self._filter(lambda d: d[field] > value))

    def lt(self, field, value):
        return Table(self._filter(lambda d: d[field] < value))

    def gte(self, field, value):
        return Table(self._filter(lambda d: d[field] >= value))

    def lte(self, field, value):
        return Table(self._filter(lambda d: d[field] <= value))

    def neq(self, field, value):
        return Table(self._filter(lambda d: d[field] != value))

    def proccesQuery(self, query):
        table = self
        if query.startswith('?'):
            query = query[1:]

        # loop over the commands
        for block in query.split("&"):
            (field, command) = block.split('=')
            subcommands = command.split(':')

            if len(subcommands) < 2:
                subcommand = "eq"
                value = subcommands
            else:
                subcommand = subcommands[0]
                value = subcommands[1]

            if subcommand in Table.SUPPORTED_FUNCS:
                table = table.__getattribute__(subcommand)(field, value)

        return table

    def __repr__(self):
        return self.records


class TableDownloadMixin(Table, Downloader):

    def __init__(self, url, fileName):
        Table.__init__(self, [])
        self.fileName = os.path.join(
            os.getcwd(), config.get("app:main", "gluegov.data_directory"),
            fileName
        )

        Downloader.__init__(self, url, self.fileName)


class CSVTable(TableDownloadMixin, CSVParser):

    def __init__(self, url, fileName):
        TableDownloadMixin.__init__(self, url, fileName)
        CSVParser.__init__(self, self.fileName)


class XLSTable(TableDownloadMixin):
    def __init__(self, url, fileName):
        TableDownloadMixin.__init__(self, url, fileName)
