import requests
import json

ENDPOINTS = {
    'version': '/api/v1/msf/version'
}


class Msf:

    url = 'https://localhost:8080'

    def __init__(self, username, password, token):
        self.username = username
        self.password = password
        self.token = token

    def version(self):
        headers = {'Authorization': str('Bearer ' + self.token), 'Content-type': 'application/json'}
        api_response = requests.get(url=self.url+ENDPOINTS.get('version'), headers=headers, verify=False)
        api_response_dict = json.loads(api_response.text)
        return api_response_dict.get('data').get('metasploit_version')


