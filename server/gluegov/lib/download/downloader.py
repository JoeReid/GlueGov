import urllib.request


class Downloader(object):
    def __init__(self, url, dest):
        urllib.request.urlretrieve(url, dest)
