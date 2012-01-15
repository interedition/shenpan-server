"""Simple example of how to apply a rule."""

import requests
from requests.auth import HTTPBasicAuth

try:
    import json
except ImportError:
    import simplejson as json


EXAMPLE_DATA = {
    'witnesses': [
        {"id": "A", "tokens": [
            {"t": "A"}, {"t": "black"}, {"t": "cat"}]},
        {"id": "B", "tokens": [
            {"t": "A"},
            {"t": "white"},
            {"t": "kitten"},
            {"t": "in"},
            {"t": "a"},
            {"t": "basket."},
        ]}
    ],
    'context': 'T-NT-01-4-3-16',
}

HEADERS = {'content-type': 'application/json',
           'charset': 'UTF-8',
           'Accept': 'application/json'}

def apply_rule(data, headers):
    url = "http://localhost:8000/api/apply/"
    req = requests.post(url, data=json.dumps(data), headers=headers,
                        auth=HTTPBasicAuth('admin', 'admin'))
    return req.content.encode('utf8')

def main():
    """Run the function when this file is called."""
    print apply_rule(EXAMPLE_DATA, HEADERS)

if __name__ == "__main__":
    main()
