import urllib.request
from urllib.parse import urlparse, quote
import json
import tempfile
import os

TEMP_DIR  =  tempfile.TemporaryDirectory()

class Library:
    def __init__(self, url):
        self.url = url
        self.title = urlparse(url).netloc
        self.library = self.get_library()
        self.tmp_cache = list()        

    def get_library(self):
        with urllib.request.urlopen(f"{self.url}/songs") as url:
            data = json.loads(url.read().decode())
        library = {'title': self.title, 'items': data}
        return library

    def get_url(self, index):
        path = self.library['items'][int(index)].get('cached_path', None)
        if not path:
            url = f"{self.url}/{self.library['items'][int(index)]['path']}"
            path = urllib.request.urlretrieve(url)[0]
            self.library['items'][int(index)]['cached_path'] = path
        return path
   
    def precache(self, index):
        path = self.library['items'][int(index)].get('cached_path', None)
        if not path:
            url = f"{self.url}/{self.library['items'][int(index)]['path']}"
            url = urllib.parse.quote(url, encoding='utf-8', safe='%;/?:@&=+$,')
            path = urllib.request.urlretrieve(url)[0]
            self.library['items'][int(index)]['cached_path'] = path
            self.tmp_cache.append(path)
            self._clean_cache()

    def _clean_cache(self):
        if len(self.tmp_cache) >= 20:
            to_remove = self.tmp_cache.pop(0)
            os.remove(to_remove)
