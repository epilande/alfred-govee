#!/usr/bin/python3

import sys
import os
import argparse
import json
dirname = os.path.dirname(__file__)
sys.path.append(os.path.join(dirname, "lib"))

from lib import requests

parser = argparse.ArgumentParser()
parser.add_argument('--fetch', default=False, action='store_true')
args = parser.parse_args()
shouldFetch = args.fetch

API_KEY = os.environ["API_KEY"]
DEBUG = False


def fetchDevices():
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

    with open(os.path.join(dirname, './devices.json'), 'w') as json_file:
        json.dump({'items': items}, json_file)

    return json.dumps({'items': items})


def listDevices():
    try:
        with open(os.path.join(dirname, './devices.json')) as f:
            data = json.load(f)
            print(json.dumps(data))
    except FileNotFoundError:
        data = fetchDevices()
        print(data)


if __name__ == '__main__':
    if (shouldFetch == True):
        fetchDevices()
    else:
        listDevices()
