import json

import requests

ENDPOINT = "http://127.0.0.1:8000/api/songs/"


def do(method="get", data={}, is_json=True):
    headers = {}
    if is_json:
        headers["content-type"] = "application/json"
        data = json.dumps(data)
    return requests.request(method, ENDPOINT, data=data)


do()
do(method="post", data={"name": "cool name"})
do(data={"id": 1})
do(method="put", data={"id": 1, "name": "new cool name"})
do()
