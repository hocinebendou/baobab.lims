import requests
from requests.auth import HTTPBasicAuth

top_level_url = 'http://localhost:8080/Plone'
username = 'admin'
password = 'hocine'

auth = HTTPBasicAuth(username, password)
url = top_level_url + '/@@API/v3/create'

data = {"BODY": '[{ \
        "portal_type": "Project", \
        "parent_path": "clients/client-1", \
        "ProjectType": "eclectic", \
        "title": "White Goblin lvl 1", \
        "description": "Cleaning up the side effects of Goblin serum", \
        "ProjectTheme": "412", \
        "EndDate": "2020-12-31", \
        "StartDate": "2018-01-31", \
        "DateCreated": "2018-02-22", \
        "SampleType": ["Blood Plasma", "Serum"], \
        "Service": ["DNA concentration","Mass Spectrometry"] \
        }]'
}

request = requests.post(url, data=data, auth=auth)
# show the response content
print(request.content)
