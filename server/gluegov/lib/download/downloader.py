import requests
# import concurrent.futures


class Downloader(object):
    # downloadExecutor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    def __init__(self, url, dest):
        response = requests.get(url)
        open(dest, 'wb').write(response.content)
