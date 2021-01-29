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

cmdName = sys.argv[1] if len(sys.argv) > 1 else "turn"
cmdValue = sys.argv[2] if len(sys.argv) > 2 else "on"

data = {
    "device": DEVICE,
    "model": MODEL,
    "cmd": {
        "name": cmdName,
        "value": int(cmdValue) if cmdName == 'brightness' else cmdValue
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
    print(data)
    print(response.json())
