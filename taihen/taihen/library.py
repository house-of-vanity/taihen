import urllib.request
import json


class Library:
    def __init__(self, url):
        self.url = url
        self.lib = self.get_library()

    def get_library(self):
        with urllib.request.urlopen(f"{self.url}/songs") as url:
            lib = json.loads(url.read().decode())
        return lib
