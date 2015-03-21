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
    pass


class TableDownloadMixin(Table, Downloader):

    def __init__(self, url, fileName):
        self.fileName = os.path.join(
            os.getcwd(), config.get("app:main", "gluegov.data_directory"),
            fileName
        )

        Downloader.__init__(self, url, self.fileName)


class CSVTable(TableDownloadMixin, CSVParser):

    def __init__(self, url, fileName):
        TableDownloadMixin.__init__(self, url, fileName)
        CSVParser.__init__(self, self.fileName)
