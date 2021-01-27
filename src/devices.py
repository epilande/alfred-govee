#!/usr/bin/python3

import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from lib import requests

API_KEY = os.environ["API_KEY"]
DEBUG = False

response = requests.get(
    "https://developer-api.govee.com/v1/devices",
    headers={
        "Govee-API-Key": API_KEY,
        "Content-Type": "application/json",
    }
)

json_response = response.json()
devices = json_response.get('data', {}).get('devices')

if DEBUG:
    print(json.dumps(json_response, indent=4))


def item(d):
    return {
        "title": d["deviceName"],
        "subtitle": d["model"],
        "arg": f"{d['device']}, {d['model']}, {d['deviceName']}"
    }


items = list(map(item, devices))

print(json.dumps({'items': items}))
