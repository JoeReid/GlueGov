import requests
import concurrent.futures
import logging
import os.path


class Downloader(object):
    downloadExecutor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    def __init__(self, url, dest):
        self.url = url
        self.dest = dest

        logging.getLogger().setLevel(20)

        if os.path.isfile(dest):
            logging.info("File " + dest + " already exists: Not Downloading")
        else:
            logging.info("Downloading File: " + dest)
            try:
                future = Downloader.downloadExecutor.submit(self._download)
                future.result()
            except Exception:
                logging.error("Downloading " + dest + " failure!")

            logging.info("Downloading " + dest + ": Done")

    def _download(self):
        response = requests.get(self.url)
        open(self.dest, 'wb').write(response.content)
