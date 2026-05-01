import ssl
import certifi
import urllib.request

url = "https://github.com/marquisedemaree/RAT/releases/download/v1.0/data.zip"
out = "https://github.com/marquisedemaree/RAT/releases/download/v1.0/models.zip"

ssl_context = ssl.create_default_context(cafile=certifi.where())

urllib.request.urlretrieve(url, out)
