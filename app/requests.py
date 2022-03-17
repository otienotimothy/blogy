import urllib.request
import json

def get_quotes():
    url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(url) as fetch:
        res = fetch.read()
        data = json.loads(res)

    return data