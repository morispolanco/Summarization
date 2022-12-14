import requests
import os

TOKEN = os.getenv("KEY")

def conect_resumidor(data):
    url = 'https://api.deepai.org/api/summarization'
    headers = {"Content-Type": "application/json", "Authorization": api-key}

    text = {
        "text":data
    }

    response = requests.post(url, json=text, headers=headers)

    if response.status_code == 200:
        return response.json(), response.status_code
    else:
        return {"Error": response.status_code}, response.status_code
