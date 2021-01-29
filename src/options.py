#!/usr/bin/python3

import os
import json

DEVICE_NAME = os.environ["DEVICE_NAME"]
MODEL = os.environ["MODEL"]

print(json.dumps({'items': [
    {
        "title": "Turn on",
        "subtitle": f"{DEVICE_NAME} - {MODEL}",
        "arg": "on"
    },
    {
        "title": "Turn off",
        "subtitle": f"{DEVICE_NAME} - {MODEL}",
        "arg": "off"
    },
]}))
