from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os
app = Flask(__name__)

@app.route('/github_webhook', methods=['POST'])
def github_webhook():

    data = request.json

    #Comment body
    comment_body = data['comment']['body']

    print("Comment:", comment_body)

    #Only create Jira ticket if /jira exists in the comment body
    if "/jira" not in comment_body:
        return "No Jira ticket created as /jira not found in comment body.", 200

    #Get issue title 
    issue_title = data['issue']['title']



    url = os.getenv("my_url") #https://#################.atlassian.net/rest/api/3/issue
    API_TOKEN = os.getenv("api_token")
    auth = HTTPBasicAuth("###############@email.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }


    payload_dict = {
       "fields": {
            "project": {
                "key": "KAN"
            },
            "summary": issue_title,
            "issuetype": {
                "name": "Task"
            }
        } 
    }
    response = requests.post(
    url,
    data=json.dumps(payload_dict),
    headers=headers,
    auth=auth
)

    print(response.text)

    return "Jira ticket created successfully.", 200


app.run(host='0.0.0.0', port=5000)



