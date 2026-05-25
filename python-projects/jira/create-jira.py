# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://###################.atlassian.net/rest/api/3/issue"

api_token = "###########################"
auth = HTTPBasicAuth("#######################@gmail.com", api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload_dict = {
    "fields": {
        "project": {
            "key": "KAN"
        },
        "summary": "Second Jira ticket Devops project",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Order entry fails when selecting supplier."
                        }
                    ]
                }
            ]
        },
        "environment": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "UAT"
                        }
                    ]
                }
            ]
        },
        "duedate": "2026-07-11",
        "issuetype": {
            "name": "Task"
        }
    },
    "update": {}
}
payload = json.dumps(payload_dict)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))