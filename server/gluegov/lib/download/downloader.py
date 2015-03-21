import requests
import concurrent.futures


class Downloader(object):
    downloadExecutor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    def __init__(self, url, dest):
        self.url = url
        self.dest = dest
        future = Downloader.downloadExecutor.submit(self._download)
        future.result()

    def _download(self):
        response = requests.get(self.url)
        open(self.dest, 'wb').write(response.content)
