"""Silly CollateX example by Zeth.
Helps to make tests and usecases.

Of course needs the requests module. One of the following commands may help:

apt-get python-requests
easy_install requests
pip install requests

You also need the json module (which you probably already have),
if not then use, one of the following

apt-get install python-simplejson
easy_install simplejson
pip install simplejson
"""

import requests

try:
    import json
except ImportError:
    import simplejson as json


HEADERS = {'content-type': 'application/json',
           'charset': 'UTF-8',
           'Accept': 'application/json'}


EXAMPLE_WITNESSDICT = {
    'witnesses': [
        {"id": "A",
         "tokens": [
                {"t": "A"},
                {"t": "black"},
                {"t": "cat"}
                ]},
        {"id": "B",
         "tokens": [
                {"t": "A"},
                {"t": "white"},
                {"t": "kitten.", "n": "cat"},
                {"t": "in"},
                {"t": "a"},
                {"t": "basket."},
                ]}
        ]
    }


def collate_witnesses(witnessdict, headers):
    """Send witnesses off to Gregor's server to be collated."""
    witnessjson = json.dumps(witnessdict)
    url = "http://gregor.middell.net/collatex/api/collate"
    req = requests.post(url, data=witnessjson, headers=headers)
    return req.content.encode('utf8')


def main():
    """Run the function when this file is called."""
    print collate_witnesses(EXAMPLE_WITNESSDICT, HEADERS)

if __name__ == "__main__":
    main()
