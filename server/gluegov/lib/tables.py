""" Collection of tables, a collection of records with filtering methods

Using the word table, due to lack of a better idea!
"""
import os
import urllib.parse
import configparser

from functools import partial
from collections import defaultdict
from gluegov.lib.parsers import CSVParser
from gluegov.lib.parsers import XLSParser
from gluegov.lib.download.downloader import Downloader

config = configparser.ConfigParser()
config.read("development.ini")


class Table(object):
    SUPPORTED_FUNCS = ["eq", "gt", "lt", "gte", "lte", "neq", "con"]

    def __init__(self, fields, records):
        self.records = records
        self.fields = fields

        self.tablePartial = None


    def _filter(self, func, value):
        types = [str, urllib.parse.unquote, int, float]
        for t in types:
            try:
                t(value)
            except:
                pass
            else:
                value = t(value)
                type = t

        return [record for record in self.records if func(record, value, type)]

    def eq(self, field, value):
        return self.tablePartial(self._filter(lambda d, v, t: t(d[field]) == v, value))

    def gt(self, field, value):
        return self.tablePartial(self._filter(lambda d, v, t: t(d[field]) > v, value))

    def lt(self, field, value):
        return self.tablePartial(self._filter(lambda d, v, t: t(d[field]) < v, value))

    def gte(self, field, value):
        return self.tablePartial(self._filter(lambda d, v, t: t(d[field]) >= v, value))

    def lte(self, field, value):
        return self.tablePartial(self._filter(lambda d, v, t: t(d[field]) <= v, value))

    def neq(self, field, value):
        return self.tablePartial(self._filter(lambda d, v, t: t(d[field]) != v, value))

    def con(self, field, value):
        def contains(d, v, t):
            return v in t(d[field]).lower()
        return self.tablePartial(self._filter(contains, value))

    def proccesQuery(self, query):
        self.tablePartial = partial(Table, self.fields)
        table = self

        if query:
            if query.startswith('?'):
                query = query[1:]

            # loop over the commands
            for block in query.split("&"):
                (field, command) = block.split('=')
                subcommands = command.split(':')

                if len(subcommands) >= 2:
                    subcommand = subcommands[0]
                    value = subcommands[1]
                else:
                    continue

                if subcommand in Table.SUPPORTED_FUNCS:
                    table = table.__getattribute__(subcommand)(field, value)

        return table


class TableDownloadMixin(Table, Downloader):

    registry = defaultdict(dict)

    def __init__(self, group, name, url, fileName):
        Table.__init__(self, [], [])
        TableDownloadMixin.registry[group][name] = self
        self.group = group
        self.name = name
        self.fileName = os.path.join(
            os.getcwd(), config.get("app:main", "gluegov.data_directory"),
            fileName
        )

        Downloader.__init__(self, url, self.fileName)


class CSVTable(TableDownloadMixin, CSVParser):
    def __init__(self, group, name, url, fileName):
        TableDownloadMixin.__init__(self, group, name, url, fileName)
        CSVParser.__init__(self, self.fileName)


class XLSTable(TableDownloadMixin, XLSParser):
    def __init__(self, group, name, url, fileName):
        TableDownloadMixin.__init__(self, group, name, url, fileName)
        XLSParser.__init__(self, self.fileName)
