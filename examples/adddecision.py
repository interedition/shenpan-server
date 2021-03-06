"""Simple example of how to add a rule."""

import requests
from requests.auth import HTTPBasicAuth

try:
    import json
except ImportError:
    import simplejson as json


EXAMPLE_ADD_RULE = {'external_user': 'bob',
                    'scope': 'global',
                    'context': 'T-NT-01-4-3-16',
                    'regularisation_type': 'orthographic',
                    'token': 'kitten',
                    'lemma': 'cat',}

HEADERS = {'content-type': 'application/json',
           'charset': 'UTF-8',
           'Accept': 'application/json'}

def add_rule(newrule, headers):
    """Try to add a rule to the server."""
    newrulejson = json.dumps(newrule)
    url = "http://www.annotation.bham.ac.uk/api/"
    req = requests.post(url,
                        data=newrulejson,
                        headers=headers,
                        auth=HTTPBasicAuth('interedition', 'PASSWORD'))
    return req.content.encode('utf8')


def main():
    """Run the function when this file is called."""
    print add_rule(EXAMPLE_ADD_RULE, HEADERS)

if __name__ == "__main__":
    main()
