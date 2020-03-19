import urllib.request
from urllib.parse import urlparse
import json


class Library:
    def __init__(self, url):
        self.url = url
        self.title = urlparse(url).netloc
        self.lib = self.get_library()

    def get_library(self):
        with urllib.request.urlopen(f"{self.url}/songs") as url:
            data = json.loads(url.read().decode())
        library = {'title': self.title, 'items': data}
        return library

