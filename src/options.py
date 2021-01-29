#!/usr/bin/python3

import os
import sys
import json

query = sys.argv[1].strip() if len(sys.argv) > 1 else ''
DEVICE_NAME = os.environ["DEVICE_NAME"]
MODEL = os.environ["MODEL"]


def clamp(n, minn, maxn): return max(min(maxn, n), minn)


items = [
    {
        "title": "Turn on",
        "subtitle": f"{DEVICE_NAME} - {MODEL}",
        "arg": "turn on"
    },
    {
        "title": "Turn off",
        "subtitle": f"{DEVICE_NAME} - {MODEL}",
        "arg": "turn off"
    },
]


if query == '' or query.isnumeric():
    num = str(clamp(int(query) if query else 0, 0, 100))
    items.append({
        "title": f"Adjust brightness {num if query else '0 – 100'}",
        "subtitle": f"{DEVICE_NAME} - {MODEL}",
        "arg": f"brightness {num}"
    })

filteredItems = [item for item in items if query in item['title'].lower()]

print(json.dumps({'items': filteredItems if query else items}))
