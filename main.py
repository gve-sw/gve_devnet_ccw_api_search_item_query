""" Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests
import datetime
from lxml import etree
import xml.etree.ElementTree as ET
import re
import requests
import datetime
from lxml import etree
import xml.etree.ElementTree as ET
import json
import config



# Change to true to enable request/response debug output
DEBUG = True

# Once the user is authenticated, the sessionTicket for all API requests will be stored here
sessionSecurityContext = {}


# Custom exception for errors when sending requests
class SendRequestError(Exception):

    def __init__(self, result, reason):
        self.result = result
        self.reason = reason

    pass


# Generic function for sending XML API requests
#   envelope : the full XML content of the request
def sendRequest(envelope,bearer_token):
    if DEBUG:
        print(envelope)

    # Use the requests library to POST the XML envelope to the Webex API endpoint
    headers = {'Content-Type': 'application/xml',
                'Accept': 'application/xml',
                'Authorization': bearer_token
                }
    response = requests.request('POST','https://api-test.cisco.com/commerce/CONFIG/v1/POE/searchItem', data=envelope, headers=headers)

    # Check for HTTP errors
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SendRequestError('HTTP ' + str(response.status_code), response.content.decode("utf-8"))

    # Use the lxml ElementTree object to parse the response XML
    message = etree.fromstring(response.content)

    if DEBUG:
        print(etree.tostring(message, pretty_print=True, encoding='unicode'))

        # Use the find() method with an XPath to get the 'result' element's text
    # Note: {*} is pre-pended to each element name - ignores namespaces
    # If not SUCCESS...
    if response.status_code == 200:
        print(response.text)
        return etree.tostring(message, pretty_print=True, encoding='unicode')

    return message



def SearchItemBuildRequest():
    # Passing the path of the
# xml document to enable the
# parsing process
    tree = ET.parse('body.xml')

    with open('body.xml') as f:
        request = f.read().replace('\n', '')

    return request


def SearchItem(bearer_token):
    request = SearchItemBuildRequest()

    response = sendRequest(request,bearer_token)

    return response


url = f"https://cloudsso.cisco.com/as/token.oauth2"
payload = {
    "client_id":config.client_id,
    "client_secret":config.client_secret,
    "grant_type":"password",
    "username":config.username,
    "password":config.password
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Accept": "application/xml",
}
response = requests.request('POST', url, headers=headers, data=payload)

response = json.loads(response.text)

token = response["access_token"]

#bearer_token = "Bearer " + token
bearer_token = "Bearer " + token

resp = SearchItem(bearer_token)

f = open("output.xml", "w")
f.write(resp)
f.close()