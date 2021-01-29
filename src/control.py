#!/usr/bin/python3

import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

from lib import requests

API_KEY = os.environ["API_KEY"]
DEVICE = os.environ["DEVICE"]
MODEL = os.environ["MODEL"]

DEBUG = False

power = sys.argv[1] if len(sys.argv) > 1 else "on"
data = {
    "device": DEVICE,
    "model": MODEL,
    "cmd": {
        "name": "turn",
        "value": power
    }
}

response = requests.put(
    "https://developer-api.govee.com/v1/devices/control",
    headers={
        "Govee-API-Key": API_KEY,
        "Content-Type": "application/json",
    },
    data=json.dumps(data)
)


if DEBUG:
    print(DEVICE)
    print(MODEL)
    print(power)
    print(json.dumps(response.json(), indent=4))
